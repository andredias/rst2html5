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
