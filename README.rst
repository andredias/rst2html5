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
--template=<filename or text>
                        Specify a filename or text to be used as the HTML5
                        output template. The template must have the {head} and
                        {body} placeholders. The "<html{html_attr}>"
                        placeholder is recommended.
--define=<identifier>   Define a case insensitive identifier to be used with
                        ifdef and ifndef directives. There is no value
                        associated with an identifier. (This option can be
                        used multiple times)



Example
-------

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

No stylesheets or classes are spread over the html5 by default.
However stylesheets and javascripts URLs or paths can be included through ``stylesheet`` and ``script`` options:

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

Additional scripts can be included in the result
using options ``--script``, ``--script-defer`` or ``--script-async``:

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


Html tag attributes can be included through ``html-tag-attr`` option:

.. parsed-literal::

    $ rst2html5 **--html-tag-attr** 'lang="pt-BR"' example.rst

.. code-block:: html

    <!DOCTYPE html>
    <html lang="pt-BR">
    ...


Templates
---------

Custom html5 template via the :literal:`--template` option. Example:

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
--------------

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



Links
=====

* `Documentation <https://rst2html5.readthedocs.org/>`_
* `Project page at BitBucket <https://bitbucket.org/andre_felipe_dias/rst2html5>`_
