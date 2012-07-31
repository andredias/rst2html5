#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2html5 in the form:
# case = {'rst': rst_text, 'out': expected_output, ...}

from __future__ import unicode_literals

indentation = {
    'rst': 'Paragraph',
    'out': '\n    <p>Paragraph</p>\n',
    'indent_output': True
}

title = {
    'rst': 'Title\n=====',
    'out': '<h1>Title</h1>'
}


title_accented_chars = {
    'rst': 'Título com Acentuação\n'
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
    'out': '<section id="level-1"><h1>Level 1</h1><p>some text</p></section>'
            '<section id="level-1-again"><h1>Level 1 Again</h1></section>',
    'show_ids': True
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
    'out': '<h1>Level 1</h1><p>some text</p>'
            '<section><h2>Level 2</h2><p>more text</p>'
            '<section><h3>Level 3</h3></section></section>',
    'show_ids': False
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
        'out': '<hgroup><h1>Document Title</h1><h2>Subtitle</h2></hgroup>'
               '<section><h1>Section Title</h1><p>...</p></section>',
        'show_ids': False
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
        'out': '''
    <hgroup>
        <h1>Document Title</h1>
        <h2>Subtitle</h2>
    </hgroup>
    <section>
        <h1>Section Title</h1>
        <p>...</p>
    </section>
''',
        'indent_output': True,
        'show_ids': False
}


paragraph = {
        'rst': 'Lorem    ipsum dolor sit amet,        consectetur '
               'adipiscing          elit.\n'
                'Vestibulum    dignissim lacinia blandit. Suspendisse potenti.',
        'out': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
               'Vestibulum dignissim lacinia blandit. Suspendisse potenti.</p>'
}


accented_paragraph = {
        'rst': 'Não há ninguém que ame a dor por si só, que a busque e '
              'queira tê-la, simplesmente por ser dor...',
        'out': '<p>Não há ninguém que ame a dor por si só, que a busque e '
               'queira tê-la, simplesmente por ser dor...</p>'
}


quoted_paragraph = {
        'rst': '''This is a paragraph.  It's   quite
short.

   This paragraph will result in an indented block of
   text, typically used for quoting other text.

This is another one.''',
        'out': "<p>This is a paragraph. It's quite short.</p>"
               "<blockquote><p>This paragraph will result in an indented "
               "block of text, typically used for quoting other text."
               "</p></blockquote><p>This is another one.</p>"
}


image = {
        'rst': '''.. image:: images/biohazard.png
   :width: 200
   :height: 100
   :scale: 50
   :alt: alternate text''',
        'out': '<img src="images/biohazard.png" alt="alternate text" '
               'scale="50" width="200" height="100" />'
}


figure = {
    'rst': '''.. figure:: picture.png
   :scale: 50%
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).''',
    'out': '''
    <figure>
        <img src="picture.png" alt="map to buried treasure" scale="50" />
        <figcaption>This is the caption of the figure (a simple paragraph).</figcaption>
    </figure>
''',
    'indent_output': True
}


inline_markup_1 = {
        'rst': '''*emphasis*
**strong emphasis**
`interpreted text`
`superscript`:sup:
`interpreted text with role`:emphasis:
`subscript`:sub:
``inline literal text``
''',
        'out': '''
    <p><em>emphasis</em> <strong>strong emphasis</strong> <cite>interpreted text</cite> \
<sup>superscript</sup> <em>interpreted text with role</em> <sub>subscript</sub> \
<code>inline literal text</code></p>
''',
        'indent_output': True
}


bullet_list = {
        'rst': '* item 1\n* item 2\n  more text',
        'out': '<ul><li>item 1</li><li>item 2 more text</li></ul>'
}

transition = {
    'rst': '''Paragraph

----------

Paragraph''',
    'out': '<p>Paragraph</p><hr /><p>Paragraph</p>',
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
    'out': '<ol prefix="(" type="a" suffix=")"><li>item 1</li><li>item 2</li>'
           '<li>item 3</li></ol>'
}

