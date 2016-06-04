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

title_with_initial_header = {
    'rst': 'Title\n=====\n\nhello\n-------',
    'out': '<h2>Title</h2><h3>hello</h3>',
    'indent_output': False,
    'part': 'body',
    'initial_header_level': 2
}


title_part = {
    'rst': '''
AbCdE fGhIjK
============''',
    'out': 'AbCdE fGhIjK',
    'part': 'title',
}

title_part_2 = {
    'rst': '''
AbCdE fGhIjK
============''',
    'out': 'Hello World',
    'title': 'Hello World',
    'part': 'title',
}

title_accented_chars = {
    'rst': 'Título com Acentuação\n'
           '=====================',
    'out': '<h1>Título com Acentuação</h1>',
    'indent_output': False,
    'part': 'body',
}

sections_1 = {
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
    <a id="section-2"></a>
    <section id="level-2">
        <h2>Level 2</h2>
        <p>more text</p>
        <section id="level-3">
            <h3>Level 3</h3>
            <p>link to <a href="#section-2">section 2</a></p>
        </section>
    </section>
''',
    'part': 'body',
}

# http://docutils.sourceforge.net/docs/user/rst/quickstart.html#sections

sections_2 = {
    'rst': '''
Chapter 1 Title
===============

Section 1.1 Title
-----------------

Subsection 1.1.1 Title
~~~~~~~~~~~~~~~~~~~~~~

Section 1.2 Title
-----------------

Chapter 2 Title
===============''',
    'part': 'body',
    'out': '''
    <section id="chapter-1-title">
        <h1>Chapter 1 Title</h1>
        <section id="section-1-1-title">
            <h2>Section 1.1 Title</h2>
            <section id="subsection-1-1-1-title">
                <h3>Subsection 1.1.1 Title</h3>
            </section>
        </section>
        <section id="section-1-2-title">
            <h2>Section 1.2 Title</h2>
        </section>
    </section>
    <section id="chapter-2-title">
        <h1>Chapter 2 Title</h1>
    </section>
''',
}


# http://docutils.sourceforge.net/docs/user/rst/quickstart.html#document-title-subtitle

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
           '<section id="section-title"><h1>Section Title</h1>'
           '<p>...</p></section>',
    'indent_output': False,
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
    'out': '<p id="target">target paragraph</p><a href="#target">'
           '<img width="50px" alt="alternate text" src="images/biohazard.png" '
           'class="top" height="100px" /></a>',
    'indent_output': False,
    'part': 'body',
}


figure = {
    'rst': '''.. figure:: picture.png
   :name: buried treasure
   :scale: 50%
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).''',
    'out': '''
    <figure id="buried-treasure">
        <img alt="map to buried treasure" scale="50" src="picture.png" />
        <figcaption>This is the caption of the figure (a simple paragraph).</figcaption>
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
<code>inline  &lt;pre&gt;   text</code></p>
''',
    'part': 'body'
}


bullet_list = {
    'rst': '* item 1\n* item 2\n  more text',
    'out': '<ul><li>item 1</li><li>item 2 more text</li></ul>',
    'indent_output': False,
    'part': 'body',
}

sublist = {
    'rst': '''* item 1
* item 2

    * subitem 1
    * subitem 2

* item 3

  Another paragraph''',
    'out': '''
    <ul>
        <li>item 1</li>
        <li>item 2
            <ul>
                <li>subitem 1</li>
                <li>subitem 2</li>
            </ul>
        </li>
        <li>item 3
            <p>Another paragraph</p>
        </li>
    </ul>
''',
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
    'out': '<ol suffix=")" type="a" prefix="("><li>item 1</li><li>item 2</li>'
           '<li>item 3</li></ol>',
    'indent_output': False,
    'part': 'body',
}

ordered_list_upper_alpha = {
    'rst': 'A) item 1\n#) item 2\n#) item 3',
    'out': '<ol suffix=")" type="A"><li>item 1</li><li>item 2</li><li>item 3'
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
<span class="classifier">classifier</span></dt>
        <dd>Definition 3.</dd>
        <dt>term 4 <span class="classifier-delimiter">:</span> <span \
class="classifier">classifier one</span> <span class="classifier-delimiter">\
:</span> <span class="classifier">classifier two</span></dt>
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
    <p id="target">The hyperlink target above points to this paragraph.</p>
''',
    'part': 'body'
}

