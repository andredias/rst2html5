#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

__version__ = '0.1'

import os
import re
import docutils
from docutils import nodes, writers, frontend
from docutils.math import pick_math_environment
from genshi.builder import tag, Fragment
from genshi.output import XHTMLSerializer

class HTML5Writer(writers.Writer):

    supported = ('html', 'html5', 'html5css3')

    config_section = 'html5writer'
    config_section_dependencies = ('writers')

    settings_spec = (
        'HTML5 Specific Options',
        None, (
        ("Don't indent output", ['--no-indent'],
            {'default': 1, 'action': 'store_false', 'dest': 'indent_output'}),
        ("Don't show id in sections", ['--show-ids'],
            {'default': 0, 'action': 'store_false', 'dest': 'show_ids'})
    ))

    settings_defaults = {'tab_width': 4}

    def __init__(self):
        writers.Writer.__init__(self)
        self.translator_class = HTML5Translator
        return

    def translate(self):
        visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.output
        self.head = visitor.head
        self.body = visitor.body
        return

    def assemble_parts(self):
        writers.Writer.assemble_parts(self)
        self.parts['head'] = self.head
        self.parts['body'] = self.body
        return



class ElemStack(object):
    def __init__(self, settings):
        self.stack = []
        self.indent_level = 0
        self.indent_output = settings.indent_output
        self.show_ids = settings.show_ids
        self.indent_width = settings.tab_width

    def begin_elem(self):
        self.stack.append([])
        self.indent_level += 1
        return

    def append(self, *fragments):
        '''
        Append fragment to previous element
        '''
        self.stack[-1].append(*fragments)
        return

    def pop(self):
        self.indent_level -= 1
        return self.stack.pop()

    def insert_elem(self, name, attributes=None):
        self.begin_elem()
        self.commit_elem(name, attributes)
        return

    def commit_elem(self, name, attributes=None, indent_elem=True):
        '''
        A new element is create by removing its stack to make a tag.
        This tag is pushed back into its parent's stack.
        '''
        attr = self._adjust_attributes(attributes) if attributes else dict()
        pop = self.stack.pop()
        elem = getattr(tag, name)(*pop, **attr)
        parent_stack = self.stack[-1]
        self.indent_level -= 1
        '''
        Indentation schema:

                current position
                       |
                       v
                  <tag>|
        |   indent   |<elem>
        |indent-1|</tag>
                 ^
             ends here
        '''
        if self.indent_output and indent_elem:
            indent = '\n' + self.indent_width * self.indent_level * ' '
            parent_stack.append(indent)
        parent_stack.append(elem)
        if self.indent_output and indent_elem:
            indent = '\n' + self.indent_width * (self.indent_level - 1) * ' '
            parent_stack.append(indent)
        return

    def pop_fragments(self, num_fragments):
        num_fragments *= -3 if self.indent_output else -1
        parent_stack = self.stack[-1]
        fragments = parent_stack[num_fragments:]
        self.stack[-1] = parent_stack[:num_fragments]
        return fragments

    def group_fragments(self, num_fragments, group_name, group_attributes=None):
        self.stack.append(self.pop_fragments(num_fragments))
        self.commit_elem(group_name, group_attributes)
        return

    def append_to_previous_element(self, *args):
        distance = -2 if self.indent_output else -1
        parent_stack = self.stack[-1]
        elem = parent_stack[distance]
        elem(*args)

    def set_next_elem_attr(self, name, value):
        '''
        The given attribute will be inserted into the attributes of the next element.
        '''
        self.next_elem_attr = {name: value}

    def _adjust_attributes(self, attributes):
        attrs = {}
        replacements = {'refuri': 'href', 'uri': 'src', 'refid': 'href',
            'morerows': 'rowspan', 'morecols': 'colspan', 'classes': 'class',
        }
        for k, v in attributes.items():
            if not v:
                continue
            elif isinstance(v, list):
                v = ' '.join(v)

            if k in ('names', 'dupnames', 'bullet', 'enumtype', 'colwidth',
                    'stub'):
                continue
            elif k in replacements:
                k = replacements[k]
            elif k == 'ids':
                if not self.show_ids:
                    continue
                k = 'id'

            attrs[k] = v

        if getattr(self, 'next_elem_attr', None):
            attrs.update(self.next_elem_attr)
            del self.next_elem_attr
        return attrs



