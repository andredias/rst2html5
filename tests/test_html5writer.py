#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import unittest
from functools import partial
from io import open
from tempfile import gettempdir
from bs4 import BeautifulSoup

from docutils.core import publish_parts
from nose.tools import assert_equals

from rst2html5 import HTML5Writer
try:
    from io import StringIO
except ImportError:  # Python 2.x
    from StringIO import StringIO

tmpdir = gettempdir()
unittest.TestCase.maxDiff = None


def rst_to_html5_part(case):
    '''
    The main parts of a test case dict are rst, part and out.
    Everything else are configuration settings.
    '''
    overrides = case.copy()
    rst = overrides.pop('rst')
    part = overrides.pop('part')
    error = StringIO()
    overrides.pop('out')
    overrides.setdefault('indent_output', True)
    overrides['warning_stream'] = error
    return publish_parts(writer=HTML5Writer(), source=rst,
                         settings_overrides=overrides)[part], error.getvalue()


def extract_variables(module):
    '''
    Extract variables of a test data module.
    Variables should be a dict().
    For example, {'rst': rst, 'out':out, ...}
    '''
    return ((v, getattr(module, v)) for v in dir(module)
            if not v.startswith('__') and isinstance(getattr(module, v), dict))


def test():
    # do not use docstrings
    # see http://code.google.com/p/python-nose/issues/detail?id=244#c1
    from . import cases
    for test_name, case in extract_variables(cases):
        func = partial(check_part)
        func.description = test_name
        yield func, test_name, case


def check_part(test_name, case):
    result, error = rst_to_html5_part(case)
    result_ = result
    expected = case['out']
    if case['part'] in ('header', 'body', 'whole'):
        result = BeautifulSoup(result, 'html.parser').decode()
        expected = BeautifulSoup(expected, 'html.parser').decode()
    if result != expected:
        filename = os.path.join(tmpdir, test_name)
        with open(filename + '.rst', encoding='utf-8', mode='w') as f:
            f.write(case['rst'])
        with open(filename + '.result', encoding='utf-8', mode='w') as f:
            f.write(result_)
        with open(filename + '.expected', encoding='utf-8', mode='w') as f:
            f.write(case['out'])
    assert_equals(expected, result)  # better diff visualization
    assert_equals(case.get('error', ''), error)
