=========
rst2html5
=========

rst2html5 generates (X)HTML5 documents from standalone reStructuredText sources.
It is a complete rewrite of the docutils' rst2html and uses new HTML5 constructs as
<section> and <aside>.

Usage
=====

.. code-block:: bash

	$ rst2html5 [options] SOURCE

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


Examples
========

Consider the following rst snippet:

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


The html5 produced is clean and tidy:

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
    </head>
    <body>
        <a id="title"></a>
        <section>
            <h1>Title</h1>
            <p>Some text and a target to <a href="#title-2">Title 2</a>. <strong>strong emphasis</strong>:</p>
            <ul>
                <li>item 1</li>
                <li>item 2</li>
            </ul>
        </section>
        <a id="title-2"></a>
        <section>
            <h1>Title 2</h1>
            <pre>Inline markup is supported, e.g. <em>emphasis</em>, <strong>strong</strong>, <code>literal
    text</code>,
    <a id="hyperlink-targets">hyperlink targets</a>, and <a href="http://www.python.org/">references</a></pre>
        </section>
    </body>
    </html>

No stylesheets or classes are spread over the html5 by default. However:

#. Stylesheets and javascritps URLs or paths can be included through ``stylesheet`` and
   ``script`` options.

    .. parsed-literal::

        $ rst2html5 example.rst \\
        **--stylesheet** css/default.css \\
        **--stylesheet** css/special.css \\
        **--script** ``https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js``

    .. code-block:: html

        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <link href="css/default.css" rel="stylesheet" />
            <link href="css/special.css" rel="stylesheet" />
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
        ...


#. Script attributes ``defer`` and ``async``:

    .. parsed-literal::

        $ rst2html5 example.rst \\
        **--script** js/test1.js \\
        **--script-defer** js/test2.js \\
        **--script-async** js/test3.js

    .. code-block:: html

        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <script src="js/test1.js"></script>
            <script src="js/test2.js" defer="defer"></script>
            <script src="js/test3.js" async="async"></script>
        ...


#. Html tag attributes can be included through ``html-tag-attr`` option:

    .. parsed-literal::

        $ rst2html5 **--html-tag-attr** 'lang="pt-BR"' example.rst

    .. code-block:: html

        <!DOCTYPE html>
        <html lang="pt-BR">
        ...



#. Classes can be explicitly associated to rst elements (see ref__):

   .. code-block:: rst

        .. class:: special

        This is a "special" paragraph.

        .. class:: exceptional remarkable

        An Exceptional Section
        ======================

        This is an ordinary paragraph.

   which results in:

   .. parsed-literal::

        <p **class="special"**>This is a "special" paragraph.</p>
        <a id="an-exceptional-section"></a>
        <section **class="exceptional remarkable"**>
            <h1>An Exceptional Section</h1>
            <p>This is an ordinary paragraph.</p>
        </section>

Installation
============

.. code-block:: bash

    $ pip install rst2html5


Links
=====

* `Documentation`__
* `Project page at BitBucket`__


.. __: http://docutils.sourceforge.net/docs/ref/rst/directives.html#class
.. __: https://rst2html5.readthedocs.org/
.. __: https://bitbucket.org/andre_felipe_dias/rst2html5
