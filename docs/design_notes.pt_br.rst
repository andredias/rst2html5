=======================
Notas de Design (pt_BR)
=======================

O texto a seguir descreve o conhecimento coletado durante a implementação do rst2html5.
Certamente não está completo e talvez nem esteja exato,
mas pode ser de grande utilidade para outras pessoas
que desejem criar um novo tradutor de rst para algum outro formato.

.. note::

    O módulo ``rst2html5`` teve de ser renomeado para ``rst2html5_``
    devido a um conflito com o módulo de mesmo nome do ``docutils``.


Docutils
========

O Docutils_ é um conjunto de ferramentas para processamento de documentação em texto simples
em marcação restructuredText_ (rst)
para outros formatos tais como HTML, PDF e Latex.
Seu funcionamento básico está descrito em http://docutils.sourceforge.net/docs/peps/pep-0258.html

Nas primeiras etapas do processo de tradução,
o documento rst é analisado e convertido para um formato intermediário chamado de *doctree*,
que então é passado a um tradutor para ser transformado na saída formatada desejada::


                               Tradutor
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
Está definida no módulo :mod:`docutils.nodes`.

O comando/aplicativo ``rst2pseudoxml.py`` gera uma representação textual da *doctree*
que é muito útil para visualizar o aninhamento dos elementos de um documento rst.
Essa informação foi de grande ajuda tanto para o *design* quanto para os testes do :mod:`rst2html5_`.

Dado o trecho de texto rst abaixo:

.. code-block:: rst

    Título
    ======

    Texto e mais texto

A sua representação textual produzida pelo ``rst2pseudoxml`` é:

.. code-block:: xml

    <document ids="titulo" names="título" source="snippet.rst" title="Título">
        <title>
            Título
        <paragraph>
            Texto e mais texto


Tradutor, Writer e NodeVisitor
-------------------------------

Um tradutor é formado por duas partes: |Writer| e |NodeVisitor|.
A responsabilidade do |Writer| é preparar e coordenar a tradução feita pelo |NodeVisitor|.
O |NodeVisitor| é responsável por visitar cada nó da doctree e
executar a ação necessária de tradução para o formato desejado
de acordo com o tipo e conteúdo do nó.


.. note::

    Estas classes correspondem a uma variação do padrão de projeto "Visitor"
    conhecida como "Extrinsic Visitor" que é mais comumente usada em Python.
    Veja
    `The "Visitor Pattern", Revisited <http://peak.telecommunity.com/DevCenter/VisitorRevisited>`_.

.. important::

    Para desenvolver um novo tradutor para o *docutils*,
    é necessário especializar estas duas classes.


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
           |  visit_TIPO_NÓ  |          |  depart_TIPO_NÓ  |
           |                 |          |                  |
           +-----------------+          +------------------+

During doctree traversal through :func:`docutils.nodes.Node.walkabout`,
there are two |NodeVisitor| dispatch methods called:
:func:`~docutils.nodes.NodeVisitor.dispatch_visit` and
:func:`~docutils.nodes.NodeVisitor.dispatch_departure`.
The former is called early in the node visitation.
Then, all children nodes :func:`~docutils.nodes.Node.walkabout` are visited and
lastly the latter dispatch method is called.
Each dispatch method calls a specific
``visit_NODE_TYPE`` or ``depart_NODE_TYPE`` method
such as ``visit_paragraph`` or ``depart_title``,
that should be implemented by the |NodeVisitor| subclass object.

Durante a travessia da doctree feita através do método :func:`docutils.nodes.Node.walkabout`,
há dois métodos ``dispatch`` de |NodeVisitor| chamados:
:func:`~docutils.nodes.NodeVisitor.dispatch_visit` e
:func:`~docutils.nodes.NodeVisitor.dispatch_departure`.
O primeiro é chamado logo no começo da visitação do nó.
Em seguida, todos os nós-filho são visitados e, por último,
o método ``dispatch_departure`` é chamado.
Cada um desses métodos chama um método cujo nome segue o padrão
``visit_NODE_TYPE`` ou ``depart_NODE_TYPE``, tal como ``visit_paragraph`` ou ``depart_title``,
que deve ser implementado na subclasse de |NodeVisitor|.

Para a *doctree* do exemplo anterior,
a sequência de chamadas ``visit_...`` e ``depart_...`` seria::

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


.. note::

    São nos métodos ``visit_...`` e ``depart_...`` onde deve ser feita a tradução de cada nó
    de acordo com seu tipo e conteúdo.


rst2html5
=========

O módulo :mod:`rst2html5_` segue as recomendações originais e especializa as classes |Writer| e |NodeVisitor| através das classes
:class:`~rst2html5_.HTML5Writer` e :class:`~rst2html5_.HTML5Translator`.
:class:`rst2html5_.HTML5Translator` é a subclasse de |NodeVisitor|
criada para implementar todos os métodos ``visit_TIPO_NÓ`` e ``depart_TIPO_NÓ``
necessários para traduzir uma doctree em seu correspondente HTML5.
Isto é feito com ajuda de um outro objeto da classe auxiliar :class:`~rst2html5_.ElemStack`
que controla uma pilha de contextos para lidar com o aninhamento da visitação dos nós
da doctree e com a endentação::


                        rst2html5
                +-----------------------+
                |    +-------------+    |
     doctree ------->| HTML5Writer |------->  HTML5
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


