#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

__version__ = '0.1'

import os
import docutils
from docutils import nodes, writers, frontend
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
        ("Don't show id in sections", ['--no-id'],
            {'default': 1, 'action': 'store_false', 'dest': 'show_id'})
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


HTMLEquivalency = {
    "abbreviation": "abbr",
    "acronym": "acronym",
    "attribution": "cite",
    "block_quote": "blockquote",
    "bullet_list": "ul",
    "caption": "figcaption",
    "definition": "dd",
    "definition_list": "dl",
    "description": "td",
    "emphasis": "em",
    "entry": "td",
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
        self.indent_width = document.settings.tab_width
        self.show_id = document.settings.show_id
        self.indent_output = document.settings.indent_output
        self.heading_level = 0
        self.indent_level = 0
        self.context = []
        return

    @property
    def output(self):
        output = '<!DOCTYPE html>\n<html>\n<head>{head}</head>\n' \
                 '<body>{body}</body>\n</html>'
        self.head = ''
        self.body = ''.join(XHTMLSerializer()(Fragment()(*self.context)))
        return output.format(head=self.head, body=self.body)

    def default_visit(self, node):
        '''
        Each level creates its own stack
        '''
        self.context.append([])
        self.indent_level += 1
        return

    def default_departure(self, node):
        name = node.__class__.__name__
        if name in HTMLEquivalency:
            name = HTMLEquivalency[name]
        self._new_elem(name, node.attributes)
        return

    def _adjust_attributes(self, attributes):
        attrs = {}
        for k, v in attributes.items():
            if not v:
                continue
            elif isinstance(v, list):
                v = ''.join(v)

            if k in ('names', 'dupnames', 'bullet'):
                continue
            elif k == 'ids':
                if not self.show_id:
                    continue
                k = 'id'
            elif k == 'refuri':
                k = 'href'
            elif k == 'refi':
                k = 'href'
                v = '#' + v
            elif k == 'uri':
                k = 'src'

            attrs[k] = v

        return attrs

    def _new_elem(self, name, attributes = None):
        '''
        A new element is create by removing its stack to make a tag.
        This tag is pushed back into its parent's stack.
        '''
        attr = self._adjust_attributes(attributes) if attributes else dict()
        pop = self.context.pop()
        elem = getattr(tag, name)(*pop, **attr)
        parent_stack = self.context[-1]
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
        if self.indent_output:
            indent = '\n' + self.indent_width * self.indent_level * ' '
            parent_stack.append(indent)
        parent_stack.append(elem)
        if self.indent_output:
            indent = '\n' + self.indent_width * (self.indent_level - 1) * ' '
            parent_stack.append(indent)
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

    def _group_fragments(self, num_fragments, group_name, group_attributes=None):
        parent_stack = self.context[-1]
        fragments = parent_stack[num_fragments:]
        self.context[-1] = parent_stack[:num_fragments]
        self.context.append(fragments)
        self._new_elem(group_name, group_attributes)

    def _append_fragments_to_previous_element(self, *args):
        distance = -2 if self.indent_output else -1
        parent_stack = self.context[-1]
        elem = parent_stack[distance]
        elem(*args)

    def _depart_test(self, node):
        import pdb
        pdb.set_trace()
        self.default_departure(node)
        return

    def visit_paragraph(self, node):
        if self._compacted_paragraph(node):
            raise nodes.SkipDeparture
        else:
            self.default_visit(node)

    def visit_Text(self, node):
        '''
        Text is a leaf node and has no element stack
        '''
        pass

    def depart_Text(self, node):
        text = node.astext().replace('\n', ' ')
        self.context[-1].append(text)

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
        self._new_elem('h' + unicode(self.heading_level), node.attributes)

    def depart_subtitle(self, node):
        '''
        The subtitle and its predecessor title should be combined
        into a hgroup
        '''
        # mount the subtitle heading
        subheading_level = 'h' + unicode(self.heading_level + 1)
        self._new_elem(subheading_level)
        # create hgroup
        num_fragments = -6 if self.indent_output else -2
        self._group_fragments(num_fragments, 'hgroup')
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
        attrs = node.attributes.copy()
        if 'enumtype' in node:
            del attrs['enumtype']
            enumtypes = {
                'arabic': '1',
                'loweralpha': 'a',
                'upperalpha': 'A',
                'lowerroman': 'i',
                'upperroman': 'I'
            }
            attrs['type'] = enumtypes.get(node['enumtype'], '1')
        if attrs.get('suffix') == '.' and 'preffix' not in attrs:
            # default suffix doesn't need special treatment
            del attrs['suffix']
        self._new_elem('ol', attrs)


    def visit_substitution_definition(self, node):
        """Internal only"""
        raise nodes.SkipNode

    def depart_document(self, node):
        pass

    def visit_definition_list_item(self, node):
        pass

    def depart_definition_list_item(self, node):
        pass

    def depart_classifier(self, node):
        self.context.pop()
        self._append_fragments_to_previous_element(
            ' ',
            tag.span(':', class_='classifier-delimiter'),
            ' ',
            tag.span(node.astext(), class_='classifier')
        )
        self.indent_level -= 1

