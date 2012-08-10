==============
Implementation
==============

The following text describes the knowledge

O texto a seguir descreve o conhecimento coletado durante a implementação do rst2html5.
Certamente não está completo e talvez nem esteja exato,
mas pode ser de grande utilidade para outras pessoas que desejem criar um novo conversor de rst para algum outro formato.

Doctree, rst2pseudoxml e NodeVisitor
====================================

O primeiro passo é entender o que é o Docutils e como ele funciona.

O Docutils foi projetado inicialmente para documentação de projetos.

Os módulos básicos são apresentados no `PEP 0258`_.
Para construir o rst2html5, o importante foi saber que::



                +-----------+
   doctree ---->| Conversor |---->  output
                +-----------+


O doctree_ é a representação hierárquica do documento rst
formada por um conjunto de nós organizados em uma estrutura de árvore.
A doctree pode ser visualizada textualmente através do comando ``rst2pseudoxml``.
Por exemplo, o trecho de texto rst abaixo::

Usando o trecho em rst abaixo::

    Título
    ======

    Texto e mais texto


O doctree correspondente pode ser entendido melhor com a ajuda do rst2pseudoxml::

    <document ids="titulo" names="título" source="snippet.rst" title="Título">
        <title>
            Título
        <paragraph>
            Texto e mais texto:


Para converter o rst para a saída no formato desejado,
é necessário percorrer cada nó da estrutura
e executar algum tipo de ação de acordo com o tipo e conteúdo do nó.
O percorrimento da árvore é feito através de uma implementação do padrão de projeto "Visitor" [GoF95]_.
A responsabilidade pela visitação está no doctree,
e é iniciada pelo método ``walkabout`` invocado do nó raiz.
A cada nó visitado, dois métodos do objeto ``visitor``, que foi recebido como parâmetro,
são invocados: ``dispatch_visit`` e ``dispatch_departure``.
O primeiro é invocado antes que os nós-filho sejam visitados e o segundo é invocado depois.
Por sua vez, o método ``dispatch_visit`` chama um método cujo nome é a combinação da
palavra ``visit_`` com o nome da classe do nó sendo visitado.
O método ``dispatch_departure`` tem um comportamento análogo e chama um método de nome ``depart_``
combinado com o nome da classe do nó sendo visitado.

Para a doctree do exemplo acima, a sequência de chamadas correspondentes seria::

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

A divisão da visitação em dois momentos,
permite que o conversor faça uma ação inicial e final para a montagem de cada elemento da saída.

Cabe a uma subclasse de ``NodeVisitor`` implementar corretamente esses métodos.
No módulo rst2html5, isto é feito pela classe HTML5Translator.

HTML5Translator
===============

A classe ``HTML5Translator`` é uma subclasse de ``NodeVisitor``
que implementa os métodos ``visit_<nome da classe do nó>`` e ``depart_<nome da classe do nó>``
necessários para converter um elemento do rst em seu correspondente em html5.

Como há um aninhamento de nós, isto é, um nó contém outros nós,
a montagem do resultado final é feita com o auxílio de uma estrutura de pilha
para registrar o contexto de cada elemento.

A ação padrão de um método ``visit_<nome da classe do nó>`` é iniciar um novo contexto para o nó sendo tratado.
A ação padrão no ``depart_`` é criar o elemento html5 de acordo com o contexto salvo
e registrá esse elemento no nó-pai.

.. code-block:: python

    def default_visit(self, node):
        # cria um novo contexto na pilha para o elemento corrente

    def default_departure(self, node):
        # Cria o elemento html5 de acordo com o contexto corrente

Nem todos os elementos rst seguem exatamente o mesmo procedimento padrão.
O elemento ``Text``, por exemplo, é um nó folha e, por isso,
não requer a criação de um contexto específico.
Basta adicionar o texto correspondente ao elemento pai (veja ref???).

Outros elementos rst têm um comportamento comum e compartilham o mesmo método ``visit_`` e/ou
``depart_``.
O mapeamento entre o nó rst e os métodos correspondentes é feito pelo dicionário ``rst_terms``.
Além dos nomes dos métodos, define também qual a *tag* padrão para o elemento,
se o nome do elemento rst deve aparecer como um atributo ``class="nome_da_classe_do_nó"``
e se o elemento deve ou não ser indentado na saída formatada.
O mapeamento é executado ao final do módulo,
no trecho de código que realmente amarra o mapeamento aos atributos da classe ``HTML5Translator``.

A montagem do elemento html5 é feito com ajuda do módulo genshi.builder,
que possui uma documentação muito boa e, por isso, não será explicado aqui.

HTML5Writer
===========

A doctree não é passada diretamente ao HTML5Translator.
Ao invés disso, o docutils usa como padrão um objeto da classe ``Writer``,
cuja responsabilidade é coordenar a tradução para o formato final desejado::

                      Converter
                +-------------------+
                |    +---------+    |
    doctree -------->|  Writer |------->  output
                |    +----+----+    |
                |         |         |
                |         |         |
                |   +-----+------+  |
                |   | Translator |  |
                |   +------------+  |
                +-------------------+


A conversão acontece efetivamente no método ``translate``,
que é sobrescrito na subclasse ``HTML5Writer``,
que chama o método de visitação ``walkabout`` de doctree passando um objeto ``HTML5Translator``,
que é quem faz a conversão na verdade::

                        rst2html5
                +-----------------------+
                |    +-------------+    |
     doctree ------->| HTML5Writer |------->  html5
                |    +------+------+    |
                |           |           |
                |           |           |
                |  +-----------------+  |
                |  | HTML5Translator |  |
                |  +-----------------+  |
                +-----------------------+
