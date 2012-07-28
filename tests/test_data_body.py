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
        'rst': 'Lorem    ipsum dolor sit amet,        consectetur ' \
               'adipiscing          elit.\n' \
                'Vestibulum    dignissim lacinia blandit. Suspendisse potenti.',
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
        'rst': '''This is a paragraph.  It's   quite
short.

   This paragraph will result in an indented block of
   text, typically used for quoting other text.

This is another one.''',
        'out': "<p>This is a paragraph. It's quite short.</p>" \
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
    <p>Clicking on this internal hyperlink will take us to the
        <a href="#target">target</a>
     below.</p>
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
    <p>Links to
        <a href="#target1">target1</a>
     and
        <a href="#target2">target2</a>
    .</p>
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
    <p>Link to
        <a href="http://mail.python.org/pipermail/doc-sig/">archive</a>
    .</p>
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
    <p>Link to
        <a href="#three">one</a>
    .</p>
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
    'out': '<p class="nav special">paragraph with some text</p><section class="heading top">'\
           '<h1>Section Title</h1></section>'
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
    'indent_output': True
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
    'indent_output': True
}

generic_admonition = {
    'rst': '''
Title
=====

text

Subtitle
--------

more text

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
        <aside class="admonition">
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
    'indent_output': True
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
    'indent_output': True
}

