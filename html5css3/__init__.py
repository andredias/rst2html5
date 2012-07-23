#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'

import os
import docutils
from docutils import nodes, writers
from genshi.builder import tag

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
    "image": "img",
    "list_item": "li",
    "literal_block": "pre",
    "option": "span",
    "option_list": "table",
    "option_list_item": "tr",
    "option_string": "span",
    "paragraph": "p",
    "row": "tr",
    "sidebar": "aside",
    "term": "dt",
    "transition": "hr",
  }

class HTML5Translator(nodes.GenericNodeVisitor):

    def __init__(self, document):
        nodes.GenericNodeVisitor.__init__(self, document)
        self.section_level = 0
        self.context = []
        self.head = tag.head
        self.body = tag.body
        return

    @property
    def output(self):
        output = '<!DOCTYPE html>\n<html>\n{head}\n{body}\n</html>'
        return output.format(head=self.head, body=self.body)

    def default_visit(self, node):
        '''
        Each level creates its own stack
        '''
        self.context.append([])

    def _new_elem(self, name, attributes):
        '''
        A new element is create by removing its stack to make a tag.
        This tag is pushed back into its parent's stack.
        '''
        pop = self.context.pop()
        elem = tag.__getattr__(name)(*pop, **attributes)
        parent_stack = self.context[-1]
        parent_stack.append(elem)
        parent_stack.append('\n')
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

    def depart_document(self, node):
        self.body(*self.context, **node.attributes)
