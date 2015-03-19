from __future__ import unicode_literals

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


def pygmentize(code, language, linenos=False, **kwargs):
    lexer = get_lexer_by_name(language, stripall=True)
    formatter = HtmlFormatter(linenos=(linenos and 'table'), **kwargs)
    result = highlight(code, lexer, formatter)
    if result.startswith('<div class="highlight"><pre>'):
        start = len('<div class="highlight"><pre>')
        stop = len(result) - len('</pre></div>\n') - 1
        result = result[start:stop:]
    return result
