from .directives import CodeBlock
from docutils.parsers.rst import directives

directives.register_directive('code-block', CodeBlock)
directives.register_directive('sourcecode', CodeBlock)
