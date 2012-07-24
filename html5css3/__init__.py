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
        self.head = tag.head
        self.body = tag.body
        return

    @property
    def output(self):
        output = '<!DOCTYPE html>\n<html>\n<head>{head}</head>\n' \
                 '<body>{body}</body>\n</html>'
        self.head = ''.join(XHTMLSerializer()(self.head))
        self.body = ''.join(XHTMLSerializer()(Fragment()(*self.context)))
        return output.format(head=self.head, body=self.body)

    def default_visit(self, node):
        '''
        Each level creates its own stack
        '''
        self.context.append([])
        self.indent_level += 1
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

    def _new_elem(self, name, attributes):
        '''
        A new element is create by removing its stack to make a tag.
        This tag is pushed back into its parent's stack.
        '''
        attr = self._adjust_attributes(attributes)
        pop = self.context.pop()
        elem = tag.__getattr__(name)(*pop, **attr)
        parent_stack = self.context[-1]
        self.indent_level -= 1
        if self.indent_output:
            indent = '\n' + self.indent_width * self.indent_level * ' '
            parent_stack.append(indent)
        parent_stack.append(elem)
        if self.indent_output:
            indent = '\n' + self.indent_width * (self.indent_level - 1) * ' '
            parent_stack.append(indent)
        return

    def default_departure(self, node):
        name = node.__class__.__name__
        if name in HTMLEquivalency:
            name = HTMLEquivalency[name]
        self._new_elem(name, node.attributes)
        return

    def visit_Text(self, node):
        '''
        Text is a leaf node and has no element stack
        '''
        pass

    def depart_Text(self, node):
        self.context[-1].append(node.astext())

    def visit_section(self, node):
        self.default_visit(node)
        self.heading_level += 1

    def depart_section(self, node):
        self.heading_level -= 1
        self.default_departure(node)

    def depart_title(self, node):
        if self.heading_level == 0:
            self.heading_level = 1
        self._new_elem('h' + unicode(self.heading_level), node.attributes)

    def visit_substitution_definition(self, node):
        """Internal only"""
        raise nodes.SkipNode

    def depart_document(self, node):
        pass
