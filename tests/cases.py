#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2html5 in the form:
# case = {'rst': rst_text, 'out': expected_output, ...}

from __future__ import unicode_literals

indentation = {
    'rst': 'Paragraph',
    'out': '\n    <p>Paragraph</p>\n',
    'part': 'body',
}

title = {
    'rst': 'Title\n=====',
    'out': '<h1>Title</h1>',
    'indent_output': False,
    'part': 'body',
}


title_accented_chars = {
    'rst': 'Título com Acentuação\n'
           '=====================',
    'out': '<h1>Título com Acentuação</h1>',
    'indent_output': False,
    'part': 'body',
}

title_2 = {
    'rst': '''
Level 1
=======

some text

Level 1 Again
=============''',
    'out': '<a id="level-1"></a><section><h1>Level 1</h1>'
           '<p>some text</p></section>'
           '<a id="level-1-again"></a><section><h1>Level 1 Again</h1>'
           '</section>',
    'indent_output': False,
    'part': 'body',
}


title_3 = {
    'rst': '''
=======
Level 1
=======

some text. Link to `Level 3`_

.. _section 2:

Level 2
=======

more text

Level 3
--------

link to `section 2`_''',
    'out': '''
    <h1>Level 1</h1>
    <p>some text. Link to <a href="#level-3">Level 3</a></p>
    <a id="level-2"></a>
    <a id="section-2"></a>
    <section>
        <h2>Level 2</h2>
        <p>more text</p>
        <a id="level-3"></a>
        <section>
            <h3>Level 3</h3>
            <p>link to <a href="#section-2">section 2</a></p>
        </section>
    </section>
''',
    'part': 'body',
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
    'out': '<h1>Document Title</h1><h2>Subtitle</h2>'
           '<a id="section-title"></a><section><h1>Section Title</h1>'
           '<p>...</p></section>',
    'indent_output': False,
    'part': 'body',
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
    <h1>Document Title</h1>
    <h2>Subtitle</h2>
    <a id="section-title"></a>
    <section>
        <h1>Section Title</h1>
        <p>...</p>
    </section>
''',
    'part': 'body',
}


paragraph = {
    'rst': 'Lorem    ipsum dolor sit amet,        consectetur '
           'adipiscing          elit.\n'
           'Vestibulum    dignissim lacinia blandit. Suspendisse potenti.',
    'out': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
           'Vestibulum dignissim lacinia blandit. Suspendisse potenti.</p>',
    'indent_output': False,
    'part': 'body',
}


accented_paragraph = {
    'rst': 'Não há ninguém que ame a dor por si só, que a busque e '
           'queira tê-la, simplesmente por ser dor...',
    'out': '<p>Não há ninguém que ame a dor por si só, que a busque e '
           'queira tê-la, simplesmente por ser dor...</p>',
    'indent_output': False,
    'part': 'body',
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
           "</p></blockquote><p>This is another one.</p>",
    'indent_output': False,
    'part': 'body',
}


image = {
    'rst': '''.. _target:

target paragraph

.. image:: images/biohazard.png
   :width: 50px
   :height: 100px
   :alt: alternate text
   :target: target_
   :class: top

''',
    'out': '<a id="target"></a><p>target paragraph</p><a href="#target">'
           '<img src="images/biohazard.png" alt="alternate text" width="50px" '
           'class="top" height="100px" /></a>',
    'indent_output': False,
    'part': 'body',
}


figure = {
    'rst': '''.. figure:: picture.png
   :scale: 50%
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).''',
    'out': '''
    <figure>
        <img src="picture.png" alt="map to buried treasure" scale="50" />
        <figcaption>This is the caption of the figure \
(a simple paragraph).</figcaption>
    </figure>
''',
    'part': 'body'
}


inline_markup = {
    'rst': '''*emphasis*
**strong emphasis**
`interpreted text`
`superscript`:sup:
`interpreted text with role`:emphasis:
`subscript`:sub:
``inline  <pre>   text``
''',
    'out': '''
    <p><em>emphasis</em> <strong>strong emphasis</strong> \