chained_internal_links_1 = {
    'rst': '''Links to outer_target_ and inner_target_.

.. _outer_target:
.. _inner_target:

The targets "outer_target" and "inner_target" are synonyms; they both
point to this paragraph.''',
    'out': '''
    <p>Links to <a href="#outer-target">outer_target</a> and <a href="#inner-target">inner_target</a>.</p>
    <a id="outer-target"></a>
    <p id="inner-target">The targets "outer_target" and "inner_target" are synonyms; \
they both point to this paragraph.</p>
''',
    'part': 'body'
}


chained_internal_links_2 = {
    'rst': '''Links to outer_target_ and inner_target_.

.. _outer_target:
.. _inner_target:

Title 1
=======

The targets "outer_target" and "inner_target" point both to Title 1.''',
    'out': '''
    <p>Links to <a href="#outer-target">outer_target</a> and <a href="#inner-target">inner_target</a>.</p>
    <a id="inner-target"></a>
    <a id="outer-target"></a>
    <section id="title-1">
        <h1>Title 1</h1>
        <p>The targets "outer_target" and "inner_target" point both to Title 1.</p>
    </section>
''',
    'part': 'body'
}

propagated_target = {
    'rst': '''Link to archive_.

.. _Python DOC-SIG mailing list archive:
.. _archive:
.. _Doc-SIG: http://mail.python.org/pipermail/doc-sig/''',
    'out': '''
    <p>Link to <a href="http://mail.python.org/pipermail/doc-sig/">archive</a>.</p>
''',
    'part': 'body'
}

inline_and_indirect_target = {
    'rst': '''This is a _`inline hyperlink target` that corresponds to a <target> in doctree.

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
    <p id="three">Target paragraph.</p>
    <p>Referencing the <a href="#inline-hyperlink-target">inline hyperlink target</a>.</p>
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
    <section id="citations">
        <h1>Citations</h1>
        <p>Here's a reference to <a href="#example">example</a>.</p>
    </section>
    <a id="another-target"></a>
    <section id="targets">
        <h1>Targets</h1>
        <p>Text of section target</p>
    </section>
    <a id="example"></a>
    <section id="id1">
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

code_role = {
    'rst': '''
.. role:: htmlcode(code)
   :language: html

Is it okay to use :htmlcode:`<input type="tel"/>` now?

Yes, any unsupported type will revert to the ``type=text`` format.
''',
    'out': '''
    <p>Is it okay to use <code class="html"><span class="nt">&lt;input</span> <span class="na">type=</span>\
<span class="s">"tel"</span><span class="nt">/&gt;</span></code> now?</p>
    <p>Yes, any unsupported type will revert to the <code>type=text</code> format.</p>
''',
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

Inline markup is supported, e.g. <em>emphasis</em>, <strong>strong</strong>, <code>literal
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
    <pre data-language="python">def extract_variables(module):
    '''
    Extract variables of a test data module.
    Variables should be a dict().
    For example, {'rst': rst, 'out':out, ...}
    '''
    return ((v, getattr(module, v)) for v in dir(module)
        if not v.startswith('__') and isinstance(getattr(module, v), dict))</pre>
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
    <pre data-language="python"><span class="k">def</span> \
<span class="nf">extract_variables</span>\
<span class="p">(</span><span class="n">module</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    Extract variables of a test data module.</span>
<span class="sd">    Variables should be a dict().</span>
<span class="sd">    For example, {&#39;rst&#39;: rst, &#39;out&#39;:out, ...}</span>
<span class="sd">    &#39;&#39;&#39;</span>

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
&#39;__&#39;</span><span class="p">)</span> <span class="ow">and</span> \
<span class="nb">isinstance</span><span class="p">(</span>\
<span class="nb">getattr</span><span class="p">(</span><span class="n">\
module</span><span class="p">,</span> <span class="n">v</span>\
<span class="p">),</span> <span class="nb">dict</span>\
<span class="p">))</span></pre>
""",
    'part': 'body'
}


class_code_block = {
    'rst': """.. code-block:: python
    :class: small

    print('Hello, world!')""",
    'out': '''<pre data-language="python" class="small"><span class="k">print</span>\
<span class="p">(</span><span class="s">&#39;Hello, world!&#39;</span><span class="p">)</span>\
</pre>''',
    'part': 'body',
    'indent_output': False,
}


code_block_indented_first_line = {
    'rst': '''
.. code-block:: java
    :number-lines: 21

            // walk over the characters in question, looking for mismatches.
            int j = prefix.length() + offset;
        }
    }''',
    'out': '''<table data-language="java"><tr><td><pre>21
