# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.directives.code import dedent_lines, container_wrapper, parselinenos, set_source_info


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
        codeblock['linenos'] = 'linenos' in self.options or \
                               'lineno-start' in self.options

        linespec = self.options.get('emphasize-lines')
        if linespec:
            try:
                nlines = len(self.content)
                hl_lines = [x+1 for x in parselinenos(linespec, nlines)]
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


directives.register_directive('code-block', CodeBlock)
directives.register_directive('sourcecode', CodeBlock)
