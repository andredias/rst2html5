import re

from docutils import nodes
from docutils.parsers.rst.roles import register_local_role

# borrowed from Pelican
# https://github.com/getpelican/pelican/blob/d43b786b300358e8a4cbae4afc4052199a7af762/pelican/rstdirectives.py#L76


class abbreviation(nodes.Inline, nodes.TextElement):
    pass


_abbr_re = re.compile(r'\((.*)\)$', re.DOTALL)


def abbr_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    m = _abbr_re.search(text)
    if m is None:
        return [abbreviation(text, text)], []
    abbr = text[: m.start()].strip()
    title = m.group(1)
    return [abbreviation(abbr, abbr, title=title)], []


register_local_role('abbr', abbr_role)