<cite>interpreted text</cite> <sup>superscript</sup> \
<em>interpreted text with role</em> <sub>subscript</sub> \
<code>inline&nbsp;&nbsp;&lt;pre&gt;&nbsp;&nbsp;&nbsp;text</code></p>
''',
    'part': 'body'
}


bullet_list = {
    'rst': '* item 1\n* item 2\n  more text',
    'out': '<ul><li>item 1</li><li>item 2 more text</li></ul>',
    'indent_output': False,
    'part': 'body',
}

transition = {
    'rst': '''Paragraph

----------

Paragraph''',
    'out': '<p>Paragraph</p><hr /><p>Paragraph</p>',
    'indent_output': False,
    'part': 'body',
}

ordered_list_decimal = {
    'rst': '#. item 1\n#. item 2',
    'out': '<ol type="1"><li>item 1</li><li>item 2</li></ol>',
    'indent_output': False,
    'part': 'body',
}

ordered_list_decimal_autonumerated = {
    'rst': '3. item 3\n#. item 4',
    'out': '<ol start="3" type="1"><li>item 3</li><li>item 4</li></ol>',
    'indent_output': False,
    'part': 'body',
}

ordered_list_lower_alpha = {
    'rst': '(a) item 1\n(#) item 2\n(#) item 3',
    'out': '<ol prefix="(" type="a" suffix=")"><li>item 1</li><li>item 2</li>'
           '<li>item 3</li></ol>',
    'indent_output': False,
    'part': 'body',
}

ordered_list_upper_alpha = {
    'rst': 'A) item 1\n#) item 2\n#) item 3',
    'out': '<ol type="A" suffix=")"><li>item 1</li><li>item 2</li><li>item 3'
           '</li></ol>',
    'indent_output': False,
    'part': 'body',
}

ordered_list_lower_roman = {
    'rst': 'i. item 1\n#. item 2\n#. item 3',
    'out': '<ol type="i"><li>item 1</li><li>item 2</li><li>item 3</li></ol>',
    'indent_output': False,
    'part': 'body',
}

ordered_list_upper_roman = {
    'rst': 'I. item 1\n#. item 2\n#. item 3',
    'out': '<ol type="I"><li>item 1</li><li>item 2</li><li>item 3</li></ol>',
    'indent_output': False,
    'part': 'body',
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
    'part': 'body'
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
    'part': 'body'
}

grid_table_with_caption = {
    'rst': '''.. table:: What a nice table!

   +--------------+----------+
   | row 1, col 1 | column 2 |
   +--------------+----------+
   | row 2        |          |
   +--------------+----------+''',
    'out': '''
    <table>
        <caption>What a nice table!</caption>
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
    'part': 'body'
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
    'part': 'body'
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
    'part': 'body'
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
    'part': 'body'
}


external_link = {
    'rst': '''This is a paragraph that contains `a link`_.

.. _a link: http://example.com/''',
    'out': '<p>This is a paragraph that contains '
           '<a href="http://example.com/">a link</a>.</p>',
    'indent_output': False,
    'part': 'body',
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
    'part': 'body'
}

chained_internal_links = {
    'rst': '''Links to target1_ and target2_.

.. _target1:
.. _target2:

The targets "target1" and "target2" are synonyms; they both
point to this paragraph.''',
    'out': '''
    <p>Links to <a href="#target1">target1</a> and \
<a href="#target2">target2</a>.</p>
    <a id="target2"></a>
    <a id="target1"></a>
    <p>The targets "target1" and "target2" are synonyms; \
they both point to this paragraph.</p>
''',
    'part': 'body'
}

propagated_target = {
    'rst': '''Link to archive_.

.. _Python DOC-SIG mailing list archive:
.. _archive:
.. _Doc-SIG: http://mail.python.org/pipermail/doc-sig/''',
    'out': '''
    <p>Link to \
<a href="http://mail.python.org/pipermail/doc-sig/">archive</a>.</p>
''',
    'part': 'body'
}

