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
from genshi.core import Markup

class HTML5Writer(writers.Writer):

    supported = ('html', 'html5', 'html5css3')

    config_section = 'html5writer'
    config_section_dependencies = ('writers')

    settings_spec = (
        'HTML5 Specific Options',
        None, (
        ("Don't indent output", ['--no-indent'],
            {'default': 1, 'action': 'store_false', 'dest': 'indent_output'}),
        ("Show sections ids", ['--show-ids'],
            {'default': 0, 'action': 'store_true', 'dest': 'show_ids'})
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
        self.indent_width = settings.tab_width

    def _indent_elem(self, element, indent):
        result = []
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
        if self.indent_output and indent:
            indentation = '\n' + self.indent_width * self.indent_level * ' '
            result.append(indentation)
        result.append(element)
        if self.indent_output and indent:
            indentation = '\n' + self.indent_width * (self.indent_level - 1) * ' '
            result.append(indentation)
        return result

    def append(self, element, indent=True):
        '''
        Append to current element
        '''
        self.stack[-1].append(self._indent_elem(element, indent))
        return

    def begin_elem(self):
        self.stack.append([])
        self.indent_level += 1
        return

    def commit_elem(self, elem, indent=True):
        '''
        A new element is create by removing its stack to make a tag.
        This tag is pushed back into its parent's stack.
        '''
        pop = self.stack.pop()
        elem(*pop)
        self.indent_level -= 1
        self.append(elem, indent)
        return

    def pop(self):
        return self.pop_elements(1)[0]

    def pop_elements(self, num_elements):
        assert num_elements > 0
        parent_stack = self.stack[-1]
        result = []
        for x in range(num_elements):
            pop = parent_stack.pop()
            elem = pop[0 if len(pop) == 1 else self.indent_output]
            result.append(elem)
        result.reverse()
        return result



dv = 'default_visit'
dp = 'default_departure'
pass_ = 'pass'

rst_terms = {
    # 'term': ('tag', 'visit_func', 'depart_func', use_term_in_class, indent_elem)
    # use_term_in_class and indent_elem are optionals. If not given, the default is False, True
    'Text': (None, 'visit_Text', None),
    'abbreviation': ('abbr', dv, dp),
    'acronym': (None, dv, dp),
    'address': (None, None, None),
    'admonition': ('aside', 'visit_aside', 'depart_aside', True),
    'attention': ('aside', 'visit_aside', 'depart_aside', True),
    'attribution': ('cite', None, None),
    'author': (None, None, None),
    'authors': (None, None, None),
    'block_quote': ('blockquote', dv, dp),
    'bullet_list': ('ul', dv, dp, False),
    'caption': ('figcaption', dv, dp, False),
    'caution': (None, 'visit_aside', 'depart_aside'),
    'citation': (None, None, None),
    'citation_reference': (None, None, None),
    'classifier': (None, 'visit_classifier', None),
    'colspec': ('col', dv, 'depart_colspec'),
    'comment': (None, None, None),
    'compound': ('div', dv, dp, True),
    'contact': (None, None, None),
    'container': ('div', dv, dp, True),
    'copyright': (None, None, None),
    'danger': (None, 'visit_aside', 'depart_aside'),
    'date': (None, None, None),
    'decoration': (None, 'skip_departure', None),
    'definition': ('dd', dv, dp),
    'definition_list': ('dl', dv, dp),
    'definition_list_item': (None, pass_, pass_),
    'description': (None, None, None),
    'docinfo': (None, None, None),
    'doctest_block': (None, None, None),
    'document': (None, 'visit_document', pass_),
    'emphasis': ('em', dv, dp, False, False),
    'entry': (None, dv, 'depart_entry'),
    'enumerated_list': ('ol', dv, 'depart_enumerated_list'),
    'error': (None, 'visit_aside', 'depart_aside'),
    'field': (None, None, None),
    'field_body': (None, None, None),
    'field_list': (None, None, None),
    'field_name': (None, None, None),
    'figure': (None, dv, dp),
    'footer': (None, dv, dp),
    'footnote': (None, None, None),
    'footnote_reference': (None, None, None),
    'generated': (None, None, None),
    'header': (None, dv, dp),
    'hint': (None, 'visit_aside', 'depart_aside'),
    'image': ('img', dv, dp),
    'important': (None, 'visit_aside', 'depart_aside'),
    'inline': ('span', dv, dp, False, False),
    'label': (None, None, None),
    'legend': (None, None, None),
    'line': (None, None, None),
    'line_block': (None, None, None),
    'list_item': ('li', dv, dp, False),
    'literal': ('tt', dv, dp, False, False),
    'literal_block': ('pre', 'visit_literal_block', 'depart_literal_block'),
    'math': (None, 'visit_math_block', None),
    'math_block': (None, 'visit_math_block', None),
    'note': ('aside', 'visit_aside', 'depart_aside', True),
    'option': (None, None, None),
    'option_argument': (None, None, None),
    'option_group': (None, None, None),
    'option_list': (None, None, None),
    'option_list_item': (None, None, None),
    'option_string': (None, None, None),
    'organization': (None, None, None),
    'paragraph': ('p', 'visit_paragraph', dp),
    'pending': (None, None, None),
    'problematic': (None, None, None),
    'raw': (None, 'visit_raw', None),
    'reference': ('a', dv, 'depart_reference', False, False),
    'revision': (None, None, None),
    'row': ('tr', 'visit_row', 'depart_row'),
    'rubric': ('p', dv, 'depart_rubric', True),
    'section': ('section', 'visit_section', 'depart_section'),
    'sidebar': ('aside', 'visit_aside', 'depart_aside', True),
    'status': (None, None, None),
    'strong': (None, dv, dp, False, False),
    'subscript': ('sub', dv, dp, False, False),
    'substitution_definition': (None, 'skip_node', None),
    'substitution_reference': (None, 'skip_node', None),
    'subtitle': (None, dv, 'depart_subtitle'),
    'superscript': ('sup', dv, dp, False, False),
    'system_message': (None, dv, dp),
    'table': (None, 'visit_table', 'depart_table'),
    'target': (None, pass_, 'depart_target'),
    'tbody': (None, dv, dp),
    'term': ('dt', dv, dp),
    'tgroup': (None, pass_, pass_),
    'thead': (None, 'visit_thead', 'depart_thead'),
    'tip': ('aside', 'visit_aside', 'depart_aside'),
    'title': (None, dv, 'depart_title'),
    'title_reference': ('cite', dv, dp, False, False),
    'topic': ('aside', 'visit_aside', 'depart_aside', True),
    'transition': ('hr', dv, dp),
    'version': (None, None, None),
    'warning': ('aside', 'visit_aside', 'depart_aside'),
}


class HTML5Translator(nodes.NodeVisitor):

    def __init__(self, document):
        nodes.NodeVisitor.__init__(self, document)
        self.heading_level = 0
        self.show_ids = document.settings.show_ids
        self.context = ElemStack(document.settings)
        self.head = []
        self.head.append(tag.meta(charset=self.document.settings.output_encoding))
        return

    @property
    def output(self):
        output = '<!DOCTYPE html>\n<html{language}>\n<head>{head}</head>\n' \
                 '<body>{body}</body>\n</html>'
        if self.document.settings.indent_output:
            indent = '\n' + ' ' * self.document.settings.tab_width
            result = []
            for f in self.head:
                result.append(Fragment()(indent, f))
            result.append('\n')
            self.head = result

        language = ' lang="%s"' % self.document.settings.language_code
        self.head = ''.join(XHTMLSerializer()(Fragment()(*self.head)))
        self.body = ''.join(XHTMLSerializer()(Fragment()(*self.context.stack)))
        return output.format(language=language, head=self.head, body=self.body)

    def set_next_elem_attr(self, name, value):
        '''
        The given attribute will be inserted into the attributes of the next element.
        '''
        self.next_elem_attr = {name: value}

    def parse(self, node):
        node_class_name = node.__class__.__name__
        spec = rst_terms[node_class_name]
        name = spec[0] or node_class_name
        use_name_in_class = len(spec) > 3 and spec[3]
        indent = spec[4] if len(spec) > 4 else True
        if use_name_in_class:
            node['classes'].insert(0, node_class_name)

        attrs = {}
        replacements = {'refuri': 'href', 'uri': 'src', 'refid': 'href',
            'morerows': 'rowspan', 'morecols': 'colspan', 'classes': 'class', }
        for k, v in node.attributes.items():
            if not v:
                continue
            elif isinstance(v, list):
                v = ' '.join(v)

            if k in ('names', 'dupnames', 'bullet', 'enumtype', 'colwidth', 'stub'):
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
        return name, indent, attrs

    def default_visit(self, node):
        '''
        Each level creates its own stack
        '''
        self.context.begin_elem()
        return

    def default_departure(self, node):
        name, indent, attr = self.parse(node)
        elem = getattr(tag, name)(**attr)
        self.context.commit_elem(elem, indent)
        return

    def _compacted_paragraph(self, node):
        """
        Determine if the <p> tags around paragraph ``node`` can be omitted.
        Based on from docutils.writers.html4css1.HTMLTranslator.should_be_compact_paragraph
        """
        if (isinstance(node.parent, (nodes.document, nodes.compound, nodes.block_quote)) or
           node['classes'] or 'paragraph' != node.__class__.__name__):
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
        self.default_visit(node)

    def visit_Text(self, node):
        text = node.astext()
        if not getattr(self, 'preserve_space', None):
            text = re.sub(r'\s+', ' ', text)
        self.context.append(text, indent=False)
        raise nodes.SkipDeparture

    def visit_section(self, node):
        self.heading_level += 1
        self.default_visit(node)

    def depart_section(self, node):
        self.heading_level -= 1
        self.default_departure(node)

    def depart_title(self, node):
        assert self.heading_level >= 0
        if self.heading_level == 0:
            self.heading_level = 1
        spec, indent, attr = self.parse(node)
        if 'href' in attr:
            '''
            backref to toc entry
            '''
            anchor = tag.a(href=("#" + attr['href']), class_="toc-backref")
            self.context.commit_elem(anchor)
            anchor = self.context.pop()
            self.context.begin_elem()
            self.context.append(anchor, indent=False)
            del attr['href']
        elem = getattr(tag, 'h' + unicode(self.heading_level))(**attr)
        self.context.commit_elem(elem, indent)

    def depart_subtitle(self, node):
        '''
        The subtitle and its predecessor title should be combined
        into a hgroup
        '''
        # mount the subtitle heading
        subheading_level = getattr(tag, 'h' + unicode(self.heading_level + 1))
        self.context.commit_elem(subheading_level)
        # create hgroup
        pop = self.context.pop_elements(2)
        self.context.begin_elem()
        self.context.append(pop[0])
        self.context.append(pop[1])
        self.context.commit_elem(tag.hgroup)
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
        self.default_departure(node)

    def skip_node(self, node):
        """Internal only"""
        raise nodes.SkipNode

    def skip_departure(self, node):
        raise nodes.SkipDeparture

    def visit_classifier(self, node):
        '''
        Classifier should remain beside the previous element
        '''
        term = self.context.pop()
        term(' ', tag.span(':', class_='classifier-delimiter'), ' ',
                           tag.span(node.astext(), class_='classifier'))
        self.context.append(term)
        raise nodes.SkipNode

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

        waste, indent, attr = self.parse(node)
        self.context.commit_elem(getattr(tag, name)(**attr))

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
            self.context.begin_elem()
            anchor = tag.a(id = node['refid'])
            self.context.commit_elem(anchor)
        elif 'ids' in node:
            '''
            Previous anchor elements should be removed.
            See test case: propagated_target
            '''
            num_anchors = len(node['ids']) - 1
            if num_anchors > 0:
                self.context.pop_elements(num_anchors)
        return

    def visit_literal_block(self, node):
        self.preserve_space = True
        self.default_visit(node)
        return

    def depart_literal_block(self, node):
        del self.preserve_space
        self.default_departure(node)
        return

    def visit_math_block(self, node):
        '''
        Only MathJax support
        '''
        math_code = node.astext()
        math_env = pick_math_environment(math_code)
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

    def visit_document(self, node):
        if 'title' in node:
            self.head.append(tag.title(node['title']))
        self.default_visit(node)

    def visit_raw(self, node):
        if 'html' in node.get('format', '').split():
            self.context.append(Markup(node.astext()), indent=False)
        raise nodes.SkipNode

    def visit_aside(self, node):
        self.save_heading_level = self.heading_level
        self.heading_level = 1
        self.default_visit(node)

    def depart_aside(self, node):
        self.heading_level = self.save_heading_level
        del self.save_heading_level
        if node['classes'] and node['classes'][0].startswith('admonition-'):
            del node['classes'][0]
        self.default_departure(node)

    def depart_rubric(self, node):
        node['classes'] = []
        self.default_departure(node)

'''
Map terms to visit and departure functions
'''
for term, spec in rst_terms.items():
    visit_func = spec[1] and getattr(HTML5Translator, spec[1], nodes._nop)
    depart_func = spec[2] and getattr(HTML5Translator, spec[2], nodes._nop)
    if visit_func:
        setattr(HTML5Translator, 'visit_' + term, visit_func)
    if depart_func:
        setattr(HTML5Translator, 'depart_' + term, depart_func)