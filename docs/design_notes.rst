======================
rst2html5 Design Notes
======================

The following documentation describes the knowledge collected during ``rst2html5`` implementation.
It might be helpful to other people who want to contribute to the project or create another rst converter.


Docutils
========

Docutils_ is a set of tools for processing plaintext documentation in restructuredText_ markup (rst)
into other formats such as  HTML, PDF and Latex.
Its documents design issues and implementation details are described at
http://docutils.sourceforge.net/docs/peps/pep-0258.html

In the early stages of the translation process,
the rst document is analyzed and transformed into an intermediary format called *doctree*
which is then passed to a translator to be transformed into the desired formatted output::


                              Translator
                        +-------------------+
                        |    +---------+    |
       ---> doctree -------->|  Writer |-------> output
                        |    +----+----+    |
                        |         |         |
                        |         |         |
                        |  +------+------+  |
                        |  | NodeVisitor |  |
                        |  +-------------+  |
                        +-------------------+


Doctree
-------

The doctree_ is a hierarchical structure of the elements of a ``rst`` document.
It is defined at ``docutils.nodes`` and is used internally by Docutils components.

The command :command:`rst2pseudoxml.py` produces a textual representation of a doctree
that is very useful to visualize the nesting of the elements of a ``rst`` document.
This information was of great help for both ``rst2html5`` design and tests.

Given the following ``rst`` snippet:

.. code-block:: rst

    Title
    =====

    Text and more text

The textual representation produced by :command:`rst2pseudoxml.py` is:

.. code-block:: xml

    <document ids="title" names="title" source="snippet.rst" title="Title">
        <title>
            Title
        <paragraph>
            Text and more text


Translator, Writer and NodeVisitor
----------------------------------

A translator is comprised of two parts: a |Writer| and a |NodeVisitor|.
The |Writer| is responsible to prepare and coordinate the translation made by the |NodeVisitor|.
The |NodeVisitor| is used for visiting each doctree node and
it performs all actions needed to translate the node to the desired format
according to its type and content.

.. important::

    To develop a new docutils translator, you need to specialize these two classes.

.. note::

    Those classes correspond to a variation of the Visitor pattern,
    called "Extrinsic Visitor" that is more commonly used in Python.
    See
    `The "Visitor Pattern", Revisited <http://peak.telecommunity.com/DevCenter/VisitorRevisited>`_.

.. seealso::

    `Double Dispatch and the "Visitor" Pattern <http://peak.telecommunity.com/protocol_ref/dispatch-example.html>`_.


::


                         +-------------+
                         |             |
                         |    Writer   |
                         |  translate  |
                         |             |
                         +------+------+
                                |
                                |    +---------------------------+
                                |    |                           |
                                v    v                           |
                           +------------+                        |
                           |            |                        |
                           |    Node    |                        |
                           |  walkabout |                        |
                           |            |                        |
                           +--+---+---+-+                        |
                              |   |   |                          |
                    +---------+   |   +----------+               |
                    |             |              |               |
                    v             |              v               |
           +----------------+     |    +--------------------+    |
           |                |     |    |                    |    |
           |  NodeVisitor   |     |    |    NodeVisitor     |    |
           | dispatch_visit |     |    | dispatch_departure |    |
           |                |     |    |                    |    |
           +--------+-------+     |    +---------+----------+    |
                    |             |              |               |
                    |             +--------------|---------------+
                    |                            |
                    v                            v
          +-------------------+        +--------------------+
          |                   |        |                    |
          |   NodeVisitor     |        |   NodeVisitor      |
          | visit_<NODE_TYPE> |        | depart_<NODE_TYPE> |
          |                   |        |                    |
          +-------------------+        +--------------------+


.. http://www.asciiflow.com/#Draw

During the doctree traversal through :func:`docutils.nodes.Node.walkabout`,
there are two |NodeVisitor| dispatch methods called:
:func:`~docutils.nodes.NodeVisitor.dispatch_visit` and
:func:`~docutils.nodes.NodeVisitor.dispatch_departure`.
The former is called early in the node visitation.
Then, all children nodes :func:`~docutils.nodes.Node.walkabout` are visited, and lastly,
the latter dispatch method is called.
Each dispatch method calls another method whose name follows the pattern
``visit_<NODE_TYPE>`` or ``depart_<NODE_TYPE>``
such as ``visit_paragraph`` or ``depart_title``,
that should be implemented by the |NodeVisitor| subclass object.



rst2html5
=========