22
23
24</pre></td><td><pre>        <span class="c1">// walk over the characters in question, looking for mismatches.</span>
        <span class="kt">int</span> <span class="n">j</span> <span class="o">=</span> \
<span class="n">prefix</span><span class="o">.</span><span class="na">length</span>\
<span class="o">()</span> <span class="o">+</span> <span class="n">offset</span><span class="o">;</span>
    <span class="o">}</span>
<span class="o">}</span></pre></td></tr></table>''',
    'part': 'body',
    'indent_output': False,
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

math_one_script_only = {
    'rst': '\n'.join([math['rst']] * 10),
    'part': 'head',
    'out': '''
    <meta charset="utf-8" />
    <script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
''',
}

math_role_body = {
    'rst': r':math:`\sqrt{3x-1}+(1+x)^2`',
    'out': '<p><span class="math">\(\sqrt{3x-1}+(1+x)^2\)</span></p>',
    'indent_output': False,
    'part': 'body',
}

math_role_head = {
    'rst': r':math:`\sqrt{3x-1}+(1+x)^2`',
    'out': '''<meta charset="utf-8" />\
<script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>''',
    'indent_output': False,
    'part': 'head',
}

raw_html = {
    'rst': '''some text

.. raw:: html

    <div class="warning">
        <p>Warning!!!</p>
    </div>

more text''',
    'out': '\n    <p>some text</p>'
           '\n    <div class="warning">'
           '\n        <p>Warning!!!</p>'
           '\n    </div>'
           '\n    <p>more text</p>\n',
    'part': 'body'
}

raw_latex = {
    'rst': '''some text

.. raw:: latex

    \setlength{\parindent}{0pt}

more text''',
    'out': '\n    <p>some text</p>'
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
           '<section id="section-title" class="heading top">'
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
    <section id="subtitle">
        <h2>Subtitle</h2>
        <p>more text</p>
        <aside class="topic">
            <h1>Topic Title</h1>
            <p>Subsequent indented lines comprise the body of the topic, \
and are interpreted as body elements.</p>
        </aside>
    </section>
    <section id="another-subtitle">
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
    <section id="subtitle">
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
    <section id="another-subtitle">
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
    <section id="subtitle">
        <h2>Subtitle</h2>
        <p>more text</p>
        <aside class="sidebar">
            <h1>This is a sidebar</h1>
            <h2>Sidebar Subtitle</h2>
            <p>This is the second line of the first paragraph.</p>
            <ul>
                <li>The note contains all indented body elements following.</li>
                <li>It includes this bullet list.</li>
            </ul>
        </aside>
    </section>
    <section id="another-subtitle">
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
   :class: custom

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.''',
    'out': '''
    <div class="custom">
        <p>The 'rm' command is very dangerous. If you are logged in as root and enter</p>
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
    'out': '<div class="custom">This paragraph might be rendered '
           'in a custom way.</div>',
    'indent_output': False,
    'part': 'body',
}

contents = {
    'rst': '''.. contents:: Table of Contents
   :depth: 2

