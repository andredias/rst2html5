#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2html5 in the form:
# case = {'rst': rst_text, 'out': expected_output, ...}

from __future__ import unicode_literals

title = {
    'rst': 'Title\n=====',
    'out':   '<h1>Title</h1>'
}


title_accented_chars = {
    'rst': 'Título com Acentuação\n' \
           '=====================',
    'out': '<h1>Título com Acentuação</h1>'
}

title_2 = {
        'rst': '''
Level 1
=======

some text

Level 1 Again
=============''',
        'out': '<section><h1>Level 1</h1><p>some text</p></section>' \
               '<section><h1>Level 1 Again</h1></section>'
}


title_3 = {
        'rst': '''
=======
Level 1
=======

some text

Level 2
=======

more text

Level 3
--------''',
        'out': '<h1>Level 1</h1><p>some text</p>' \
               '<section><h2>Level 2</h2><p>more text</p>' \
               '<section><h3>Level 3</h3></section></section>'
}


subtitle = {
        'rst': '''
================
 Document Title
================
----------
 Subtitle
----------

Section Title
=============

...''',
        'out': '<hgroup><h1>Document Title</h1><h2>Subtitle</h2></hgroup>' \
               '<section><h1>Section Title</h1><p>...</p></section>'
}


'''
The subtitle processing should deal with indentation
'''
subtitle_2 = {
        'rst': '''
================
 Document Title
================
----------
 Subtitle
----------

Section Title
=============

...''',
        'out':   '''
<hgroup>
    <h1>Document Title</h1>
    <h2>Subtitle</h2>
</hgroup>
<section>
    <h1>Section Title</h1>
    <p>...</p>
</section>
''',
        'indent_output': True
}


paragraph = {
        'rst': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n' \
                'Vestibulum dignissim lacinia blandit. Suspendisse potenti.',
        'out': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
               'Vestibulum dignissim lacinia blandit. Suspendisse potenti.</p>'
}


accented_paragraph = {
        'rst': 'Não há ninguém que ame a dor por si só, que a busque e ' \
              'queira tê-la, simplesmente por ser dor...',
        'out': '<p>Não há ninguém que ame a dor por si só, que a busque e ' \
               'queira tê-la, simplesmente por ser dor...</p>'
}


quoted_paragraph = {
        'rst': '''This is a paragraph.  It's quite
short.

   This paragraph will result in an indented block of
   text, typically used for quoting other text.

This is another one.''',
        'out': "<p>This is a paragraph.  It's quite short.</p>" \
               "<blockquote>This paragraph will result in an indented " \
               "block of text, typically used for quoting other text." \
               "</blockquote><p>This is another one.</p>"
}


image = {
        'rst': '''.. image:: images/biohazard.png
   :width: 200
   :height: 100
   :scale: 50
   :alt: alternate text''',
        'out': '<img src="images/biohazard.png" alt="alternate text" ' \
               'scale="50" width="200" height="100" />'
}


inline_markup_1 = {
        'rst': '''*emphasis*
**strong emphasis**
`interpreted text`
`interpreted text with role`:emphasis:
``inline literal text``
''',
        'out': '<p><em>emphasis</em> <strong>strong emphasis</strong> ' \
               '<cite>interpreted text</cite> <em>interpreted text with ' \
               'role</em> <tt>inline literal text</tt></p>'
}


bullet_list = {
        'rst': '* item 1\n* item 2\n  more text',
        'out': '<ul><li>item 1</li><li>item 2 more text</li></ul>'
}

ordered_list_decimal = {
    'rst': '#. item 1\n#. item 2',
    'out': '<ol type="1"><li>item 1</li><li>item 2</li></ol>'
}

ordered_list_decimal_autonumerated = {
    'rst': '3. item 3\n#. item 4',
    'out': '<ol start="3" type="1"><li>item 3</li><li>item 4</li></ol>'
}

ordered_list_lower_alpha = {
    'rst': '(a) item 1\n(#) item 2\n(#) item 3',
    'out': '<ol prefix="(" type="a" suffix=")"><li>item 1</li><li>item 2</li>' \
           '<li>item 3</li></ol>'
}

ordered_list_upper_alpha = {
    'rst': 'A) item 1\n#) item 2\n#) item 3',
    'out': '<ol type="A" suffix=")"><li>item 1</li><li>item 2</li><li>item 3'\
           '</li></ol>'
}

ordered_list_lower_roman = {
    'rst': 'i. item 1\n#. item 2\n#. item 3',
    'out': '<ol type="i"><li>item 1</li><li>item 2</li><li>item 3</li></ol>'
}

ordered_list_upper_roman = {
    'rst': 'I. item 1\n#. item 2\n#. item 3',
    'out': '<ol type="I"><li>item 1</li><li>item 2</li><li>item 3</li></ol>'
}

definition_list = {
    'rst': '''term 1
    Definition 1.

term 2
    Definition 2, paragraph 1.

    Definition 2, paragraph 2.

term 3 : classifier
    Definition 3.

term 4 : classifier one : classifier two
    Definition 4.''',
    'out': '''
    <dl>
        <dt>term 1</dt>
        <dd>Definition 1.</dd>
        <dt>term 2</dt>
        <dd>
            <p>Definition 2, paragraph 1.</p>
            <p>Definition 2, paragraph 2.</p>
        </dd>
        <dt>term 3 <span class="classifier-delimiter">:</span> \
<span class="classifier">\
classifier</span></dt>
        <dd>Definition 3.</dd>
        <dt>term 4 <span class="classifier-delimiter">:</span> <span \
class="classifier">classifier one</span> <span class="classifier-delimiter">\
:</span> <span class="classifier">\
classifier two</span></dt>
        <dd>Definition 4.</dd>
    </dl>
''',
    'indent_output': True
}