=============
Implementação
=============

O texto a seguir descreve o conhecimento coletado durante a implementação do rst2html5.
Certamente não está completo e talvez nem esteja exato,
mas pode ser de grande utilidade para outras pessoas
que desejem criar um novo conversor de rst para algum outro formato.


Docutils
========

O Docutils_ é um conjunto de ferramentas para processamento de documentação em texto simples
seguindo a marcação restructuredText_ (rst)
para outros formatos tais como HTML, PDF e Latex.

Seu funcionamento básico está descrito em http://docutils.sourceforge.net/docs/peps/pep-0258.html
Nas primeiras etapas do processo de tradução,
o documento rst é analisado e convertido para um formato intermediário chamado de *doctree*,
que então é passado ao conversor (``Writer``) para ser transformado na saída formatada desejada::

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

O doctree_ é uma estrutura hierárquica dos elementos que compõem o documento rst,
usada internamente pelos componentes do ``Docutils``.
Está definida no módulo ``docutils.nodes``.

O comando ``rst2pseudoxml`` gera uma representação textual da *doctree* que é muito útil
para visualizar o aninhamento dos elementos de um documento rst.
Essa informação foi de grande ajuda tanto para o *design* quanto para os testes do ``rst2html5``.

Dado o trecho de texto rst abaixo::

    Título
    ======

    Texto e mais texto

.. _trecho rst usado como exemplo:

A sua representação textual produzida pelo ``rst2pseudoxml`` é::

    <document ids="titulo" names="título" source="snippet.rst" title="Título">
        <title>
            Título
        <paragraph>
            Texto e mais texto


Writer
------

No *docutils*, o padrão é passar antes por um objeto da classe |Writer|,
A responsabilidade do ``Writer`` é coordenar a tradução para o formato final desejado.
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


NodeVisitor
-----------

A tradução é feita percorrendo cada nó da estrutura
e executando algum tipo de ação de acordo com o tipo e conteúdo do nó.
A travessia da árvore é coordenada pelo método :func:`docutils.snodes.Node.walkabout`
chamado a partir do nó-raiz da *doctree*.
Esse método recebe como parâmetro um objeto da classe |NodeVisitor|,
que corresponde à superclasse abstrata do padrão de projeto "Visitor" [GoF95]_.
Os métodos do "visitor" chamados durante a travessia são :func:`docutils.nodes.NodeVisitor.dispatch_visit` e
:func:`docutils.nodes.NodeVisitor.dispatch_departure`.
O primeiro é chamado assim que um nó começa a ser visitado;
o segundo é chamado logo antes de sair do nó:

.. automethod:: docutils.nodes.NodeVisitor.dispatch_visit

.. automethod:: docutils.nodes.NodeVisitor.dispatch_departure

Para a *doctree* do `trecho rst usado como exemplo`_, a sequência de chamadas correspondentes seria::

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

Cabe a uma subclasse de |NodeVisitor| implementar corretamente os métodos ``visit_...`` e ``depart_...``
para todos os tipos de nós existentes e fazer a tradução necessária para o formato desejado.


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