ordered_list_upper_alpha = {
    'rst': 'A) item 1\n#) item 2\n#) item 3',
    'out': '<ol type="A" suffix=")"><li>item 1</li><li>item 2</li><li>item 3'
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

grid_table = {
    'rst': '''+--------------+----------+
| row 1, col 1 | column 2 |
+--------------+----------+
| row 2        |          |
+--------------+----------+''',
    'out': '''
    <table>
        <col />
        <col />
        <tbody>
            <tr>
                <td>row 1, col 1</td>
                <td>column 2</td>
            </tr>
            <tr>
                <td>row 2</td>
                <td></td>
            </tr>
        </tbody>
    </table>
''',
    'indent_output': True
}

grid_table_with_head = {
    'rst': '''+--------------+----------+
| row 1, col 1 | column 2 |
+==============+==========+
| row 2        |          |
+--------------+----------+''',
    'out': '''
    <table>
        <col />
        <col />
        <thead>
            <tr>
                <th>row 1, col 1</th>
                <th>column 2</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>row 2</td>
                <td></td>
            </tr>
        </tbody>
    </table>
''',
    'indent_output': True
}

csv_table = {
    'rst': '''.. csv-table::
    :header: "Command", "Subversion", "Mercurial", "Git"
    :stub-columns: 2

    add, 30, 23, 333
''',
    'out': '''
    <table>
        <col />
        <col />
        <col />
        <col />
        <thead>
            <tr>
                <th>Command</th>
                <th>Subversion</th>
                <th>Mercurial</th>
                <th>Git</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>add</th>
                <th>30</th>
                <td>23</td>
                <td>333</td>
            </tr>
        </tbody>
    </table>
''',
    'indent_output': True
}

grid_table_span = {
    'rst': '''+------------------------+------------+---------------------+
| body row 1             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 2             |            | - body elements.    |
+------------------------+------------+---------------------+
| body row 3             |       col span cell              |
+------------------------+------------+---------------------+''',
    'out': '''
    <table>
        <col />
        <col />
        <col />
        <tbody>
            <tr>
                <td>body row 1</td>
                <td rowspan="2">Cells may span rows.</td>
                <td rowspan="2">
                    <ul>
                        <li>Table cells</li>
                        <li>contain</li>
                        <li>body elements.</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <td>body row 2</td>
            </tr>
            <tr>
                <td>body row 3</td>
                <td colspan="2">col span cell</td>
            </tr>
        </tbody>
    </table>
''',
    'indent_output': True
}


external_link = {
    'rst': '''This is a paragraph that contains `a link`_.

.. _a link: http://example.com/''',
    'out': '<p>This is a paragraph that contains <a href="http://example.com/">a link</a>.</p>'
}

# see: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#hyperlink-targets

internal_link = {
    'rst': '''Clicking on this internal hyperlink will take us to the target_
below.

.. _target:

The hyperlink target above points to this paragraph.''',
    'out': '''
    <p>Clicking on this internal hyperlink will take us to the \
<a href="#target">target</a> below.</p>
    <a id="target"></a>
    <p>The hyperlink target above points to this paragraph.</p>
''',
    'indent_output': True
}

chained_internal_links = {
    'rst': '''Links to target1_ and target2_.

.. _target1:
.. _target2:

The targets "target1" and "target2" are synonyms; they both
point to this paragraph.''',
    'out': '''
    <p>Links to <a href="#target1">target1</a> and <a href="#target2">target2</a>.</p>
    <a id="target1"></a>
    <a id="target2"></a>
    <p>The targets "target1" and "target2" are synonyms; they both point to this paragraph.</p>
''',
    'indent_output': True
}

propagated_target = {
    'rst': '''Link to archive_.

.. _Python DOC-SIG mailing list archive:
.. _archive:
.. _Doc-SIG: http://mail.python.org/pipermail/doc-sig/''',
    'out': '''
    <p>Link to <a href="http://mail.python.org/pipermail/doc-sig/">archive</a>.</p>
''',
    'indent_output': True
}

indirect_target_links = {
    'rst': '''Link to one_.

.. _one: two_
.. _two: three_
.. _three:

Target paragraph.''',
    'out': '''
    <p>Link to <a href="#three">one</a>.</p>
    <a id="three"></a>
    <p>Target paragraph.</p>
''',
    'indent_output': True
}

preformatted_text = {
    'rst': r'''An example::

    Whitespace, newlines, blank lines, and all kinds of markup
      (like *this* or \this) is preserved by literal blocks.
  Lookie here, I've dropped an indentation level
  (but not far enough)''',
    'out': r'''
    <p>An example:</p>
    <pre>  Whitespace, newlines, blank lines, and all kinds of markup
    (like *this* or \this) is preserved by literal blocks.
Lookie here, I've dropped an indentation level
(but not far enough)</pre>
''',
    'indent_output': True
}

code_block = {
    'rst': """.. code-block:: python

    def extract_variables(module):
        '''
        Extract variables of a test data module.
        Variables should be a dict().
        For example, {'rst': rst, 'out':out, ...}
        '''
        return ((v, getattr(module, v)) for v in dir(module)
            if not v.startswith('__') and isinstance(getattr(module, v), dict))
""",
    'out': """
    <pre class="code python"><span class="k">def</span> <span class="nf">extract_variables</span>\
<span class="p">(</span><span class="n">module</span><span class="p">):</span>
    <span class="sd">'''
    Extract variables of a test data module.
    Variables should be a dict().
    For example, {'rst': rst, 'out':out, ...}
    '''</span>
    <span class="k">return</span> <span class="p">((</span><span class="n">v</span>\
<span class="p">,</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">\
module</span><span class="p">,</span> <span class="n">v</span><span class="p">))</span>\
 <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="nb">\
dir</span><span class="p">(</span><span class="n">module</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">v</span>\
<span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">\
'__'</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">isinstance</span>\
<span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">\
module</span><span class="p">,</span> <span class="n">v</span><span class="p">),\
</span> <span class="nb">dict</span><span class="p">))</span></pre>
""",
    'indent_output': True
}

math = {
    'rst': r'''.. math::

    \dot{x} &amp; = \sigma(y-x) \\
    \dot{y} &amp; = \rho x - y - xz \\
    \dot{z} &amp; = -\beta z + xy''',
    'out': r'''
    <div class="math">\begin{align*}
\dot{x} &amp;amp; = \sigma(y-x) \\
\dot{y} &amp;amp; = \rho x - y - xz \\
\dot{z} &amp;amp; = -\beta z + xy
\end{align*}</div>
''',
    'indent_output': True
}

math_role = {
    'rst': r':math:`\sqrt{3x-1}+(1+x)^2`',
    'out': '<p><span class="math">\(\sqrt{3x-1}+(1+x)^2\)</span></p>'
}

raw = {
    'rst': '''some text

.. raw:: html

    <hr width=50 size=10 />
    <br />

more text''',
    'out': '\n    <p>some text</p>\n<hr width=50 size=10 />\n<br />\n    <p>more text</p>\n',
    'indent_output': True
}

class_directive = {
    'rst': '''.. class:: nav special

paragraph with some text

.. class:: heading top

Section Title
=============''',
    'out': '<p class="nav special">paragraph with some text</p><section class="heading top">'
           '<h1>Section Title</h1></section>',
    'show_ids': False
}

role = {
    'rst': '''.. role:: custom
   :class: special

this is an :custom:`interpreted text`.''',
    'out': '<p>this is an <span class="special">interpreted text</span>.</p>'
}

topic = {
    'rst': '''
Title 1
=======

text

Subtitle
--------

more text

.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

Another Subtitle
----------------''',
    'out': '''
    <h1>Title 1</h1>
    <p>text</p>
    <section>
        <h2>Subtitle</h2>
        <p>more text</p>
        <aside class="topic">
            <h1>Topic Title</h1>
            <p>Subsequent indented lines comprise the body of the topic, and are interpreted as \
body elements.</p>
        </aside>
    </section>
    <section>
        <h2>Another Subtitle</h2>
    </section>
''',
    'indent_output': True,
    'show_ids': False
}

specific_admonition = {
    'rst': '''
Title
=====

text

Subtitle
--------

more text

.. note:: This is a note admonition.

   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.

Another Subtitle
----------------''',
    'out': '''
    <h1>Title</h1>
    <p>text</p>
    <section>
        <h2>Subtitle</h2>
        <p>more text</p>
        <aside class="note">
            <p>This is a note admonition.</p>
            <p>This is the second line of the first paragraph.</p>
            <ul>
                <li>The note contains all indented body elements following.</li>
                <li>It includes this bullet list.</li>
            </ul>
        </aside>
    </section>
    <section>
        <h2>Another Subtitle</h2>
    </section>
''',
    'indent_output': True,
    'show_ids': False
}

generic_admonition = {
    'rst': '''
Title
=====

text

Subtitle
--------

more text

.. class:: special

.. admonition:: This is a note admonition.

   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.

Another Subtitle
----------------''',
    'out': '''
    <h1>Title</h1>
    <p>text</p>
    <section>
        <h2>Subtitle</h2>
        <p>more text</p>
        <aside class="admonition special">
            <h1>This is a note admonition.</h1>
            <p>This is the second line of the first paragraph.</p>
            <ul>
                <li>The note contains all indented body elements following.</li>
                <li>It includes this bullet list.</li>
            </ul>
        </aside>
    </section>
    <section>
        <h2>Another Subtitle</h2>
    </section>
''',
    'indent_output': True,
    'show_ids': False
}

sidebar = {
    'rst': '''
Title
=====

text

Subtitle
--------

more text

.. sidebar:: This is a sidebar
   :subtitle: Sidebar Subtitle

   This is the second line of the first paragraph.

   - The note contains all indented body elements
     following.
   - It includes this bullet list.

Another Subtitle
----------------
''',
    'out': '''
    <h1>Title</h1>
    <p>text</p>
    <section>
        <h2>Subtitle</h2>
        <p>more text</p>
        <aside class="sidebar">
            <hgroup>
                <h1>This is a sidebar</h1>
                <h2>Sidebar Subtitle</h2>
            </hgroup>
            <p>This is the second line of the first paragraph.</p>
            <ul>
                <li>The note contains all indented body elements following.</li>
                <li>It includes this bullet list.</li>
            </ul>
        </aside>
    </section>
    <section>
        <h2>Another Subtitle</h2>
    </section>
''',
    'indent_output': True,
    'show_ids': False
}

rubric = {
    'rst': 'some text\n\n.. rubric:: RuBriC\n    :class: special heading\n\nmore text',
    'out': '<p>some text</p><p class="rubric">RuBriC</p><p>more text</p>',
}

epigraph = {
    'rst': '''.. epigraph::

   No matter where you go, there you are.''',
    'out': '<blockquote class="epigraph"><p>No matter where you go, there you are.</p>'
           '</blockquote>',
}

compound = {
    'rst': '''.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.''',
    'out': '''
    <div class="compound">
        <p>The 'rm' command is very dangerous. If you are logged in as root and enter</p>
        <pre>cd /
rm -rf *</pre>
        <p>you will erase the entire contents of your file system.</p>
    </div>
''',
    'indent_output': True
}

container = {
    'rst': '''.. container:: custom

   This paragraph might be rendered in a custom way.''',
    'out': '<div class="container custom">This paragraph might be rendered in a custom way.</div>',
}

contents = {
    'rst': '''.. contents:: Table of Contents
   :depth: 2

Basic Usage
===========

To start using subrepositories, you need two repositories, a main repo and a nested repo''',
    'out': '''
    <aside class="topic contents" id="table-of-contents">
        <h1>Table of Contents</h1>
        <ul>
            <li><a href="#basic-usage" id="id1">Basic Usage</a></li>
        </ul>
    </aside>
    <section id="basic-usage">
        <h1><a class="toc-backref" href="#id1">Basic Usage</a></h1>
        <p>To start using subrepositories, you need two repositories, a main repo and a nested repo</p>
    </section>
''',
    'indent_output': True,
    'show_ids': True
}

header = {
    'rst': '.. header:: This space for rent.',
    'out': '<header>This space for rent.</header>',
}

footer = {
    'rst': '.. footer:: This space for rent.',
    'out': '<footer>This space for rent.</footer>',
}

replace = {
    'rst': '''.. |reST| replace:: reStructuredText

Yes, |reST| is a long word, so I can't blame anyone for wanting to
abbreviate it.''',
    'out': "<p>Yes, reStructuredText is a long word, so I can't blame anyone for wanting to "
           "abbreviate it.</p>",
}

docinfo = {
    'rst': ''':Version: 1
:Authors: - André
          - Felipe
          - Dias
:Organization: Pronus Engenharia de Software
:Contact: andref.dias@pronus.eng.br
:Address: Av. Ipê Amarelo
   Sumaré - São Paulo - Brasil
   13175-667
:Version: 1
:Status: Alpha
:Date: 2012-07-29
:Copyright: André Felipe Dias
:Dedication: To Andréa, Dexter e DeeDee
:Abstract: Generates (X)HTML5 documents from standalone reStructuredText sources.
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter i: integer''',
    'out': '''
    <table class="docinfo">
        <col />
        <col />
        <tbody>
            <tr>
                <th>version</th>
                <td>1</td>
            </tr>
            <tr>
                <th>authors</th>
                <td>
                    <ul>
                        <li>André</li>
                        <li>Felipe</li>
                        <li>Dias</li>
                    </ul>
                </td>
            </tr>
            <tr>
                <th>organization</th>
                <td>Pronus Engenharia de Software</td>
            </tr>
            <tr>
                <th>contact</th>
                <td><a href="mailto:andref.dias@pronus.eng.br">andref.dias@pronus.eng.br</a></td>
            </tr>
            <tr>
                <th>address</th>
                <td>
                    <pre class="docinfo-address">Av. Ipê Amarelo
Sumaré - São Paulo - Brasil
13175-667</pre>
                </td>
            </tr>
            <tr>
                <th>version</th>
                <td>1</td>
            </tr>
            <tr>
                <th>status</th>
                <td>Alpha</td>
            </tr>
            <tr>
                <th>date</th>
                <td>2012-07-29</td>
            </tr>
            <tr>
                <th>copyright</th>
                <td>André Felipe Dias</td>
            </tr>
            <tr>
                <th>Indentation</th>
                <td>Since the field marker may be quite long, the second and \
subsequent lines of the field body do not have to line up with the first line, \
but they must be indented relative to the field name marker, and they must line \
up with each other.</td>
            </tr>
            <tr>
                <th>Parameter i</th>
                <td>integer</td>
            </tr>
        </tbody>
    </table>
    <aside class="topic dedication">
        <h1>Dedication</h1>
        <p>To Andréa, Dexter e DeeDee</p>
    </aside>
    <aside class="topic abstract">
        <h1>Abstract</h1>
        <p>Generates (X)HTML5 documents from standalone reStructuredText sources.</p>
    </aside>
''',
    'indent_output': True,
}

docinfo2 = {
    'rst': ''':Info: See https://bitbucket.org/andre_felipe_dias/rst2html5
:Author: André Felipe Dias <andref.dias@gmail.com>
:Date: 2012-07-30
:Revision: 38
:Description: This is a "docinfo block", or bibliographic field list''',
    'out': '''
    <table class="docinfo">
        <col />
        <col />
        <tbody>
            <tr>
                <th>Info</th>
                <td>See <a href="https://bitbucket.org/andre_felipe_dias/rst2html5">\
https://bitbucket.org/andre_felipe_dias/rst2html5</a></td>
            </tr>
            <tr>
                <th>author</th>
                <td>André Felipe Dias &lt;<a href="mailto:andref.dias@gmail.com">\
andref.dias@gmail.com</a>&gt;</td>
            </tr>
            <tr>
                <th>date</th>
                <td>2012-07-30</td>
            </tr>
            <tr>
                <th>revision</th>
                <td>38</td>
            </tr>
            <tr>
                <th>Description</th>
                <td>This is a "docinfo block", or bibliographic field list</td>
            </tr>
        </tbody>
    </table>
''',
    'indent_output': True
}

comment = {
    'rst': '''..
    comment <comment> comment
    comment

    more text''',
    'out': ''
}

citation = {
    'rst': '''this is a citation [CIT2012]_

Another [TEST2]_.

.. [CIT2012] A citation
.. [TEST2] Test text''',
    'out': '''
    <p>this is a citation <a href="#cit2012" id="id1" class="citation_reference">[CIT2012]</a></p>
    <p>Another <a href="#test2" id="id2" class="citation_reference">[TEST2]</a>.</p>
    <table class="citation" id="cit2012">
        <col />
        <col />
        <tbody>
            <tr>
                <th>[CIT2012]</th>
                <td>A citation</td>
            </tr>
        </tbody>
    </table>
    <table class="citation" id="test2">
        <col />
        <col />
        <tbody>
            <tr>
                <th>[TEST2]</th>
                <td>Test text</td>
            </tr>
        </tbody>
    </table>
''',
    'indent_output': True
}

attribution = {
    'rst': '''Quote:

    "Choose a job you love, and you will never have to work a day in your life."

    -- Confucius''',
    'out': '''
    <p>Quote:</p>
    <blockquote>
        <p>"Choose a job you love, and you will never have to work a day in your life."</p>
        <p class="attribution">Confucius</p>
    </blockquote>
''',
    'indent_output': True
}

doctest_block = {
    'rst': '''This is an ordinary paragraph.

>>> print 'this is a Doctest block'
this is a Doctest block''',
    'out': '''
    <p>This is an ordinary paragraph.</p>
    <pre class="doctest_block">&gt;&gt;&gt; print 'this is a Doctest block'
this is a Doctest block</pre>
''',
    'indent_output': True
}

option_list = {
    'rst': '''-a         Output all.
-b         Output both (this description is
           quite long).
-c arg     Output just arg.
--long     Output all day long.

-p         This option has two paragraphs in the description.
           This is the first.

           This is the second.  Blank lines may be omitted between
           options (as above) or left in (as here and below).

--very-long-option  A VMS-style option.  Note the adjustment for
                    the required two spaces.

--an-even-longer-option
           The description can also start on the next line.

-2, --two  This option has two variants.

-f FILE, --file=FILE  These two options are synonyms; both have
                      arguments.

/V         A VMS/DOS-style option.''',
    'out': '''
    <table class="option_list">
        <col />
        <col />
        <tbody>
            <tr>
                <td><kbd>-a</kbd></td>
                <td>Output all.</td>
            </tr>
            <tr>
                <td><kbd>-b</kbd></td>
                <td>Output both (this description is quite long).</td>
            </tr>
            <tr>
                <td><kbd>-c <var>arg</var></kbd></td>
                <td>Output just arg.</td>
            </tr>
            <tr>
                <td><kbd>--long</kbd></td>
                <td>Output all day long.</td>
            </tr>
            <tr>
                <td><kbd>-p</kbd></td>
                <td>
                    <p>This option has two paragraphs in the description. This is the first.</p>
                    <p>This is the second. Blank lines may be omitted between options (as above) or left in (as here and below).</p>
                </td>
            </tr>
            <tr>
                <td colspan="2"><kbd>--very-long-option</kbd></td>
            </tr>
            <tr>
                <td></td>
                <td>A VMS-style option. Note the adjustment for the required two spaces.</td>
            </tr>
            <tr>
                <td colspan="2"><kbd>--an-even-longer-option</kbd></td>
            </tr>
            <tr>
                <td></td>
                <td>The description can also start on the next line.</td>
            </tr>
            <tr>
                <td><kbd>-2</kbd>, <kbd>--two</kbd></td>
                <td>This option has two variants.</td>
            </tr>
            <tr>
                <td colspan="2"><kbd>-f <var>FILE</var></kbd>, <kbd>--file=<var>FILE</var></kbd></td>
            </tr>
            <tr>
                <td></td>
                <td>These two options are synonyms; both have arguments.</td>
            </tr>
            <tr>
                <td><kbd>/V</kbd></td>
                <td>A VMS/DOS-style option.</td>
            </tr>
        </tbody>
    </table>
''',
    'indent_output': True,
    'option_limit': 15,
}

footnote = {
    'rst': '''[#]_ will be "2" (manually numbered),
[#]_ will be "3" (anonymous auto-numbered), and
[#label]_ will be "1" (labeled auto-numbered).

.. [#label] This autonumber-labeled footnote will be labeled "1".

   It is the first auto-numbered footnote and no other footnote
   with label "1" exists.

   The order of the footnotes is used to
   determine numbering, not the order of the footnote references.

.. [#] This footnote is labeled manually, so its number is fixed.

.. [#] This footnote will be labeled "3".  It is the second
   auto-numbered footnote, but footnote label "2" is already used.''',
   'out': '''
    <p><a href="#id4" id="id1" class="footnote_reference">[2]</a> will be "2" (manually numbered), \
<a href="#id5" id="id2" class="footnote_reference">[3]</a> will be "3" (anonymous auto-numbered), \
and <a href="#label" id="id3" class="footnote_reference">[1]</a> will be "1" \
(labeled auto-numbered).</p>
    <table id="label" class="footnote">
        <col />
        <col />
        <tbody>
            <tr>
                <th>[1]</th>
                <td>
                    <p>This autonumber-labeled footnote will be labeled "1".</p>
                    <p>It is the first auto-numbered footnote and no other footnote with label \
"1" exists.</p>
                    <p>The order of the footnotes is used to determine numbering, not the order \
of the footnote references.</p>
                </td>
            </tr>
        </tbody>
    </table>
    <table id="id4" class="footnote">
        <col />
        <col />
        <tbody>
            <tr>
                <th>[2]</th>
                <td>This footnote is labeled manually, so its number is fixed.</td>
            </tr>
        </tbody>
    </table>
    <table id="id5" class="footnote">
        <col />
        <col />
        <tbody>
            <tr>
                <th>[3]</th>
                <td>This footnote will be labeled "3". It is the second auto-numbered footnote, but footnote label "2" is already used.</td>
            </tr>
        </tbody>
    </table>
''',
   'indent_output': True,
}


line_block = {
    'rst': r"""
| paragraph = {
|     'rst': 'Paragraph',
|     'out': '<meta charset="utf-8" />',
|     'indent_output': **True**
| }
|
| def **test_body**\ ():
|     '''
|     test the *body* part of a rst2html5 conversion
|     '''
|     import test_data_body
|     for test_name, case in extract_variables(test_data_body):
|         yield _test_part, 'body', test_name, case""",
    'out': """
    <pre class="line_block">paragraph = {
    'rst': 'Paragraph',
    'out': '&lt;meta charset="utf-8" /&gt;',
    'indent_output': <strong>True</strong>
}

def <strong>test_body</strong>():
    '''
    test the <em>body</em> part of a rst2html5 conversion
    '''
    import test_data_body
    for test_name, case in extract_variables(test_data_body):
        yield _test_part, 'body', test_name, case</pre>
""",
    'indent_output': True
}

legend = {
    'rst': '''.. figure:: picture.png
   :scale: 50%
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).

   The legend consists of all elements after the caption.  In this
   case, the legend consists of this paragraph.
''',
    'out': '''
    <figure>
        <img src="picture.png" alt="map to buried treasure" scale="50" />
        <figcaption>This is the caption of the figure (a simple paragraph).</figcaption>
        <div class="legend">The legend consists of all elements after the caption. In this case, the legend consists of this paragraph.</div>
    </figure>
''',
    'indent_output': True
}