In :mod:`rst2html5`,
|Writer| and |NodeVisitor| are specialized through
:class:`~rst2html5.HTML5Writer` and :class:`~rst2html5.HTML5Translator` classes.

:class:`rst2html5.HTML5Translator` is a |NodeVisitor| subclass
that implements all ``visit_<NODE_TYPE>`` and ``depart_<NODE_TYPE>`` methods
needed to translate a doctree to its HTML5 content.
The :class:`rst2html5.HTML5Translator` uses
an object of the :class:`~rst2html5.ElemStack` helper class that controls a context stack
to handle indentation and the nesting of the doctree traversal::


                        rst2html5
                +-----------------------+
                |    +-------------+    |
     doctree ---|--->| HTML5Writer |----|-->  HTML5
                |    +------+------+    |
                |           |           |
                |           |           |
                |  +--------+--------+  |
                |  | HTML5Translator |  |
                |  +--------+--------+  |
                |           |           |
                |           |           |
                |     +-----+-----+     |
                |     | ElemStack |     |
                |     +-----------+     |
                +-----------------------+

The standard ``visit_<NODE_TYPE>`` action is called ``default_visit`` and it initiates a new element context:

.. literalinclude:: ../rst2html5/__init__.py
    :pyobject: HTML5Translator.default_visit
    :emphasize-lines: 12

The standard ``depart_<NODE_TYPE>`` action is ``default_departure`` and it creates the HTML5 element
corresponding to the saved context:

.. literalinclude:: ../rst2html5/__init__.py
    :pyobject: HTML5Translator.default_departure
    :emphasize-lines: 6-8

Not all rst elements follow this procedure.
The ``Text`` element, for example, is a leaf-node and thus doesn't need a specific context.
Other elements have a common processing and can share the same ``visit_`` and/or ``depart_`` method.
To take advantage of theses similarities,
the ``rst_terms`` dict maps a node type to its ``visit_`` and ``depart_`` methods:

.. literalinclude:: ../rst2html5/__init__.py
    :pyobject: HTML5Translator
    :lines: 3-141

where ``dv`` is ``default_visit`` and ``dp`` means ``default_departure``.


HTML5 Tag Construction
----------------------

HTML5 Tags are constructed by the :class:`genshi.builder.tag` object.



ElemStack
---------

For the previous doctree example,
the sequence of ``visit_...`` and ``depart_...`` calls is this::

    1. visit_document
        2. visit_title
            3. visit_Text
            4. depart_Text
        5. depart_title
        6. visit_paragraph
            7. visit_Text
            8. depart_Text
        9. depart_paragraph
    10. depart_document

For this sequence,
the behavior of a ElemStack context object is:


0. **Initial State**. The context stack is empty::

    context = []


1. **visit_document**. A new context for ``document`` is reserved::

    context = [ [] ]
                 \
                  document
                  context

2. **visit_title**. A new context for *title* is pushed into the context stack::

                    title
                    context
                     /
    context = [ [], [] ]
                 \
                  document
                  context


3. **visit_Text**. A ``Text`` node doesn't need a new context because it is a leaf-node.
Its text is simply added to the context of its parent node::

                      title
                      context
                     /
    context = [ [], ['Title'] ]
                 \
                  document
                  context

4. **depart_Text**. No action performed. The context stack remains the same.

5. **depart_title**. This is the end of the title processing.
   The title context is popped from the context stack to form an ``h1`` tag
   that is then inserted into the context of the title parent node (*document context*)::

    context = [ [tag.h1('Title')] ]
                 \
                  document
                  context

6. **visit_paragraph**. A new context is added::

                                     paragraph
                                     context
                                    /
    context = [ [tag.h1('Title')], [] ]
                 \
                  document
                  context

7. **visit_Text**. Again, the text is inserted into its parent's node context::

                                     paragraph
                                     context
                                    /
    context = [ [tag.h1('Title')], ['Text and more text'] ]
                 \
                  document
                  context

8. **depart_Text**. No action performed.

9. **depart_paragraph**. Follows the standard procedure
   where the current context is popped and form a new tag that is appended into
   the context of the parent node::

    context = [ [tag.h1('Title'), tag.p('Text and more text')] ]
                 \
                  document
                  context

10. **depart_document**. The document node doesn't have an HTML tag.
    Its context is simply combined to the outer context to form the body of the HTML5 document::

        context = [tag.h1('Title'), tag.p('Text and more text')]


.. _tests:

rst2html5 Tests
===============