Basic Usage
===========

To start using subrepositories, you need two repositories, a main repo and a nested repo''',
    'out': '''
    <aside id="table-of-contents" class="topic contents">
        <h1>Table of Contents</h1>
        <ul>
            <li><a href="#basic-usage">Basic Usage</a></li>
        </ul>
    </aside>
    <section id="basic-usage">
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
:Abstract: Generates (X)HTML5 documents from standalone reStructuredText sources.
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter i: integer''',
    'out': '''
    <aside class="topic dedication">
        <h1>Dedication</h1>
        <p>To Andréa, Dexter e DeeDee</p>
    </aside>
    <aside class="topic abstract">
        <h1>Abstract</h1>
        <p>Generates (X)HTML5 documents from standalone reStructuredText sources.</p>
    </aside>
''',
    'part': 'body',
}

docinfo1 = {
    'rst': docinfo['rst'],
    'out': '''
    <meta charset="utf-8" />
    <meta content="1" name="version" />
    <meta content="André; Felipe; Dias" name="authors" />
    <meta content="Pronus Engenharia de Software" name="organization" />
    <meta content="andref.dias@pronus.eng.br" name="contact" />
    <meta content="Av. Ipê Amarelo, Sumaré - São Paulo - Brasil, 13175-667" name="address" />
    <meta content="Alpha" name="status" />
    <meta content="2012-07-29" name="date" />
    <meta content="André Felipe Dias" name="copyright" />
    <meta content="Since the field marker may be quite long, the second and subsequent lines of \
the field body do not have to line up with the first line, but they must be indented relative to \
the field name marker, and they must line up with each other." name="Indentation" />
    <meta content="integer" name="Parameter i" />
''',
    'part': 'head',
}

docinfo2 = {
    'rst': ''':Info: See https://bitbucket.org/andre_felipe_dias/rst2html5
:Author: André Felipe Dias <andref.dias@gmail.com>
:Date: 2012-07-30
:Revision: 38
:Description: This is a "docinfo block", or bibliographic field list''',
    'out': '''
    <meta charset="utf-8" />
    <meta content="See https://bitbucket.org/andre_felipe_dias/rst2html5" name="Info" />
    <meta content="André Felipe Dias &lt;andref.dias@gmail.com&gt;" name="author" />
    <meta content="2012-07-30" name="date" />
    <meta content="38" name="revision" />
    <meta content="This is a &#34;docinfo block&#34;, or bibliographic field list" name="Description" />
''',
    'part': 'head',
}

docinfo3 = {
    'rst': ''':tags: oh, bar, yeah
:category: bar
:slug: oh-yeah
:license: WTFPL
:test: <tag>''',
    'out': '''
    <meta charset="utf-8" />
    <meta content="oh, bar, yeah" name="tags" />
    <meta content="bar" name="category" />
    <meta content="oh-yeah" name="slug" />
    <meta content="WTFPL" name="license" />
    <meta content="&lt;tag&gt;" name="test" />
''',
    'part': 'head',
}

docinfo4 = {
    'rst': docinfo3['rst'],
    'out': '',
    'part': 'body',
}

docinfo5 = {
    'rst': docinfo3['rst'],
    'part': 'docinfo',
    'out': {'tags': 'oh, bar, yeah',
            'category': 'bar',
            'slug': 'oh-yeah',
            'license': 'WTFPL',
            'test': '<tag>',
            },
}

field_list_1 = {
    'rst': ''':http-equiv=X-UA-Compatible: chrome=1:
:viewport: width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes

..

:data-x: 1000
:data-y: 2000

Title
=====

Text

Title 2
=======

Another line
''',
    'part': 'whole',
    'out': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta content="chrome=1:" name="http-equiv=X-UA-Compatible" />
    <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />
    <meta content="1000" name="data-x" />
    <meta content="2000" name="data-y" />
</head>
<body>
    <section id="title">
        <h1>Title</h1>
        <p>Text</p>
    </section>
    <section id="title-2">
        <h1>Title 2</h1>
        <p>Another line</p>
    </section>
</body>
</html>''',
}

