#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2html5 in the form:
# case = {'rst': rst_text, 'out': expected_output, ...}

from __future__ import unicode_literals

sphinx_code_block = {
    'rst': '''.. code-block:: python
    :class: small
    :linenos:

    def double(x):
        return 2 * x
''',
    'out': '''
    <table class="small" data-language="python"><tr><td><pre>1
2</pre></td><td><pre><span class="k">def</span> \
<span class="nf">double</span><span class="p">(</span><span class="n">x</span>\
<span class="p">):</span>
    <span class="k">return</span> <span class="mi">2</span> <span class="o">*</span> \
<span class="n">x</span>
</pre>
</td></tr></table>
''',
    'part': 'body',
}
