from __future__ import unicode_literals

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


def pygmentize(code, language, linenos=False, **kwargs):
    lexer = get_lexer_by_name(language, stripall=True)
    formatter = HtmlFormatter(linenos=(linenos and 'table'), **kwargs)
    return highlight(code, lexer, formatter)
