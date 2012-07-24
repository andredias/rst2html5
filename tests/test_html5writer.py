#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
from html5css3 import HTML5Writer
from docutils.core import publish_parts

def rst_to_html5_body(rst, no_indent=True, no_id=True):
    overrides = {'indent_output': not no_indent, 'show_id': not no_id}
    parts = publish_parts(writer=HTML5Writer(), source=rst,
                          settings_overrides=overrides)
    return parts['body']

class TestHTML5Writer(unittest.TestCase):

    def test_title(self):
        rst = 'Title\n====='
        out = '<h1>Title</h1>'
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_title_accented_chars(self):
        rst = 'Título com Acentuação\n' \
              '====================='
        out = '<h1>Título com Acentuação</h1>'
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_title_2(self):
        rst = '''
Level 1
=======

some text

Level 1 Again
============='''
        out = '<section><h1>Level 1</h1><p>some text</p></section>' \
              '<section><h1>Level 1 Again</h1></section>'
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_title_3(self):
        rst = '''
=======
Level 1
=======

some text

Level 2
=======

more text

Level 3
--------'''
        out = '<h1>Level 1</h1><p>some text</p>' \
              '<section><h2>Level 2</h2><p>more text</p>' \
              '<section><h3>Level 3</h3></section></section>'
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_paragraph(self):
        rst = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
              'Vestibulum dignissim lacinia blandit. Suspendisse potenti.'
        out = '<p>%s</p>' % rst
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_accented_paragraph(self):
        rst = 'Não há ninguém que ame a dor por si só, que a busque e ' \
              'queira tê-la, simplesmente por ser dor...'
        out = '<p>%s</p>' % rst
        self.assertEqual(rst_to_html5_body(rst), out)