field_list_2 = {
    'rst': ''':http-equiv=X-UA-Compatible: chrome=1:
:viewport: width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes

Title
=====

Text

:data-x: 1000
:data-y: 2000

Title 2
=======

Another line
''',
    'part': 'whole',
    'out': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta content="chrome=1:" name="http-equiv=X-UA-Compatible" />
    <meta content="width=device-width, maximum-scale=1.0, initial-scale=1.0, user-scalable=yes" name="viewport" />
    <meta content="1000" name="data-x" />
    <meta content="2000" name="data-y" />
</head>
<body>
    <section id="title">
        <h1>Title</h1>
        <p>Text</p>
    </section>
    <section id="title-2">
        <h1>Title 2</h1>
        <p>Another line</p>
    </section>
</body>
</html>''',
}


citation = {
    'rst': '''this is a citation [CIT2012]_

Another [TEST2]_.

.. [CIT2012] A citation
.. [TEST2] Test text''',
    'out': '''
    <p>this is a citation <a id="id1" href="#cit2012" class="citation_reference">CIT2012</a></p>
    <p>Another <a id="id2" href="#test2" class="citation_reference">TEST2</a>.</p>
    <table id="cit2012" class="citation">
        <tbody>
            <tr>
                <th>CIT2012</th>
                <td>A citation</td>
            </tr>
        </tbody>
    </table>
    <table id="test2" class="citation">
        <tbody>
            <tr>
                <th>TEST2</th>
                <td>Test text</td>
            </tr>
        </tbody>
    </table>
''',
    'part': 'body'
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
                    <p>This is the second. Blank lines may be omitted between options (as above) \
or left in (as here and below).</p>
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
    <p><a id="id1" href="#id4" class="footnote_reference">2</a> \
will be "2" (manually numbered), <a id="id2" href="#id5" \
class="footnote_reference">3</a> will be "3" (anonymous auto-numbered), \
and <a id="id3" href="#label" class="footnote_reference">1</a> will be "1" \
(labeled auto-numbered).</p>
    <table id="label" class="footnote">
        <tbody>
            <tr>
                <th>1</th>
                <td>
                    <p>This autonumber-labeled footnote will be labeled "1".</p>
                    <p>It is the first auto-numbered footnote and no other \
footnote with label "1" exists.</p>
                    <p>The order of the footnotes is used to determine \
numbering, not the order of the footnote references.</p>
                </td>
            </tr>
        </tbody>
    </table>
    <table id="id4" class="footnote">
        <tbody>
            <tr>
                <th>2</th>
                <td>This footnote is labeled manually, so its number is fixed.</td>
            </tr>
        </tbody>
    </table>
    <table id="id5" class="footnote">
        <tbody>
            <tr>
                <th>3</th>
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


line_block_2 = {
    'rst': '''Some text

|      1234 Sesame St.
|      New York, NY 10001
|      tel:555-111-1111
|      nobody@nowhere.org

.. sidebar:: Contact

   | 123 Address St.
   | City, State ZIP
''',
    'part': 'body',
    'out': '''
    <p>Some text</p>
    <pre class="line_block">1234 Sesame St.
New York, NY 10001
<a href="tel:555-111-1111">tel:555-111-1111</a>
<a href="mailto:nobody@nowhere.org">nobody@nowhere.org</a></pre>
    <aside class="sidebar">
        <h1>Contact</h1>
        <pre class="line_block">123 Address St.
City, State ZIP</pre>
    </aside>
''',
}

line_block_3 = {
    'rst': '''Take it away, Eric the Orchestra Leader!

| A one, two, a one two three four
|
| Half a bee, philosophically,
|     must, *ipso facto*, half not be.
| But half the bee
  has got to be,
|     *vis a vis* its entity.  D'you see?
|
| But can a bee be said to be
|     or not to be an entire bee,
|         when half the bee is not a bee,
|             due to some ancient injury?
|
| Singing...
''',
    'out': '''
    <p>Take it away, Eric the Orchestra Leader!</p>
    <pre class="line_block">A one, two, a one two three four

Half a bee, philosophically,
    must, <em>ipso facto</em>, half not be.
But half the bee has got to be,
    <em>vis a vis</em> its entity. D'you see?
    \

But can a bee be said to be
    or not to be an entire bee,
        when half the bee is not a bee,
            due to some ancient injury?
            \

Singing...</pre>
''',
    'part': 'body',
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
        <img alt="map to buried treasure" scale="50" src="picture.png" />
        <figcaption>This is the caption of the figure (a simple paragraph).</figcaption>
        <div class="legend">The legend consists of all elements after the \
caption. In this case, the legend consists of this paragraph.</div>
    </figure>
''',
    'part': 'body'
}

