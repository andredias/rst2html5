from .directives import CodeBlock, Define, Undefine, IfDef, IfNDef
from docutils.parsers.rst import directives

directives.register_directive('code-block', CodeBlock)
directives.register_directive('sourcecode', CodeBlock)
directives.register_directive('define', Define)
directives.register_directive('undef', Undefine)
directives.register_directive('undefine', Undefine)
directives.register_directive('ifdef', IfDef)
directives.register_directive('ifndef', IfNDef)
