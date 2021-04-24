=========
rst2html5
=========

*rst2html5* generates (X)HTML5 documents from standalone reStructuredText sources.
It is a complete rewrite of the docutils' *rst2html* and uses new HTML5 constructs such as
:code:`<section>` and :code:`<aside>`.


Installation
============

.. code-block:: bash

    $ pip install rst2html5


Usage
=====

.. code-block:: bash

	$ rst2html5 [options] SOURCE [DEST]

Options:

--no-indent             Don't indent output
--stylesheet=<URL or path>
                        Specify a stylesheet URL to be included.
                        (This option can be used multiple times)
--script=<URL or path>  Specify a script URL to be included.
                        (This option can be used multiple times)
--script-defer=<URL or path>
                        Specify a script URL with a defer attribute
                        to be included in the output HTML file.
                        (This option can be used multiple times)
--script-async=<URL or path>
                        Specify a script URL with a async attribute
                        to be included in the output HTML file.
                        (This option can be used multiple times)
--html-tag-attr=<attribute>
                        Specify a html tag attribute.
                        (This option can be used multiple times)
--template=<filename or text>
                        Specify a filename or text to be used as the HTML5
                        output template. The template must have the {head} and
                        {body} placeholders. The "<html{html_attr}>"
                        placeholder is recommended.
--define=<identifier>   Define a case insensitive identifier to be used with
                        ifdef and ifndef directives. There is no value
                        associated with an identifier. (This option can be
                        used multiple times)


If ``DEST`` is not provided, the output is send to ``stdout``.


Example
-------

Consider a file called ``example.rst`` that contains:

.. code-block:: rst

    Title
    =====

    Some text and a target to `Title 2`_. **strong emphasis**:

    * item 1
    * item 2

    Title 2
    =======

    .. parsed-literal::

        Inline markup is supported, e.g. *emphasis*, **strong**, ``literal
        text``,
        _`hyperlink targets`, and `references <http://www.python.org/>`_


The command to produce an ``example.html`` output file is::

    $ rst2html5 example.rst example.html


The HTML5 produced is clean and tidy:

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
        <section id="title">
            <h1>Title</h1>
            <p>Some text and a target to <a href="#title-2">Title 2</a>. <strong>strong emphasis</strong>:</p>
            <ul>
                <li>item 1</li>
                <li>item 2</li>
            </ul>
        </section>
        <section id="title-2">
            <h1>Title 2</h1>
            <pre>Inline markup is supported, e.g. <em>emphasis</em>, <strong>strong</strong>, <code>literal
    text</code>,
    <a id="hyperlink-targets">hyperlink targets</a>, and <a href="http://www.python.org/">references</a></pre>
        </section>
    </body>
    </html>


Stylesheets and Scripts
-----------------------

No stylesheets or scripts are spread over the HTML5 by default.
However stylesheets and javascripts URLs or paths can be included through ``stylesheet`` and ``script`` options:

.. parsed-literal::

    $ rst2html5 example.rst \\
    **--stylesheet** https://example.com/css/default.css \\
    **--stylesheet-inline** css/simple.css \\
    **--script** ``https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js``
    **--script-defer** ``js/test1.js``
    **--script-async** ``js/test2.js``


.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://example.com/css/default.css" />
        <style>h1 {font-size: 20em}
    img.icon {
        width: 48px;
        height: 48px;
    }
    h2 {color: red}
    </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
        <script src="js/test1.js" defer="defer"></script>
        <script src="js/test2.js" async="async"></script>
    </head>
    ...


HTML tag attributes can be included through ``html-tag-attr`` option:

.. parsed-literal::

    $ rst2html5 **--html-tag-attr** 'lang="pt-BR"' example.rst

.. code-block:: html

    <!DOCTYPE html>
    <html lang="pt-BR">
    ...


Templates
---------

Custom HTML5 template via the :literal:`--template` option. Example:

.. parsed-literal::

    $ template='<!DOCTYPE html>
    <html{html_attr}>
    <head>{head}    <!-- custom links and scripts -->
        <link href="css/default.css" rel="stylesheet" />
        <link href="css/pygments.css" rel="stylesheet" />
        <script src="http\://code.jquery.com/jquery-latest.min.js"></script>
    </head>
    <body>{body}</body>
    </html>'

    $ echo 'one line' > example.rst

    $ rst2html5 **--template "$template"** example.rst


