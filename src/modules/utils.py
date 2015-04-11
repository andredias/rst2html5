from __future__ import unicode_literals

import re
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from genshi.builder import tag
from genshi.core import Markup


def pygmentize(code, language, linenos=False, **kwargs):
    lexer = get_lexer_by_name(language)
    formatter = HtmlFormatter(linenos=(linenos and 'table'), **kwargs)
    return highlight(code, lexer, formatter)


def pygmentize_to_tag(code, language, linenos=False, **kwargs):
    '''
    Rebuild a raw pygmentize highlighting as tag elements, avoiding Genshi to delete blank lines.

    See http://genshi.edgewall.org/wiki/GenshiFaq#WhatisGenshidoingwiththewhitespaceinmymarkuptemplate
    '''

    codeblock = pygmentize(code, language, linenos, **kwargs)
    pre = re.findall('<pre>(.*?)\n*</pre>', codeblock, re.DOTALL)
    if len(pre) == 1:
        return tag.pre(Markup(pre[0]), data_language=language)
    return tag.table(
        tag.tr(
            tag.td(
                tag.pre(pre[0])  # line numbers
            ),
            tag.td(
                tag.pre(Markup(pre[1]))  # code
            )
        ),
        data_language=language
    )
