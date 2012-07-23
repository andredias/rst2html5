#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'

import os
import docutils
from docutils import nodes, writers
from genshi.builder import tag
from genshi.output import XHTMLSerializer

class HTML5Writer(writers.Writer):

    supported = ('html5', 'html5css3')

    def __init__(self):
        writers.Writer.__init__(self)
        self.translator_class = HTML5Translator
        return

    def translate(self):
        visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.output
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

    indent_width = 4

    def __init__(self, document):
        nodes.GenericNodeVisitor.__init__(self, document)
        self.section_level = 0
        self.indent_level = 0
        self.indent_output = True
        self.context = []
        self.show_id = True
        self.head = tag.head
        self.body = tag.body
        return

    @property
    def output(self):
        output = '<!DOCTYPE html>\n<html>\n{head}\n{body}\n</html>'
        head = ''.join(XHTMLSerializer()(self.head))
        body = ''.join(XHTMLSerializer()(self.body))
        return output.format(head=head, body=body)

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
            elif k == 'ids' and self.show_id:
                attrs['id'] = v
            elif k == 'refuri':
                attrs['href'] = v
            elif k == 'refi':
                attrs['href'] = '#' + v
            elif k == 'uri':
                attrs['src'] = v
            else:
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
        self.section_level += 1

    def depart_section(self, node):
        self.section_level -= 1
        self.default_departure(node)

    def depart_title(self, node):
        self._new_elem('h' + unicode(self.section_level), node.attributes)

    def visit_substitution_definition(self, node):
        """Internal only"""
        raise nodes.SkipNode

    def depart_document(self, node):
        self.body(*self.context, **self._adjust_attributes(node.attributes))