The test cases are located at :file:`tests/cases.py` and
each test case is a dictionary whose main keys are:

:rst: text snippet in rst format
:out: expected output
:part: specifies which part of **rst2html5** output will be compared to **out**.
       Possible values are **head**,  **body** or **whole**.

Other possible keys are ``rst2html5`` configuration settings such as
*indent_output*, *script*, *script-defer*, *html-tag-attr* or *stylesheet*.

When a test fails,
three auxiliary files are created on the default temporary directory (:file:`/tmp`):

#. :file:`TEST_CASE_NAME.rst`  contains the rst snippet of the test case.;
#. :file:`TEST_CASE_NAME.result` contais the result produced by **rst2html5** and
#. :file:`TEST_CASE_NAME.expected` contains the expected result.

Their differences can be easily visualized by a diff tool::

    $ kdiff3 /tmp/TEST_CASE_NAME.result /tmp/TEST_CASE_NAME.expected


.. _workaround:

Workaround to Conflicts with ``Docutils``
=========================================

``rst2html5`` package installation should make it possible to use it via command line
and also being imported in other projects using ``rst2html5``.
For example, to use it via command line:

.. code:: bash

    $ rst2html5 example.rst example.html


And programmatically from another project:

.. code:: python

    from rst2html5 import HTML5Writer

    ...


The problem is that after ``0.13.1``,
``docutils`` installation creates two scripts called ``rst2html5``
*and* ``rst2html5.py`` in ``<venv>/bin``,
where ``<venv>`` is the installation path of the virtual environment being used.
Both do the same.

Since it is not possible to delete a script from another package,
``rst2html5`` package installation overwrites both,
but ``rst2html5.py`` still causes problems.
When importing ``rst2html5`` from one of those scripts,
Python reaches ``<venv>/bin/rst2html5.py``
instead of ``<venv>/lib/<python_version>/site-packages/rst2html5``
because the former comes first in ``sys.path``
**during the execution, in a virtual environment**.

A typical ``sys.path`` is:

.. code:: python

    [
        '/tmp/py39/bin',
        '/usr/lib/python39.zip',
        '/usr/lib/python3.9',
        '/usr/lib/python3.9/lib-dynload',
        '/tmp/py39/lib/python3.9/site-packages'
    ]

where ``/tmp/py39`` is the path of the virtual environment,
and ``python3.9`` is the current Python version.

.. note::

    The ``sys.path`` information from the command line is different
    from the one inside a running script.
    To get the real value,
    you must manually insert a breakpoint or print it from a installed script.

From ``1.9.2 <= rst2html5 < 2.0``,
the immediate solution was to rename the module from ``rst2html5`` to ``rs2html5_``,
so that importing would skip ``<venv>/bin/rst2html5.py``
and find the right module at ``<venv>/lib/<python_version>/site-packages``.

Version ``2.0`` implements a more elegant solution for the problem
that allows both the script *and* the module to be named ``rst2html5``.
The script ``<venv>/bin/rst2html5`` still imports ``rst2html5_``
but instead of reaching a module, the importing hits a file called ``rst2html5_.py``
that modifies ``sys.path`` and only then import the module ``rst2html5``::

                    <venv>/bin              <venv>/lib/<python_version>/site-packages


    before 2.0:     rst2html5    ----->     rst2html5_/
                    (import rst2html5_)


    2.0 onwards:    rst2html5    ----->     rst2html5_.py     -------->   rst2html5/
                    (import rst2html5_)     (modifies sys.path
                                             and then import rst2html5)



``<venv>/bin/rst2html5`` is generated automatically during the package installation,
and contains something very similar to this:

.. code:: python

    #!/<venv>/bin/python
    from rst2html5_ import main

    if __name__ == '__main__':
        main()


The intermediary file ``rst2html5_.py`` is shown below:

.. literalinclude:: ../rst2html5_.py
    :lines: 7-
    :name: rst2html5_.py


The package installation is configured in the file ``pyproject.toml``:

.. code-block:: toml

    [tool.poetry]
    ...
    packages = [
        {include = "rst2html5"}
    ]
    include = ["rst2html5_.py"]

    [tool.poetry.scripts]
    rst2html5 = "rst2html5_:main"  # overwrites docutils' rst2html5
    ...


.. attention::

    It is very likely that projects that use ``rst2html5`` prior to 2.0 *won't* need to change their imports
    because ``rst2html5_.HTML5Writer`` is still reachable through the new ``rst2html5_.py`` file.
    However, they're advised to do so.