inline_and_indirect_target = {
    'rst': '''This is a _`inline hyperlink target` that corresponds to \
a <target> in doctree.

Link to one_.

.. _one: two_
.. _two: three_
.. _three:

Target paragraph.

Referencing the  `inline hyperlink target`_.
''',

    'out': '''
    <p>This is a <a id="inline-hyperlink-target">inline hyperlink target</a> \
that corresponds to a &lt;target&gt; in doctree.</p>
    <p>Link to <a href="#three">one</a>.</p>
    <a id="three"></a>
    <p>Target paragraph.</p>
    <p>Referencing the \
<a href="#inline-hyperlink-target">inline hyperlink target</a>.</p>
''',
    'part': 'body'
}

anonymous_links = {
    'rst': '''Paragraphs contain text and may contain `anonymous hyperlink
references`__ (`a second reference`__).

__ http://www.python.org/
__ http://docutils.sourceforge.net/''',
    'out': '''
    <p>Paragraphs contain text and may contain \
<a href="http://www.python.org/">anonymous hyperlink references</a> \
(<a href="http://docutils.sourceforge.net/">a second reference</a>).</p>
''',
    'part': 'body',
}

section_with_two_ids = {
    'rst': '''Citations
---------

Here's a reference to example_.

.. _Another Target:

Targets
-------

Text of section target

.. _example:

Example
-------

This paragraph belongs to Example section.''',
    'out': '''
    <a id="citations"></a>
    <section>
        <h1>Citations</h1>
        <p>Here's a reference to <a href="#example">example</a>.</p>
    </section>
    <a id="targets"></a>
    <a id="another-target"></a>
    <section>
        <h1>Targets</h1>
        <p>Text of section target</p>
    </section>
    <a id="id1"></a>
    <a id="example"></a>
    <section>
        <h1>Example</h1>
        <p>This paragraph belongs to Example section.</p>
    </section>
''',
    'part': 'body',
}


literal_text = {
    'rst': '``<style>``',
    'out': '<p><code>&lt;style&gt;</code></p>',
    'indent_output': False,
    'part': 'body',
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
    'part': 'body'
}

parsed_literal_block = {
    'rst': '''.. parsed-literal::

   This is a parsed literal block.
       This line is indented.  The next line is blank.

   Inline markup is supported, e.g. *emphasis*, **strong**, ``literal
   text``, _`hyperlink targets`, and `references <http://www.python.org/>`_.
''',
    'out': '''
    <pre>This is a parsed literal block.
    This line is indented.  The next line is blank.

Inline markup is supported, e.g. <em>emphasis</em>, <strong>strong</strong>, \
<code>literal
text</code>, <a id="hyperlink-targets">hyperlink targets</a>, \
and <a href="http://www.python.org/">references</a>.</pre>
''',
    'part': 'body',
}