legend_more = {
    'rst': '''.. figure:: picture.png
   :scale: 50%
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).

   The legend consists of all elements after the caption.  In this
   case, the legend consists of this paragraph.

   .. image:: x-mark.png
      :name: xmark
      :alt: image of x mark
''',
    'out': '''
    <figure>
        <img alt="map to buried treasure" scale="50" src="picture.png" />
        <figcaption>This is the caption of the figure (a simple paragraph).</figcaption>
        <div class="legend">
            <p>The legend consists of all elements after the \
caption. In this case, the legend consists of this paragraph.</p>
            <img alt="image of x mark" src="x-mark.png" id="xmark" />
        </div>
    </figure>
''',
    'part': 'body'
}

# stderr should present: <string>:1: (ERROR/3) Unknown target name: "target"
system_message = {
    'rst': 'target_',
    'out': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
</head>
<body>
    <p><a id="id2" href="#id1" class="problematic">target_</a></p>
    <section class="system-messages">
        <h1>Docutils System Messages</h1>
        <div id="id1">
            <h1>System Message: ERROR/3 (&lt;string&gt; line 1) <a href="#id2">id2</a></h1>
            <p>Unknown target name: "target".</p>
        </div>
    </section>
</body>
</html>''',
    'part': 'whole',
    'error': '<string>:1: (ERROR/3) Unknown target name: "target".\n',
}


system_message_2 = {
    'rst': '''Target1__
Target2__

.. __: http://opensource.org/licenses/MIT
''',
    'out': '''
    <p><a id="id3" href="#id2" class="problematic">Target1__</a> <a id="id4" href="#id2" \
class="problematic">Target2__</a></p>
    <section class="system-messages">
        <h1>Docutils System Messages</h1>
        <div id="id2">
            <h1>System Message: ERROR/3 (&lt;string&gt; line ) <a href="#id3">id3</a> \
<a href="#id4">id4</a></h1>
            <p>Anonymous hyperlink mismatch: 2 references but 1 targets. \
See "backrefs" attribute for IDs.</p>
        </div>
    </section>
''',
    'part': 'body',
    'error': '<string>:: (ERROR/3) Anonymous hyperlink mismatch: 2 references but 1 targets.\n'
             'See "backrefs" attribute for IDs.\n',
}

problematic = {
    'rst': '''[2]_

.. [#] footnote''',
    'out': '''
    <p><a id="id4" href="#id3" class="problematic">[2]_</a></p>
    <table id="id2" class="footnote">
        <tbody>
            <tr>
                <th>1</th>
                <td>footnote</td>
            </tr>
        </tbody>
    </table>
    <section class="system-messages">
        <h1>Docutils System Messages</h1>
        <div id="id3">
            <h1>System Message: ERROR/3 (&lt;string&gt; line 1) <a href="#id4">id4</a></h1>
            <p>Unknown target name: "2".</p>
        </div>
    </section>
''',
    'part': 'body',
    'error': '<string>:1: (ERROR/3) Unknown target name: "2".\n',
}

paragraph_h = {
    'rst': 'Paragraph',
    'out': '\n    <meta charset="utf-8" />\n',
    'part': 'head',
}

metadata = {
    'rst': '.. title:: Foo Bar',
    'out': '<title>Foo Bar</title><meta charset="utf-8" />',
    'indent_output': False,
    'part': 'head',
}

html_tag_attr = {
    'rst': 'text',
    'out': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
</head>
<body>
    <p>text</p>
</body>
</html>''',
    'part': 'whole',
    'html_tag_attr': ['lang="en"', ]
}

stylesheet = {
    'rst': 'ordinary paragraph',
    'out': '''
    <meta charset="utf-8" />
    <link href="http://test.com/css/default.css" rel="stylesheet" />
    <link href="http://www.pronus.eng.br/css/standard.css" rel="stylesheet" />
''',
    'part': 'head',
    'stylesheet': ['http://test.com/css/default.css',
                   'http://www.pronus.eng.br/css/standard.css']
}

javascript = {
    'rst': 'ordinary paragraph',
    'out': '''
    <meta charset="utf-8" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
''',
    'script': [('https://ajax.googleapis.com/ajax/libs/jquery/'
                '1.7.2/jquery.min.js', None)],
    'part': 'head',
}

javascript_2 = {
    'rst': 'ordinary paragraph',
    'out': '''
    <meta charset="utf-8" />
    <script src="js/test1.js" defer="defer"></script>
    <script src="js/test2.js" async="async"></script>
    <script src="js/test3.js"></script>
''',
    'script': [('js/test1.js', 'defer'),
               ('js/test2.js', 'async'),
               ('js/test3.js', None), ],
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

meta_h2 = {
    'rst': meta_h['rst'],
    'out': '',
    'part': 'body',
}

template_text = {
    'rst': 'ordinary paragraph',
    'out': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <link href="css/default.css" rel="stylesheet" />
    <link href="css/pygments.css" rel="stylesheet" />
    <script src="http://code.jquery.com/jquery-latest.min.js"></script>
</head>
<body>
    <p>ordinary paragraph</p>
</body>
</html>''',
    'template': '''<!DOCTYPE html>
<html>
<head>{head}    <link href="css/default.css" rel="stylesheet" />
    <link href="css/pygments.css" rel="stylesheet" />
    <script src="http://code.jquery.com/jquery-latest.min.js"></script>
</head>
<body>{body}</body>
</html>''',
    'part': 'whole',
}


template_filename = {
    'rst': 'ordinary paragraph',
    'out': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <link href="css/default.css" rel="stylesheet" />
    <link href="css/pygments.css" rel="stylesheet" />
    <script src="http://code.jquery.com/jquery-latest.min.js"></script>
</head>
<body>
    <p>ordinary paragraph</p>
</body>
</html>''',
    'template': 'template.html',
    'part': 'whole',
}


comment_1 = {
    'rst': '.. this is a comment',
    'out': '''
    <!-- this is a comment -->
''',
    'part': 'body',
}

comment_2 = {
    'rst': '''
..
   this is a comment
   which continues at a new line
   and goes on
''',
    'out': '''
    <!-- this is a comment
which continues at a new line
and goes on -->
''',
    'part': 'body',
}

sphinx_code_block = {
    'rst': '''.. code-block:: python
    :class: small
    :linenos:

    def double(x):
        """
        useless comment
        """

        return 2 * x
''',
    'out': '''
    <table data-language="python" class="small"><tr><td><pre>1
2
3
4
5
6</pre></td><td><pre><span class="k">def</span> <span class="nf">double</span><span class="p">\
(</span><span class="n">x</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    useless comment</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> \
<span class="n">x</span></pre></td></tr></table>
''',
    'part': 'body',
}


include = {
    'rst': '''Test the inclusion of an external file:

.. include:: include_file.rst''',
    'out': '''
    <p>Test the inclusion of an external file:</p>
    <section id="hello-world">
        <h1>Hello, world!</h1>
        <p>Nothing else to say</p>
    </section>
''',
    'part': 'body',
}


define_directive_1 = {
    'rst': '''
.. define:: x
.. define:: y

.. ifdef:: x

    * x is defined

.. ifndef:: x

    x is not defined

.. undef:: y

.. ifndef:: y

    y is not defined''',
    'out': '''
    <ul>
        <li>x is defined</li>
    </ul>
    <p>y is not defined</p>
''',
    'part': 'body',
}


define_directive_2 = {
    'rst': '''
.. define:: x y

Some text

.. ifdef:: x

    x is defined

.. ifndef:: x

    x is not defined

.. ifdef:: y

    y is defined

.. ifndef:: y

    y is not defined

.. ifndef:: z

    z is not defined
''',
    'out': '''
    <p>Some text</p>
    <p>x is defined</p>
    <p>y is defined</p>
    <p>z is not defined</p>
''',
    'part': 'body',
}


ifdef_operator_missing = {
    'rst': '''
.. define:: x
.. define:: y
.. ifdef:: x y

    Error expected! Logical operator must be declared.
''',
    'out': '''
    <div>
        <h1>System Message: ERROR/3 (&lt;string&gt; line 4)</h1>
        <p>You must define an operator when more than one identifier is passed as argument.</p>
        <pre>.. ifdef:: x y

    Error expected! Logical operator must be declared.</pre>
    </div>
''',
    'part': 'body',
    'error': '<string>:4: (ERROR/3) You must define an operator when more than one identifier is passed as argument.\n',
}


ifndef_operator_missing = {
    'rst': '''
.. ifndef:: x y

    Error expected! Logical operator must be declared.''',
    'out': '''
    <div>
        <h1>System Message: ERROR/3 (&lt;string&gt; line 2)</h1>
        <p>You must define an operator when more than one identifier is passed as argument.</p>
        <pre>.. ifndef:: x y

    Error expected! Logical operator must be declared.</pre>
    </div>
''',
    'part': 'body',
    'error': '<string>:2: (ERROR/3) You must define an operator when more than one identifier is passed as argument.\n',
}


ifdef_operator_and_1 = {
    'rst': '''
.. define:: x
.. define:: y
.. ifdef:: x y
    :operator: and

    x and y defined!

.. ifndef:: x y
    :operator: and

    Error expected!''',
    'out': '''
    <p>x and y defined!</p>
''',
    'part': 'body',
}


ifdef_operator_and_2 = {
    'rst': '''
.. define:: x
.. ifdef:: x y
    :operator: and

    This line should not be shown.

.. ifndef:: x y
    :operator: and

    x defined but y is not.''',
    'out': '''
    <p>x defined but y is not.</p>
''',
    'part': 'body',
}


ifdef_operator_or_1 = {
    'rst': '''
.. define:: y
.. ifdef:: x y
    :operator: or

    y defined!

.. ifndef:: x y
    :operator: or

    Error expected since nor x nor y should be undefined.''',
    'out': '''
    <p>y defined!</p>
''',
    'part': 'body',
}


ifdef_operator_or_2 = {
    'rst': '''
.. ifdef:: x y
    :operator: or

    This line should not be shown.

.. ifndef:: x y
    :operator: or

    Ok. nor x nor y are defined.''',
    'out': '''
    <p>Ok. nor x nor y are defined.</p>
''',
    'part': 'body',
}


ifdef_include = {
    'rst': '''
.. define:: mercurial
.. ifdef:: mercurial

    .. include:: include_file.rst
''',
    'out': '''
    <h1>Hello, world!</h1>
    <p>Nothing else to say</p>
''',
    'part': 'body',
}


define_undefine_multiple_times = {
    'rst': '''
.. define:: x
.. define:: x
.. define:: y

.. undef:: x
.. undefine:: x

.. ifdef:: x y
    :operator: or

    x or y defined
''',
    'out': '''
    <p>x or y defined</p>
''',
    'part': 'body',
}


define_via_params = {
    'rst': '''
.. ifdef:: x

    x is defined
''',
    'out': '''
    <p>x is defined</p>
''',
    'part': 'body',
    'identifiers': ['x'],
}
