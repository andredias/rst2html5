#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2html5 in the form:
# case = {'rst': rst_text, 'out': expected_output, ...}

from __future__ import unicode_literals

paragraph = {
    'rst': 'Paragraph',
    'out': '\n    <meta charset="utf-8" />\n',
    'indent_output': True
}

math_role = {
    'rst': r':math:`\sqrt{3x-1}+(1+x)^2`',
    'out': '<meta charset="utf-8" /><script src="http://cdn.mathjax.org/mathjax/latest/MathJax.js'\
           '?config=TeX-AMS-MML_HTMLorMML"></script>'
}

metadata = {
    'rst': '.. title:: Foo Bar',
    'out': '<meta charset="utf-8" /><title>Foo Bar</title>'
}

stylesheet = {
    'rst': 'ordinary paragraph',
    'out': '''
    <meta charset="utf-8" />
    <link href="http://test.com/css/default.css" rel="stylesheet" />
    <link href="http://www.pronus.eng.br/css/standard.css" rel="stylesheet" />
''',
    'indent_output': True,
    'stylesheet': 'http://test.com/css/default.css, http://www.pronus.eng.br/css/standard.css'
}


javascript = {
    'rst': 'ordinary paragraph',
    'out': '''
    <meta charset="utf-8" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
''',
    'indent_output': True,
    'script': 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js',
}

meta = {
    'rst': '''.. meta::
    :author: André Felipe Dias

.. meta::
    :http-equiv=X-UA-Compatible: chrome=1
''',
    'out': '''
    <meta charset="utf-8" />
    <meta content="André Felipe Dias" name="author" />
    <meta content="chrome=1" http-equiv="X-UA-Compatible" />
''',
    'indent_output': True,
}