parsed_literal_as_code_block = {
    'rst': """.. class:: code language-python

.. parsed-literal::

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
    <pre><code class="language-python">def extract_variables(module):
    '''
    Extract variables of a test data module.
    Variables should be a dict().
    For example, {'rst': rst, 'out':out, ...}
    '''
    return ((v, getattr(module, v)) for v in dir(module)
        if not v.startswith('__') and isinstance(getattr(module, v), \
dict))</code></pre>
""",
    'part': 'body',
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
    <pre><code class="python"><span class="k">def</span> \
<span class="nf">extract_variables</span>\
<span class="p">(</span><span class="n">module</span><span class="p">):</span>
    <span class="sd">'''
    Extract variables of a test data module.
    Variables should be a dict().
    For example, {'rst': rst, 'out':out, ...}
    '''</span>
    <span class="k">return</span> <span class="p">((</span>\
<span class="n">v</span><span class="p">,</span> \
<span class="nb">getattr</span><span class="p">(</span>\
<span class="n">module</span><span class="p">,</span> \
<span class="n">v</span><span class="p">))</span> \
<span class="k">for</span> <span class="n">v</span> \
<span class="ow">in</span> <span class="nb">\
dir</span><span class="p">\
(</span><span class="n">module</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> \
<span class="n">v</span><span class="o">.</span>\
<span class="n">startswith</span><span class="p">(</span><span class="s">\
'__'</span><span class="p">)</span> <span class="ow">and</span> \
<span class="nb">isinstance</span><span class="p">(</span>\
<span class="nb">getattr</span><span class="p">(</span><span class="n">\
module</span><span class="p">,</span> <span class="n">v</span>\
<span class="p">),</span> <span class="nb">dict</span>\
<span class="p">))</span></code></pre>
""",
    'part': 'body'
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
    'part': 'body'
}

math_role = {
    'rst': r':math:`\sqrt{3x-1}+(1+x)^2`',
    'out': '<p><span class="math">\(\sqrt{3x-1}+(1+x)^2\)</span></p>',
    'indent_output': False,
    'part': 'body',
}

raw = {
    'rst': '''some text

.. raw:: html

    <hr width=50 size=10 />
    <br />

more text''',
    'out': '\n    <p>some text</p>\n<hr width=50 size=10 />\n<br />'
           '\n    <p>more text</p>\n',
    'part': 'body'
}

class_directive = {
    'rst': '''.. class:: nav special

paragraph with some text

.. class:: heading top

Section Title
=============''',
    'out': '<p class="nav special">paragraph with some text</p>'
           '<a id="section-title"></a>'
           '<section class="heading top">'
           '<h1>Section Title</h1></section>',
    'indent_output': False,
    'part': 'body',
}

role = {
    'rst': '''.. role:: custom
   :class: special

this is an :custom:`interpreted text`.''',
    'out': '<p>this is an <span class="special">interpreted text</span>.</p>',
    'indent_output': False,
    'part': 'body',
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
    <a id="subtitle"></a>
    <section>
        <h2>Subtitle</h2>
        <p>more text</p>
        <aside class="topic">
            <h1>Topic Title</h1>
            <p>Subsequent indented lines comprise the body of the topic, \
and are interpreted as body elements.</p>
        </aside>
    </section>
    <a id="another-subtitle"></a>
    <section>
        <h2>Another Subtitle</h2>
    </section>
''',
    'part': 'body',
}

admonitions = {
    'rst': '''Admonitions
```````````

.. Attention:: Directives at large.

.. Caution::

   Don't take any wooden nickels.

.. DANGER:: Mad scientist at work!

.. Error:: Does not compute.

.. Hint:: It's bigger than a bread box.

.. Important::
   - Wash behind your ears.
   - Clean up your room.
   - Call your mother.
   - Back up your data.

.. Note:: This is a note.

.. Tip:: 15% if the service is good.

.. WARNING:: Strong prose may provoke extreme mental exertion.
   Reader discretion is strongly advised.

.. admonition:: And, by the way...

   You can make up your own admonition too.

   .. _Docutils: http://docutils.sourceforge.net/''',
    'out': '''
    <h1>Admonitions</h1>
    <aside class="attention">Directives at large.</aside>
    <aside class="caution">Don't take any wooden nickels.</aside>
    <aside class="danger">Mad scientist at work!</aside>
    <aside class="error">Does not compute.</aside>
    <aside class="hint">It's bigger than a bread box.</aside>
    <aside class="important">
        <ul>
            <li>Wash behind your ears.</li>
            <li>Clean up your room.</li>
            <li>Call your mother.</li>
            <li>Back up your data.</li>
        </ul>
    </aside>
    <aside class="note">This is a note.</aside>
    <aside class="tip">15% if the service is good.</aside>
    <aside class="warning">Strong prose may provoke extreme mental exertion. \
Reader discretion is strongly advised.</aside>
    <aside class="admonition">
        <h1>And, by the way...</h1>
        <p>You can make up your own admonition too.</p>
    </aside>
''',
    'part': 'body',
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
    <a id="subtitle"></a>
    <section>
        <h2>Subtitle</h2>
        <p>more text</p>
        <aside class="admonition special">
            <h1>This is a note admonition.</h1>
            <p>This is the second line of the first paragraph.</p>
            <ul>
                <li>The note contains all indented body elements \
following.</li>
                <li>It includes this bullet list.</li>
            </ul>
        </aside>
    </section>
    <a id="another-subtitle"></a>
    <section>
        <h2>Another Subtitle</h2>
    </section>
''',
    'part': 'body',
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
    <a id="subtitle"></a>
    <section>
        <h2>Subtitle</h2>
        <p>more text</p>
        <aside class="sidebar">
            <h1>This is a sidebar</h1>
            <h2>Sidebar Subtitle</h2>
            <p>This is the second line of the first paragraph.</p>
            <ul>
                <li>The note contains all indented body elements \
following.</li>
                <li>It includes this bullet list.</li>
            </ul>
        </aside>
    </section>
    <a id="another-subtitle"></a>
    <section>
        <h2>Another Subtitle</h2>
    </section>
''',
    'part': 'body',
}

rubric = {
    'rst': 'some text\n\n.. rubric:: RuBriC\n    :class: special heading'
           '\n\nmore text',
    'out': '<p>some text</p><p class="rubric">RuBriC</p><p>more text</p>',
    'indent_output': False,
    'part': 'body',
}

epigraph = {
    'rst': '''.. epigraph::

   No matter where you go, there you are.''',
    'out': '<blockquote class="epigraph"><p>No matter where you go, there you '
           'are.</p></blockquote>',
    'indent_output': False,
    'part': 'body',
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
        <p>The 'rm' command is very dangerous. If you are logged in as \
root and enter</p>
        <pre>cd /
rm -rf *</pre>
        <p>you will erase the entire contents of your file system.</p>
    </div>
''',
    'part': 'body'
}

container = {
    'rst': '''.. container:: custom

   This paragraph might be rendered in a custom way.''',
    'out': '<div class="container custom">This paragraph might be rendered '
           'in a custom way.</div>',
    'indent_output': False,
    'part': 'body',
}

contents = {
    'rst': '''.. contents:: Table of Contents
   :depth: 2

Basic Usage
===========

To start using subrepositories, you need two repositories, a main repo and \
a nested repo''',
    'out': '''
    <a id="table-of-contents"></a>
    <aside class="topic contents">
        <h1>Table of Contents</h1>
        <ul>
            <li><a href="#basic-usage">Basic Usage</a></li>
        </ul>
    </aside>
    <a id="basic-usage"></a>
    <section>
        <h1>Basic Usage</h1>
        <p>To start using subrepositories, you need two repositories, a main \
repo and a nested repo</p>
    </section>
''',
    'part': 'body',
}

header = {
    'rst': '.. header:: This space for rent.',
    'out': '<header>This space for rent.</header>',
    'indent_output': False,
    'part': 'body',
}

footer = {
    'rst': '.. footer:: This space for rent.',
    'out': '<footer>This space for rent.</footer>',
    'indent_output': False,
    'part': 'body',
}

header_and_footer = {
    'rst': '''Title
=====

some text

.. header:: this is a header

more text

.. footer:: this is a footer''',
    'out': '''
    <h1>Title</h1>
    <header>this is a header</header>
    <p>some text</p>
    <p>more text</p>
    <footer>this is a footer</footer>
''',
    'indent_output': True,
    'part': 'body',
}


replace = {
    'rst': '''.. |reST| replace:: reStructuredText

Yes, |reST| is a long word, so I can't blame anyone for wanting to
abbreviate it.''',
    'out': "<p>Yes, reStructuredText is a long word, so I can't blame "
           "anyone for wanting to abbreviate it.</p>",
    'indent_output': False,
    'part': 'body',
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
:Abstract: Generates (X)HTML5 documents from standalone reStructuredText \
sources.
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
                <td><a href="mailto:andref.dias@pronus.eng.br">\
andref.dias@pronus.eng.br</a></td>
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
subsequent lines of the field body do not have to line up with the \
first line, but they must be indented relative to the field name marker, \
and they must line up with each other.</td>
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
        <p>Generates (X)HTML5 documents from standalone reStructuredText \
sources.</p>
    </aside>
''',
    'part': 'body',
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
                <td>See <a href="https://bitbucket.org/\
andre_felipe_dias/rst2html5">https://bitbucket.org/andre_felipe_dias/\
rst2html5</a></td>
            </tr>
            <tr>
                <th>author</th>
                <td>André Felipe Dias &lt;<a href="mailto:\
andref.dias@gmail.com">andref.dias@gmail.com</a>&gt;</td>
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
    'part': 'body'
}

comment = {
    'rst': '''..
    comment <comment> comment
    comment

    more text''',
    'out': '',
    'indent_output': False,
    'part': 'body',
}

citation = {
    'rst': '''this is a citation [CIT2012]_

Another [TEST2]_.

.. [CIT2012] A citation
.. [TEST2] Test text''',
    'out': '''
    <p>this is a citation <a href="#cit2012" id="id1" \
class="citation_reference">[CIT2012]</a></p>
    <p>Another <a href="#test2" id="id2" \
class="citation_reference">[TEST2]</a>.</p>
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
    'part': 'body'
}

attribution = {
    'rst': '''Quote:

    "Choose a job you love, and you will never have to work a day \
in your life."

    -- Confucius''',
    'out': '''
    <p>Quote:</p>
    <blockquote>
        <p>"Choose a job you love, and you will never have to work a day \
in your life."</p>
        <p class="attribution">Confucius</p>
    </blockquote>
''',
    'part': 'body'
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
    'part': 'body'
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
                    <p>This option has two paragraphs in the description. \
This is the first.</p>
                    <p>This is the second. Blank lines may be omitted \
between options (as above) or left in (as here and below).</p>
                </td>
            </tr>
            <tr>
                <td colspan="2"><kbd>--very-long-option</kbd></td>
            </tr>
            <tr>
                <td></td>
                <td>A VMS-style option. Note the adjustment for the required \
two spaces.</td>
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
                <td colspan="2"><kbd>-f <var>FILE</var></kbd>, \
<kbd>--file=<var>FILE</var></kbd></td>
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
    'part': 'body',
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
    <p><a href="#id4" id="id1" class="footnote_reference">[2]</a> \
will be "2" (manually numbered), <a href="#id5" id="id2" \
class="footnote_reference">[3]</a> will be "3" (anonymous auto-numbered), \
and <a href="#label" id="id3" class="footnote_reference">[1]</a> will be "1" \
(labeled auto-numbered).</p>
    <table id="label" class="footnote">
        <col />
        <col />
        <tbody>
            <tr>
                <th>[1]</th>
                <td>
                    <p>This autonumber-labeled footnote will be \
labeled "1".</p>
                    <p>It is the first auto-numbered footnote and no other \
footnote with label "1" exists.</p>
                    <p>The order of the footnotes is used to determine \
numbering, not the order of the footnote references.</p>
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
                <td>This footnote is labeled manually, so its number is \
fixed.</td>
            </tr>
        </tbody>
    </table>
    <table id="id5" class="footnote">
        <col />
        <col />
        <tbody>
            <tr>
                <th>[3]</th>
                <td>This footnote will be labeled "3". It is the second \
auto-numbered footnote, but footnote label "2" is already used.</td>
            </tr>
        </tbody>
    </table>
''',
    'part': 'body',
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
    'part': 'body'
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
        <figcaption>This is the caption of the figure (a simple paragraph).\
</figcaption>
        <div class="legend">The legend consists of all elements after the \
caption. In this case, the legend consists of this paragraph.</div>
    </figure>
''',
    'part': 'body'
}

# stderr should present: <string>:1: (ERROR/3) Unknown target name: "target"
system_message = {
    'rst': 'target_',
    'out': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
</head>
<body>
    <p><a href="#id1" id="id2" class="problematic">target_</a></p>
    <section class="system-messages">
        <h1>Docutils System Messages</h1>
        <a id="id1"></a>
        <div>
            <h1>System Message: ERROR/3 (&lt;string&gt; line 1) \
<a href="#id2">id2</a></h1>
            <p>Unknown target name: "target".</p>
        </div>
    </section>
</body>
</html>''',
    'part': 'whole',
}


system_message_2 = {
    'rst': '''Target1__
Target2__

.. __: http://opensource.org/licenses/MIT
''',
    'out': '''
    <p><a href="#id2" id="id3" class="problematic">Target1__</a> \
<a href="#id2" id="id4" \
class="problematic">Target2__</a></p>
    <section class="system-messages">
        <h1>Docutils System Messages</h1>
        <a id="id2"></a>
        <div>
            <h1>System Message: ERROR/3 (&lt;string&gt; line ) \
<a href="#id3">id3</a> \
<a href="#id4">id4</a></h1>
            <p>Anonymous hyperlink mismatch: 2 references but 1 targets. \
See "backrefs" attribute for IDs.</p>
        </div>
    </section>
''',
    'part': 'body',
}

problematic = {
    'rst': '''[2]_

.. [#] footnote''',
    'out': '''
    <p><a href="#id3" id="id4" class="problematic">[2]_</a></p>
    <table id="id2" class="footnote">
        <col />
        <col />
        <tbody>
            <tr>
                <th>[1]</th>
                <td>footnote</td>
            </tr>
        </tbody>
    </table>
    <section class="system-messages">
        <h1>Docutils System Messages</h1>
        <a id="id3"></a>
        <div>
            <h1>System Message: ERROR/3 (&lt;string&gt; line 1) \
<a href="#id4">id4</a></h1>
            <p>Unknown target name: "2".</p>
        </div>
    </section>
''',
    'part': 'body',
}

paragraph_h = {
    'rst': 'Paragraph',
    'out': '\n    <meta charset="utf-8" />\n',
    'part': 'head',
}

math_role = {
    'rst': r':math:`\sqrt{3x-1}+(1+x)^2`',
    'out': '<meta charset="utf-8" />\
<script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js'
           '?config=TeX-AMS-MML_HTMLorMML"></script>',
    'indent_output': False,
    'part': 'head',
}

metadata = {
    'rst': '.. title:: Foo Bar',
    'out': '<meta charset="utf-8" /><title>Foo Bar</title>',
    'indent_output': False,
    'part': 'head',
}

stylesheet = {
    'rst': 'ordinary paragraph',
    'out': '''
    <meta charset="utf-8" />
    <link href="http://test.com/css/default.css" rel="stylesheet" />
    <link href="http://www.pronus.eng.br/css/standard.css" rel="stylesheet" />
''',
    'part': 'head',
    'stylesheet': 'http://test.com/css/default.css, '
                  'http://www.pronus.eng.br/css/standard.css'
}

javascript = {
    'rst': 'ordinary paragraph',
    'out': '''
    <meta charset="utf-8" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/\
1.7.2/jquery.min.js"></script>
''',
    'script': 'https://ajax.googleapis.com/ajax/libs/jquery/\
1.7.2/jquery.min.js',
    'part': 'head',
}

meta_h = {
    'rst': '''.. meta::
    :author: André Felipe Dias

.. meta::
    :http-equiv=X-UA-Compatible: chrome=1
''',
    'out': '''
    <meta charset="utf-8" />
    <meta content="André Felipe Dias" name="author" />
    <meta content="chrome=1" http-equiv="X-UA-Compatible" />
''',
    'part': 'head',
}
