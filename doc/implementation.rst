========================
rst2html5 Implementation
========================

The following documentation describes the knowledge collected durint rst2html5 implementation.
Certainly, it isn't complete or even exact,
but it might be helpful to other people who want to create another rst converter.


Docutils, doctree, rst2pseudoxml and NodeVisitor
================================================

The docutils_ is a a set of tools for processing restructuredText_ (rst) documentation
into useful formats, such as HTML, PDF, LaTeX, man-pages, open-document or XML.
At first stages of the translation,
the ``rst`` document is analyzed and converted to an intermediary format called *doctree*,
that is sent to the converter (``Writer``) to be transformed into the desired output::

                +------------+
   doctree ---->| Translator |----> output
                +------------+

Doctree
-------

The doctree_ is an internal hierarchical representation of the elements of the rst document.
The command ``rst2pseudoxml`` produces a textual representation of the *doctree*
which is useful to visualize the elements and their nesting.
This information has been very helpful to *design* and tests of the ``rst2html5``.

Given the rst snippet below:

.. code-block:: rst

    Title
    =====

    Text text text

.. _trecho rst usado como exemplo:

The textual representation produced by ``rst2pseudoxml`` is::

    <document ids="title" names="title" source="snippet.rst" title="Title">
        <title>
            Title
        <paragraph>
            Text text text


NodeVisitor
-----------

The translation is done by traversing each doctree node
and performing some kind of action according to the type and content of the node.
The tree traversal is coordinated by the method :func:`docutils.nodes.Node.walkabout`
called from the root node of the doctree.
This method receives a |NodeVisitor| object as parameter,
which corresponds to the abstract superclass in the "Visitor" design pattern [GoF95]_.
The "visitor" methods called during the traversal are
:func:`docutils.nodes.NodeVisitor.dispatch_visit` and
:func:`docutils.nodes.NodeVisitor.dispatch_departure`.
The former is called at the beginning of the visit,
and the latter at the end, just before leaving the node:

.. automethod:: docutils.nodes.NodeVisitor.dispatch_visit

.. automethod:: docutils.nodes.NodeVisitor.dispatch_departure

The sequence of calls for the doctree presented earlier is::

    visit_document
        visit_title
            visit_Text
            depart_Text
        depart_title
        visit_paragraph
            visit_Text
            depart_Text
        depart_paragraph
    depart_document

It is up to a |NodeVisitor| subclass to implement correctly the ``visit_...`` and ``depart_...``
methods for all types of existing nodes.


Writer
------

A *doctree* não costuma ser enviada diretamente ao |NodeVisitor|.
No *docutils*, o padrão é passar antes por um objeto da classe |Writer|,
cuja responsabilidade é coordenar a tradução para o formato final desejado.
A chamada ao método :func:`~docutils.nodes.Node.walkabout` acontece no
método :func:`docutils.writers.Writer.translate`:

.. automethod:: docutils.writers.Writer.translate

A relação formada é apresentada na ilustração abaixo::


                +-------------------+
                |    +---------+    |
    doctree -------->|  Writer |-------> output
                |    +----+----+    |
                |         |         |
                |         |         |
                |  +------+------+  |
                |  | NodeVisitor |  |
                |  +-------------+  |
                +-------------------+

Portanto, para desenvolver um novo script para o *docutils*,
o modo mais simples é através de uma especialização dessas duas classes.

rst2html5
=========

O módulo :mod:`rst2html5` segue as recomendações originais e especializa as classes |Writer| e |NodeVisitor|::

                        rst2html5
                +-----------------------+
                |    +-------------+    |
     doctree ------->| HTML5Writer |------->  HTML5
                |    +------+------+    |
                |           |           |
                |           |           |
                |  +--------+--------+  |
                |  | HTML5Translator |  |
                |  +-----------------+  |
                +-----------------------+

HTML5Writer
-----------

:class:`rst2html5.HTML5Writer` é a subclasse de :class:`~docutils.writers.Writer`
criada para coordenar a tradução da *doctree* para HTML5.
Conforme o padrão recomendado,
o método :func:`~rst2html5.HTML5Writer.translate` delega a tradução para um objeto :class:`~rst2html5.HTML5Translator` (linhas 2 e 3):

.. literalinclude:: ../rst2html5.py
    :pyobject: HTML5Writer.translate
    :linenos:
    :emphasize-lines: 2, 3


HTML5Translator
---------------

