# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import Directive, directives

#
# The functions below were borrowed from Sphinx to avoid direct dependency to its code
#


def parselinenos(spec, total):
    """
    Parse a line number spec (such as "1,2,4-6") and return a list of wanted line numbers.

    copied from sphinx.util import parselinenos
    """
    items = list()
    parts = spec.split(',')
    for part in parts:
        try:
            begend = part.strip().split('-')
            if len(begend) > 2:
                raise ValueError
            if len(begend) == 1:
                items.append(int(begend[0]) - 1)
            else:
                start = (begend[0] == '') and 0 or int(begend[0]) - 1
                end = (begend[1] == '') and total or int(begend[1])
                items.extend(range(start, end))
        except Exception:
            raise ValueError('invalid line number spec: %r' % spec)
    return items


def dedent_lines(lines, dedent):
    '''
    copied from sphinx.code.dedent_lines
    '''
    if not dedent:
        return lines

    new_lines = []
    for line in lines:
        new_line = line[dedent:]
        if line.endswith('\n') and not new_line:
            new_line = '\n'  # keep CRLF
        new_lines.append(new_line)

    return new_lines


def container_wrapper(directive, literal_node, caption):
    '''
    copied from sphinx.code.container_wrapper
    '''
    container_node = nodes.container('', literal_block=True,
                                     classes=['literal-block-wrapper'])
    parsed = nodes.Element()
    directive.state.nested_parse(ViewList([caption], source=''),
                                 directive.content_offset, parsed)
    caption_node = nodes.caption(parsed[0].rawsource, '',
                                 *parsed[0].children)
    caption_node.source = parsed[0].source
    caption_node.line = parsed[0].line
    container_node += caption_node
    container_node += literal_node
    return container_node


def set_source_info(directive, node):
    '''
    copied from sphinx.util.nodes import set_source_info
    '''
    node.source, node.line = directive.state_machine.get_source_and_line(directive.lineno)


class CodeBlock(Directive):
    '''
    Directive for a code block with special highlighting or line numbering
    settings.

    This class mix docutils and Sphinx CodeBlock directives.
    '''

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'linenos': directives.flag,
        'dedent': int,
        'lineno-start': int,
        'emphasize-lines': directives.unchanged_required,
        'caption': directives.unchanged_required,
        # docutils CodeBlock options
        'class': directives.class_option,
        'name': directives.unchanged,
        'number-lines': directives.unchanged  # integer or None
    }

    def run(self):
        self.assert_has_content()

        if 'number-lines' in self.options:
            self.options['linenos'] = True
            if self.options['number-lines']:
                self.options['lineno-start'] = int(self.options['number-lines'])

        code = '\n'.join(self.content)
        if 'dedent' in self.options:
            lines = code.split('\n')
            lines = dedent_lines(lines, self.options['dedent'])
            code = '\n'.join(lines)

        codeblock = nodes.literal_block(code, code, classes=self.options.get('class', []))
        self.add_name(codeblock)
        # if called from "include", set the source
        if 'source' in self.options:
            codeblock.attributes['source'] = self.options['source']
        codeblock['language'] = self.arguments[0]
        codeblock['linenos'] = ('linenos' in self.options or
                                'lineno-start' in self.options) and 'table'

        linespec = self.options.get('emphasize-lines')
        if linespec:
            try:
                nlines = len(self.content)
                hl_lines = [x + 1 for x in parselinenos(linespec, nlines)]
            except ValueError as err:
                document = self.state.document
                return [document.reporter.warning(str(err), line=self.lineno)]
        else:
            hl_lines = None

        extra_args = codeblock['highlight_args'] = {}
        if hl_lines is not None:
            extra_args['hl_lines'] = hl_lines
        if 'lineno-start' in self.options:
            extra_args['linenostart'] = self.options['lineno-start']
        set_source_info(self, codeblock)

        caption = self.options.get('caption')
        if caption:
            codeblock = container_wrapper(self, codeblock, caption)

        return [codeblock]


class Define(Directive):
    '''
    Defines an identifier to be checked by directive ifdef and ifndef.
    Identifiers are case insensitive.
    More than one identifier can be defined at once. Example::

        .. define:: one
        .. define:: two three four

    '''

    has_content = False
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        if not self.state.document.settings.identifiers:
            identifiers = self.state.document.settings.identifiers = []
        else:
            identifiers = self.state.document.settings.identifiers
        arguments = self.arguments[0].lower().split()
        for identifier in arguments:
            identifier = identifier.lower()
            if identifier not in identifiers:
                identifiers.append(identifier)
        return []


class Undefine(Directive):
    '''
    Undefine an identifier. Example::

        .. undef:: one
        .. undef:: one two three four

    '''

    has_content = False
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        identifiers = self.state.document.settings.identifiers or []
        arguments = self.arguments[0].lower().split()
        for identifier in arguments:
            identifier = identifier.lower()
            if identifier in identifiers:
                identifiers.remove(identifier)
        return []


class IfDef(Directive):
    '''
    Include content only if the identifier passed as argument is defined.
    If more than one identified is passed,
    there must be an option to identify which logical operation is to be used:
    'and' or 'or'.  Example::

        .. ifdef:: x y z
            :operator: or

            some content...

    'some content...' only will be included if x or y or z is defined.
    '''

    def logical_operator(argument):
        return directives.choice(argument, ['and', 'or'])

    has_content = True
    required_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'operator': logical_operator,
    }

    def check(self):
        self.assert_has_content()
        identifiers = self.state.document.settings.identifiers or []
        arguments = self.arguments[0].lower().split()
        if len(arguments) == 1:
            identifier = arguments[0]
            show_content = identifier in identifiers
        else:
            if 'operator' not in self.options:
                raise self.error('You must define an operator when more than one '
                                 'identifier is passed as argument.')
            operator = self.options['operator']
            operation = {
                'and': (lambda x, y: x and y),
                'or': (lambda x, y: x or y)
            }
            show_content = operator == 'and'
            for identifier in arguments:
                show_content = operation[operator](show_content, identifier in identifiers)
        return show_content

    def run(self):
        if self.check():
            # see Include Directive at docutils/parsers/rst/directives/misc.py
            lines = self.content.data
            source = self.content.source(0)
            self.state_machine.insert_input(lines, source)
        return []


class IfNDef(IfDef):
    '''
    Include content only if the identifier passed as argument is not defined.
    See IfDef directive for options
    '''

    def check(self):
        return not IfDef.check(self)