HTMLEquivalency = {
    "abbreviation": "abbr",
    "acronym": "acronym",
    "attribution": "cite",
    "block_quote": "blockquote",
    "bullet_list": "ul",
    "caption": "figcaption",
    "colspec": "col",
    "definition": "dd",
    "definition_list": "dl",
    "description": "td",
    "emphasis": "em",
    "enumerated_list": "ol",
    "image": "img",
    "list_item": "li",
    "literal": "tt",
    "literal_block": "pre",
    "option": "span",
    "option_list": "table",
    "option_list_item": "tr",
    "option_string": "span",
    "paragraph": "p",
    "reference": "a",
    "row": "tr",
    "sidebar": "aside",
    "subscript": "sub",
    "superscript": "sup",
    "term": "dt",
    "title_reference": "cite",
    "transition": "hr",
  }


class HTML5Translator(nodes.GenericNodeVisitor):

    def __init__(self, document):
        nodes.GenericNodeVisitor.__init__(self, document)
        self.heading_level = 0
        self.context = ElemStack(document.settings)
        self.head = []
        self.head.append(tag.meta(charset=self.document.settings.output_encoding))
        return

    @property
    def output(self):
        output = '<!DOCTYPE html>\n<html>\n<head>{head}</head>\n' \
                 '<body>{body}</body>\n</html>'
        if self.document.settings.indent_output:
            indent = '\n' + ' ' * self.document.settings.tab_width
            result = []
            for f in self.head:
                result.append(Fragment()(indent, f))
            result.append('\n')
            self.head = result

        self.head = ''.join(XHTMLSerializer()(Fragment()(*self.head)))
        self.body = ''.join(XHTMLSerializer()(Fragment()(*self.context.pop())))
        return output.format(head=self.head, body=self.body)

    def default_visit(self, node):
        '''
        Each level creates its own stack
        '''
        self.context.begin_elem()
        return

    def default_departure(self, node):
        name = node.__class__.__name__
        if name in HTMLEquivalency:
            name = HTMLEquivalency[name]
        self.context.commit_elem(name, node.attributes)
        return

    def _compacted_paragraph(self, node):
        """
        Determine if the <p> tags around paragraph ``node`` can be omitted.
        Based on from docutils.writers.html4css1.HTMLTranslator.should_be_compact_paragraph
        """
        if (isinstance(node.parent, nodes.document) or
            isinstance(node.parent, nodes.compound)):
            # Never compact paragraphs in document or compound.
            return False
        first = isinstance(node.parent[0], nodes.label) # skip label
        for child in node.parent.children[first:]:
            # only first paragraph can be compact
            if isinstance(child, nodes.Invisible):
                continue
            if child is node:
                break
            return False
        parent_length = len([n for n in node.parent if not isinstance(
            n, (nodes.Invisible, nodes.label))])
        return parent_length == 1

    def visit_paragraph(self, node):
        if self._compacted_paragraph(node):
            raise nodes.SkipDeparture
        else:
            self.default_visit(node)

    def depart_Text(self, node):
        text = node.astext()
        if not getattr(self, 'preserve_space', None):
            text = re.sub(r'\s+', ' ', text)
        self.context.append(text)

    def visit_section(self, node):
        self.default_visit(node)
        self.heading_level += 1

    def depart_section(self, node):
        self.heading_level -= 1
        self.default_departure(node)

    def depart_title(self, node):
        assert self.heading_level >= 0
        if self.heading_level == 0:
            self.heading_level = 1
        self.context.commit_elem('h' + unicode(self.heading_level), node.attributes)

    def depart_subtitle(self, node):
        '''
        The subtitle and its predecessor title should be combined
        into a hgroup
        '''
        # mount the subtitle heading
        subheading_level = 'h' + unicode(self.heading_level + 1)
        self.context.commit_elem(subheading_level)
        # create hgroup
        num_fragments = 2
        self.context.group_fragments(num_fragments, 'hgroup')
        self.heading_level -= 1

    def depart_enumerated_list(self, node):
        '''
        Ordered list.
        It may have a preffix and suffix that must be handled by CSS3 and javascript to
        be presented as intended.

        See:
            http://dev.opera.com/articles/view/automatic-numbering-with-css-counters/
            http://stackoverflow.com/questions/2558358/how-to-add-brackets-a-to-ordered-list-compatible-in-all-browsers
        '''
        if 'enumtype' in node:
            enumtypes = {
                'arabic': '1',
                'loweralpha': 'a',
                'upperalpha': 'A',
                'lowerroman': 'i',
                'upperroman': 'I'
            }
            node['type'] = enumtypes.get(node['enumtype'], '1')
        if node.get('suffix') == '.' and 'preffix' not in node:
            # default suffix doesn't need special treatment
            del node['suffix']
        self.context.commit_elem('ol', node.attributes)

    def _skip_node(self, node):
        """Internal only"""
        raise nodes.SkipNode

    def depart_classifier(self, node):
        self.context.pop() # pop text element internal to classifier
        self.context.append_to_previous_element(
            ' ',
            tag.span(':', class_='classifier-delimiter'),
            ' ',
            tag.span(node.astext(), class_='classifier')
        )

    #
    # table
    #

    def visit_table(self, node):
        self.th_required = 0
        self.in_thead = False
        self.default_visit(node)

    def depart_table(self, node):
        del self.th_required
        del self.in_thead
        self.default_departure(node)

    def depart_colspec(self, node):
        '''
        stub attribute indicates that the column should be a th tag.
        It could be resolved by CSS3 instead...
        see http://demosthenes.info/blog/556/The-HTML-col-and-colgroup-elements
        '''
        if 'stub' in node:
            self.th_required += 1
        self.default_departure(node)

    def visit_thead(self, node):
        self.in_thead = True
        self.default_visit(node)

    def depart_thead(self,node):
        self.in_thead = False
        self.default_departure(node)

    def visit_row(self, node):
        self.th_available = self.th_required
        self.default_visit(node)

    def depart_row(self, node):
        del self.th_available
        self.default_departure(node)

    def depart_entry(self, node):
        if self.in_thead or self.th_available:
            name = 'th'
            self.th_available -= 1
        else:
            name = 'td'

        if 'morerows' in node:
            node['morerows'] = node['morerows'] + 1
        if 'morecols' in node:
            node['morecols'] = node['morecols'] + 1

        self.context.commit_elem(name, node.attributes)

    def depart_reference(self, node):
        if 'name' in node:
            del node['name']
        if 'refid' in node:
            node['refid'] = '#' + node['refid']
        self.default_departure(node)
        return

    def depart_target(self, node):
        if 'refid' in node and len(node['ids']):
            '''
            see test_case: indirect_target_links
            '''
            return
        if 'refid' in node:
            self.context.insert_elem('a', {'id': node['refid']})
        elif 'ids' in node:
            '''
            Previous anchor elements should be removed.
            See test case: propagated_target
            '''
            num_anchors = len(node['ids']) - 1
            if num_anchors > 0:
                self.context.pop_fragments(num_anchors)
        return

    def visit_literal_block(self, node):
        self.preserve_space = True
        self.default_visit(node)
        return

    def depart_literal_block(self, node):
        del self.preserve_space
        self.default_departure(node)
        return

    def depart_inline(self, node):
        self.context.commit_elem('span', node.attributes, indent_elem=False)

    def visit_math_block(self, node):
        '''
        Only MathJax support
        '''
        math_code = node.astext()
        math_env = pick_math_environment(node.astext())
        if 'align' in math_env:
            template = '\\begin{%s}\n%s\n\\end{%s}' % (math_env, math_code, math_env)
            elem = tag.div(template)
        else: # equation
            template = '\(%s\)' % math_code
            elem = tag.span(template)
        elem(class_='math')
        self.context.append(elem)
        src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
        self.head.append(tag.script(src=src))
        raise nodes.SkipNode

    def visit_math(self, node):
        self.visit_math_block(node)

    def visit_document(self, node):
        if 'title' in node:
            self.head.append(tag.title(node['title']))
        self.default_visit(node)

'''
Some elements don't need any visit_ or depart_ processing in HTML5Translator.
'Text', for example, is a leaf node.
'''
pass_visit = ('tgroup', 'definition_list_item', 'Text', 'target', )
pass_depart = ('document', 'tgroup', 'definition_list_item', )
skip_node = ('substitution_definition', )

for name in pass_visit:
    setattr(HTML5Translator, 'visit_' + name, nodes._nop)
for name in pass_depart:
    setattr(HTML5Translator, 'depart_' + name, nodes._nop)
for name in skip_node:
    setattr(HTML5Translator, 'visit_' + name, HTML5Translator._skip_node)