:class:`rst2html5.HTML5Translator` é a subclasse de ``NodeVisitor``
criada para implementar os métodos ``visit_<nome da classe do nó>`` e ``depart_<nome da classe do nó>``
necessários para traduzir um elemento ``rst`` em seu correspondente em HTML5.
Conta ainda com ajuda de um outro objeto da classe auxiliar ElemStack_
que controla uma pilha de contextos para lidar com o aninhamento dos nós.

A ação padrão de um método ``visit_<nome da classe do nó>`` é iniciar um novo contexto para o nó sendo tratado.
A ação padrão no ``depart_<nome da classe do nó>`` é criar o elemento HTML5 de acordo com o contexto salvo:

.. automethod:: rst2html5.HTML5Translator.default_visit

.. automethod:: rst2html5.HTML5Translator.default_departure

Nem todos os elementos rst seguem o este processamento.
O elemento ``Text``, por exemplo, é um nó folha e, por isso,
não requer a criação de um contexto específico.
Basta adicionar o texto correspondente ao elemento pai (veja :func:`~rst2html5.HTML5Translator.visit_Text`).

Outros nós têm um processamento comum e podem compartilhar o mesmo método ``visit_`` e/ou ``depart_``.
Para aproveitar essas similaridades,
é feito um mapeamento entre o nó rst e os métodos correspondentes pelo dicionário ``rst_terms``,
que registra também qual a *tag* padrão para o elemento,
se o nome do elemento rst deve aparecer como um atributo ``class`` no HTML5 (``class="nome_da_classe_do_nó"``)
e se o elemento deve ou não ser indentado na saída formatada:

A construção das *tags* do HTML5 é feita através do objeto ``tag`` do módulo :mod:`genshi.builder`.
Veja a própria documentação do módulo para mais informações.

.. _ElemStack:

ElemStack
---------

A finalidade desta classe é registrar os contextos de cada elemento sendo processado
e controlar o nível de endentação.
Na maioria dos casos,
a tradução de um elemento rst só pode ser concluída quando seus elementos internos forem processados.
Como a travessia da *doctree* não é feita por recursão,
é necessária uma estrutura auxiliar de pilha para armazenar os contextos prévios.

O comportamento de um objeto ElemStack é ilustrado a seguir,
através da visualização da estrutura de pilha durante a análise do trecho rst
que vem sendo usado como exemplo.

As chamadas ``visit_...`` e ``depart_...`` acontecerão na seguinte ordem::

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



0. **Estado inicial**. A pilha (``stack``) está vazia::

    stack = []


1. **visit_document**. É criado contexto para ``document``, mantido por uma nova lista em ``stack``::

    stack = [ [] ]
               \
                document
                context

2. **visit_title**. Um novo contexto é criado para o elemento ``title``::

                    title
                    context
                   /
    stack = [ [], [] ]
               \
                document
                context


3. **visit_Text**. O nó do tipo ``Text`` não precisa de um novo contexto pois é um nó-folha.
   O texto é simplesmente adicionado ao contexto do seu nó-pai::

                    title
                    context
                   /
    stack = [ [], ['Título'] ]
               \
                document
                context

4. **depart_Text**. Nenhuma ação é executada neste passo. A pilha permanece inalterada.

5. **depart_title**. Representa o fim do processamento do título.
   O contexto do título é extraído da pilha e combinado com uma tag ``h1``
   que é inserida no contexto do nó-pai (``document``)::

    stack = [ [<h1>] ]
               \
                document
                context

6. **visit_paragraph**. Um novo contexto é criado::

                        paragraph
                        context
                       /
    stack = [ [<h1>], [] ]
               \
                document
                context

7. **visit_Text**. Mais uma vez, o texto é adicionado ao contexto do nó-pai::

                        paragraph
                        context
                       /
    stack = [ [<h1>], ['Texto e mais texto'] ]
               \
                document
                context

8. **depart_Text**. Nenhuma ação é necessária.

9. **depart_paragraph**. Segue o comportamento padrão, isto é,
   o contexto é combinado com a tag do elemento rst atual e então é inserida no contexto do nó-pai::

    stack = [ [<h1>, <p>] ]
               \
                document
                context

10. **depart_document**. O nó da classe ``document`` não tem um correspondente em HTML5.
    Seu contexto é simplesmente combinado com o contexto mais geral que será o ``body``::

        stack = [<h1>, <p>]




.. |NodeVisitor| replace:: :class:`docutils.nodes.NodeVisitor`
.. |Writer| replace::  :class:`~docutils.writers.Writer`
.. |HTML5Translator| replace:: :class:`rst2html5.HTML5Translator`

.. [GoF95] Gamma, Helm, Johnson, Vlissides. *Design Patterns: Elements of
   Reusable Object-Oriented Software*. Addison-Wesley, Reading, MA, USA,
   1995.