A ação padrão de um método ``visit_TIPO_NÓ``
é iniciar um novo contexto para o nó sendo tratado:

.. literalinclude:: ../src/rst2html5_.py
    :pyobject: HTML5Translator.default_visit
    :linenos:
    :emphasize-lines: 12

A ação padrão no ``depart_TIPO_NÓ``
é criar o elemento HTML5 de acordo com o contexto salvo:

.. literalinclude:: ../src/rst2html5_.py
    :pyobject: HTML5Translator.default_departure
    :linenos:
    :emphasize-lines: 6-8


Nem todos os elementos rst seguem o este processamento.
O elemento ``Text``, por exemplo, é um nó folha e, por isso,
não requer a criação de um contexto específico.
Basta adicionar o texto correspondente ao elemento pai.

Outros tipos de nós têm um processamento comum
e podem compartilhar o mesmo método ``visit_`` e/ou ``depart_``.
Para aproveitar essas similaridades,
é feito um mapeamento entre o nó rst e os métodos correspondentes pelo dicionário ``rst_terms``:

.. literalinclude:: ../src/rst2html5_.py
    :language: python
    :linenos:
    :lines: 207-326


Construção de Tags HTML5
------------------------

A construção das *tags* do HTML5 é feita através do objeto :class:`~genshi.builder.tag`
do módulo :mod:`genshi.builder`.

.. topic:: Genshi Builder

    .. automodule:: genshi.builder



ElemStack
---------

Como a travessia da *doctree* não é feita por recursão,
é necessária uma estrutura auxiliar de pilha para armazenar os contextos prévios.
A classe auxiliar :class:`~rst2html5_.ElemStack` é uma pilha que registra os contextos
e controla o nível de endentação.

O comportamento do objeto ElemStack é ilustrado a seguir,
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



0. **Estado inicial**. A pilha de contexto está vazia::

    context = []


1. **visit_document**. Um novo contexto para ``document`` é criado::

    context = [ [] ]
                 \
                  document
                  context


2. **visit_title**. Um novo contexto é criado para o elemento ``title``::


                    title
                    context
                     /
    context = [ [], [] ]
                 \
                  document
                  context


3. **visit_Text**. O nó do tipo ``Text`` não precisa de um novo contexto pois é um nó-folha.
   O texto é simplesmente adicionado ao contexto do seu nó-pai::

                      title
                      context
                     /
    context = [ [], ['Title'] ]
                 \
                  document
                  context

4. **depart_Text**. Nenhuma ação é executada neste passo. A pilha permanece inalterada.

5. **depart_title**. Representa o fim do processamento do título.
   O contexto do título é extraído da pilha e combinado com uma tag ``h1``
   que é inserida no contexto do nó-pai (``document context``)::


    context = [ [tag.h1('Title')] ]
                 \
                  document
                  context


6. **visit_paragraph**. Um novo contexto é criado::

                                     paragraph
                                     context
                                    /
    context = [ [tag.h1('Title')], [] ]
                 \
                  document
                  context

7. **visit_Text**. Mais uma vez, o texto é adicionado ao contexto do nó-pai::

                                     paragraph
                                     context
                                    /
    context = [ [tag.h1('Title')], ['Text and more text'] ]
                 \
                  document
                  context

8. **depart_Text**. Nenhuma ação é necessária.

9. **depart_paragraph**. Segue o comportamento padrão, isto é,
   o contexto é combinado com a tag do elemento rst atual e então é inserida no contexto do nó-pai::


    context = [ [tag.h1('Title'), tag.p('Text and more text')] ]
                 \
                  document
                  context

10. **depart_document**. O nó da classe ``document`` não tem um correspondente em HTML5.
    Seu contexto é simplesmente combinado com o contexto mais geral que será o ``body``:

::

    context = [tag.h1('Title'), tag.p('Text e more text')]


.. _testes:

Testes
======

Os testes executados no módulo :mod:`rst2html5_.tests.test_html5writer` são baseados em geradores
(veja http://nose.readthedocs.org/en/latest/writing_tests.html#test-generators).
Os casos de teste são registrados no arquivo :file:`tests/cases.py`.
Cada caso de teste fica registrado em uma variável do tipo dicionário cujas entradas principais são:

:rst: Trecho de texto rst a ser transformado
:out: Saída esperada
:part: A qual parte da saída produzida pelo ``rst2html5_`` será usada na comparação com ``out``.
       As partes possíveis são: ``head``,  ``body`` e ``whole``.

Todas as demais entradas são consideradas opções de configuração do ``rst2html5_``.
Exemplos: ``indent_output``, ``script``, ``script-defer``, ``html-tag-attr`` e ``stylesheet``.

Em caso de falha no teste,
três arquivos auxiliares são gravados no diretório temporário (:file:`/tmp` no Linux):

#. :file:`NOME_CASO_TESTE.rst` com o trecho de texto rst do caso de teste;
#. :file:`NOME_CASO_TESTE.result` com resultado produzido pelo ``rst2html5_`` e
#. :file:`NOME_CASO_TESTE.expected` com o resultado esperado pelo caso de teste.

Em que ``NOME_CASO_TESTE`` é o nome da variável que contém o dicionário do caso de teste.

A partir desses arquivos é mais fácil comparar as diferenças::

    $ kdiff3 /tmp/NOME_CASO_TESTE.result /tmp/NOME_CASO_TESTE.expected