.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <!-- custom links and scripts -->
        <link href="css/default.css" rel="stylesheet" />
        <link href="css/pygments.css" rel="stylesheet" />
        <script src="http://code.jquery.com/jquery-latest.min.js"></script>
    </head>
    <body>
        <p>one line</p>
    </body>
    </html>


New Directives
==============

``define``, ``undef``, ``ifdef`` and ``ifndef``
-----------------------------------------------

:code:`rst2html5` provides some new directives: ``define``, ``undef``, ``ifdef`` and ``ifndef``,
similar to those used in C++.
They allow to conditionally include (or not) some rst snippets:

.. code-block:: rst

    .. ifdef:: x

        this line will be included if 'x' was previously defined


In case of you check two or more identifiers,
there must be an operator (``[and | or]``) defined:

.. code-block:: rst

    .. ifdef:: x y z
        :operator: or

        This line will be included only if 'x', 'y' or 'z' is defined.


``stylesheet`` and ``script``
-----------------------------

From rst2html5 1.9, you can include stylesheets and scripts via directives inside a reStructuredText text:

.. code-block:: rst

    Just an ordinary paragraph.

    .. stylesheet:: css/default.css
    .. stylesheet:: https://pronus.io/css/standard.css

    .. script:: http://code.jquery.com/jquery-latest.min.js
    .. script:: slide.js
        :defer:

    .. script:: test/animations.js
        :async:

    Another paragraph


.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <link href="css/default.css" rel="stylesheet" />
        <link href="https://pronus.io/css/standard.css" rel="stylesheet" />
        <script src="http://code.jquery.com/jquery-latest.min.js"></script>
        <script src="slide.js" defer="defer"></script>
        <script src="test/animations.js" async="async"></script>
    </head>
    <body>
        <p>Just an ordinary paragraph.</p>
        <p>Another paragraph</p>
    </body>
    </html>


``template``
------------

There also is a :code:`template` directive. The usage is:

.. code-block:: rst

    .. template:: filename

    or

    .. template::

        template content here.


New Roles
=========

``:abbr:``
----------

From `MDN Web Docs <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr>`_:

    The HTML Abbreviation element (:code:`<abbr>`) represents an abbreviation or acronym;
    the optional title attribute can provide an expansion or description for the abbreviation.
    If present, title must contain this full description and nothing else.

To create an abbreviation in ``rst2html5`` use the ``:abbr:`` role:

.. code:: rst

    * :abbr:`SPA (Single-Page Application)`
    * :abbr:`ASGI (Asynchronous Server Gateway Interface)` is a spiritual successor to :abbr:`WSGI`
    * :abbr:`WSGI (Web Server Gateway Interface)`


Resulting in:

.. code:: html

    <ul>
        <li>
            <abbr title="Single-Page Application">SPA</abbr>
        </li>
        <li>
            <abbr title="Asynchronous Server Gateway Interface">ASGI</abbr>
        is a spiritual successor to
            <abbr>WSGI</abbr>
        </li>
        <li>
            <abbr title="Web Server Gateway Interface">WSGI</abbr>
        </li>
    </ul>


Note that if the abbreviation follows the pattern ``ABBR (Description for the abbreviation)``,
the description is extracted and becomes the ``title``.


How To Use rst2html5 Programmatically
=====================================

You should use ``rst2html5.HTML5Writer`` with one of the ``publish_*` methods available in ``docutils.core``.
In the case that the input and output will be in memory,
``publish_parts`` is the best fit:

.. code:: python

    from docutils.core import publish_parts

    from rst2html5 import HTML5Writer

    text = r'''The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.

    .. math::

        \frac{ \sum_{t=0}^{N}f(t,k) }{N}
    '''

    body = publish_parts(writer=HTML5Writer(), source=text)['body']
    print(body)


Resulting in:

.. code:: html

    <p>The area of a circle is
        <span class="math">\(A_\text{c} = (\pi/4) d^2\)</span>
    .</p>
    <div class="math">\(\frac{ \sum_{t=0}^{N}f(t,k) }{N}\)</div>


.. attention::

    Version 2.0 renames the module ``rst2html5_`` back to ``rst2html5``
    since the conflict with docutils installation is solved.
    Importing ``rst2html5_.HTML5Writer`` still works though.
    See the section "**Workaround to Conflicts with Docutils**"
    on ``docs/design_notes.rst`` for more information.


See also: `The Docutils Publisher <https://docutils.sourceforge.io/docs/api/publisher.html>`_


Links
=====

* `Documentation <https://rst2html5.readthedocs.org/>`_
* `Project page at Heptapod <https://foss.heptapod.net/doc-utils/rst2html5>`_
