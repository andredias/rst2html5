#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
from html5css3 import HTML5Writer
from docutils.core import publish_parts

def rst_to_html5_body(rst, indent_output=False, show_id=False):
    overrides = {'indent_output': indent_output, 'show_id': show_id}
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

    def test_subtitle(self):
        rst = '''
================
 Document Title
================
----------
 Subtitle
----------

Section Title
=============

...'''
        out = '<hgroup><h1>Document Title</h1><h2>Subtitle</h2></hgroup>' \
              '<section><h1>Section Title</h1><p>...</p></section>'
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_subtitle_2(self):
        '''
        The subtitle processing should deal with indentation
        '''
        rst = '''
================
 Document Title
================
----------
 Subtitle
----------

Section Title
=============

...'''
        out = '''
<hgroup>
    <h1>Document Title</h1>
    <h2>Subtitle</h2>
</hgroup>
<section>
    <h1>Section Title</h1>
    <p>...</p>
</section>
'''
        self.assertEqual(rst_to_html5_body(rst, indent_output=True), out)

    def test_paragraph(self):
        rst = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n' \
              'Vestibulum dignissim lacinia blandit. Suspendisse potenti.'
        out = '<p>%s</p>' % rst.replace('\n', ' ')
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_accented_paragraph(self):
        rst = 'Não há ninguém que ame a dor por si só, que a busque e ' \
              'queira tê-la, simplesmente por ser dor...'
        out = '<p>%s</p>' % rst
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_quoted_paragraph(self):
        rst = '''This is a paragraph.  It's quite
short.

   This paragraph will result in an indented block of
   text, typically used for quoting other text.

This is another one.'''
        out = "<p>This is a paragraph.  It's quite short.</p>" \
              "<blockquote><p>This paragraph will result in an indented " \
              "block of text, typically used for quoting other text.</p>" \
              "</blockquote><p>This is another one.</p>"
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_image(self):
        rst = '''.. image:: images/biohazard.png
   :width: 200
   :height: 100
   :scale: 50
   :alt: alternate text'''
        out = '<img src="images/biohazard.png" alt="alternate text" ' \
              'scale="50" width="200" height="100" />'
        self.assertEqual(rst_to_html5_body(rst), out)

    def test_inline_markup_1(self):
        rst = '''*emphasis*
**strong emphasis**
`interpreted text`
`interpreted text with role`:emphasis:
``inline literal text``
'''
        out = '<p><em>emphasis</em> <strong>strong emphasis</strong> ' \
              '<cite>interpreted text</cite> <em>interpreted text with ' \
              'role</em> <tt>inline literal text</tt></p>'
        self.assertEqual(rst_to_html5_body(rst), out)

    @unittest.SkipTest
    def test_inline_markup_2(self):
        rst = '''standalone hyperlink, http://docutils.sourceforge.net
named reference, reStructuredText_
`anonymous reference`__
footnote reference, [1]_
citation reference, [CIT2002]_
|substitution|
_`inline internal target`.

.. _inline internal target:

.. _reStructuredText:
__ http://www.pronus.eng.br
.. [#] footnote reference
.. [CIT2002] Citation
.. |substitution| replace:: substituted'''
        out = ''
        self.assertEqual(rst_to_html5_body(rst), out)

    @unittest.SkipTest
    def test_grid_table(self):
        rst = '''
+--------------------------------+-----------------------------------+
| Paragraphs are flush-left,     | Literal block, preceded by "::":: |
| separated by blank lines.      |                                   |
|                                |     Indented                      |
|     Block quotes are indented. |                                   |
+--------------------------------+ or::                              |
| >>> print 'Doctest block'      |                                   |
| Doctest block                  | > Quoted                          |
+--------------------------------+-----------------------------------+
| | Line blocks preserve line breaks & indents. [new in 0.3.6]       |
| |     Useful for addresses, verse, and adornment-free lists; long  |
|       lines can be wrapped with continuation lines.                |
+--------------------------------------------------------------------+'''
        out = ''
        self.assertEqual(rst_to_html5_body(rst), out)

    @unittest.SkipTest
    def test_simple_table(self):
        rst = '''
================  ============================================================
List Type         Examples
================  ============================================================
Bullet list       * items begin with "-", "+", or "*"
Enumerated list   1. items use any variation of "1.", "A)", and "(i)"
                  #. also auto-enumerated
Definition list   Term is flush-left : optional classifier
                      Definition is indented, no blank line between
Field list        :field name: field body
Option list       -o  at least 2 spaces between option & description
================  ============================================================
'''
        out = ''
        self.assertEqual(rst_to_html5_body(rst), out)
