======================
rst2html5 Design Notes
======================

The following documentation describes the knowledge collected durint rst2html5 implementation.
Probably, it isn't complete or even exact,
but it might be helpful to other people who want to create another rst converter.


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

The doctree_ is a hierarchical structure of the elements of a rst document.
It is defined at :mod:`docutils.nodes` and is used internally by Docutils components.

The command ``rst2pseudoxml.py`` produces a textual representation of a doctree
that is very useful to visualize the nesting of the elements of a rst document.
This information was of great help to both :mod:`rst2html5` design and tests.

Given the following rst snippet:

.. code-block:: rst

    Title
    =====

    Text and more text

The textual representation produced by ``rst2pseudoxml`` is:

.. code-block:: xml

    <document ids="title" names="title" source="snippet.rst" title="Title">
        <title>
            Title
        <paragraph>
            Text and more text


Translator, Writer e NodeVisitor
--------------------------------

A translator is comprised of two parts: a |Writer| and a |NodeVisitor|.
The |Writer| is responsible to prepare
and to coordinate the translation made by the |NodeVisitor|.
The |NodeVisitor| is used when visiting each doctree node and
it performs all actions needed to translate the node to the desired format
according to its type and content.

.. important::

    To develop a new docutils translator, one needs to specialize these two classes.

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
           +-----------------+          +------------------+
           |                 |          |                  |
           |   NodeVisitor   |          |   NodeVisitor    |
           | visit_NODE_TYPE |          | depart_NODE_TYPE |
           |                 |          |                  |
           +-----------------+          +------------------+


.. http://www.asciiflow.com/#Draw

During the doctree traversal through :func:`docutils.nodes.Node.walkabout`,
there are two |NodeVisitor| dispatch methods called:
:func:`~docutils.nodes.NodeVisitor.dispatch_visit` and
:func:`~docutils.nodes.NodeVisitor.dispatch_departure`.
The former is called early in the node visitation.
Then, all children nodes :func:`~docutils.nodes.Node.walkabout` are visited and
lastly the latter dispatch method is called.
Each dispatch method calls another method whose name follows the pattern
``visit_NODE_TYPE`` or ``depart_NODE_TYPE``
such as ``visit_paragraph`` or ``depart_title``,
that should be implemented by the |NodeVisitor| subclass object.


rst2html5
=========

In :mod:`rst2html5`,
|Writer| and |NodeVisitor| are specialized through
:class:`~rst2html5.HTML5Writer` and :class:`~rst2html5.HTML5Translator` classes.

:class:`rst2html5.HTML5Translator` is a |NodeVisitor| subclass
that implements all ``visit_NODE_TYPE`` and ``depart_NODE_TYPE`` methods
needed to translate a doctree to its HTML5 content.
The :class:`rst2html5.HTML5Translator` uses
an object of the:class:`~rst2html5.ElemStack` helper class that controls a context stack
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

The standard ``visit_NODE_TYPE`` action is initiate a new node context:

.. literalinclude:: ../rst2html5.py
    :pyobject: HTML5Translator.default_visit
    :linenos:
    :emphasize-lines: 15

The standard ``depart_NODE_TYPE`` action is to create the HTML5 element
according to the saved context:

.. literalinclude:: ../rst2html5.py
    :pyobject: HTML5Translator.default_departure
    :linenos:
    :emphasize-lines: 6-8

Not all rst elements follow this procedure.
The ``Text`` element, for example, is a leaf-node and thus doesn't need a specific context.
Other elements have a common processing and can share the same ``visit_`` and/or ``depart_`` method.
To take advantage of theses similarities,
the ``rst_terms`` dict maps a node type to a ``visit_`` and ``depart_`` methods:

.. literalinclude:: ../rst2html5.py
    :language: python
    :linenos:
    :lines: 207-326


HTML5 Tag Construction
----------------------

HTML5 Tags are constructed by the :class:`genshi.builder.tag` object.

.. topic:: Genshi Builder

    .. automodule:: genshi.builder


ElemStack
---------

For the previous doctree example,
the sequence of ``visit_...`` and ``depart_...`` calls is::

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

2. **visit_title**. A new context for ``title`` is pushed into the context stack::

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
   that is then inserted into the context of the title parent node (``document context``)::

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

The tests executed in :mod:`rst2html5.tests.test_html5writer` are bases on generators
(veja http://nose.readthedocs.org/en/latest/writing_tests.html#test-generators).
The test cases are in :file:`tests/cases.py`.
Each test case is a dictionary whose main keys are:

:rst: text snippet in rst format
:out: expected output
:part: specifies which part of ``rst2html5`` output will be compared to ``out``.
       Possible values are ``head``,  ``body`` or ``whole``.

All other keys are ``rst2html5`` configuration settings such as
``indent_output``, ``script``, ``script-defer``, ``html-tag-attr`` or ``stylesheet``.

When test fails,
three auxiliary files are saved on the temporary directory (:file:`/tmp`):

#. :file:`TEST_CASE.rst` com o trecho de texto rst do caso de teste;
#. :file:`TEST_CASE.result` com resultado produzido pelo ``rst2html5`` e
#. :file:`TEST_CASE.expected` com o resultado esperado pelo caso de teste.

Their differences can be easily visualized::

    $ kdiff3 /tmp/TEST_CASE.result /tmp/TEST_CASE.expected
