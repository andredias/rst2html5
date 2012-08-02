#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import codecs
import unittest

from html5css3 import HTML5Writer
from docutils.core import publish_parts, publish_string
from nose.tools import assert_equals
from tempfile import gettempdir

tmpdir = gettempdir()
unittest.TestCase.maxDiff = None

def rst_to_html5(case, part=None):
    overrides = case.copy()
    rst = overrides.pop('rst')
    overrides.pop('out')
    overrides.setdefault('indent_output', False)
    if part:
        return publish_parts(writer=HTML5Writer(), source=rst,
                          settings_overrides=overrides)[part]
    else:
        return unicode(publish_string(writer=HTML5Writer(), source=rst,
                          settings_overrides=overrides), encoding='utf-8')


def extract_variables(module):
    '''
    Extract variables of a test data module.
    Variables should be a dict().
    For example, {'rst': rst, 'out':out, ...}
    '''
    return ((v, getattr(module, v)) for v in dir(module)
        if not v.startswith('__') and isinstance(getattr(module, v), dict))


def test_head():
    '''
    test the head part of a rst2html5 conversion
    '''
    import head_cases
    func = lambda x: rst_to_html5(x, 'head')
    for test_name, case in extract_variables(head_cases):
        yield _test_part, func, test_name, case


def test_body():
    '''
    test the body part of a rst2html5 conversion
    '''
    import body_cases
    func = lambda x: rst_to_html5(x, 'body')
    for test_name, case in extract_variables(body_cases):
        yield _test_part, func, test_name, case

def test_errors():
    '''
    test some cases that should raise expected test_errors
    '''
    import error_cases
    import sys

    aux_stderr = sys.stderr
    f = open(os.path.join(tmpdir, 'stderr.txt'), 'w')
    sys.stderr = f
    func = lambda x: rst_to_html5(x)
    try:
        for test_name, case in extract_variables(error_cases):
            yield _test_part, func, test_name, case
    finally:
        sys.stderr = aux_stderr
        f.close()


def _test_part(func, test_name, case):
    try:
        assert_equals(func(case), case['out'])
    except Exception as error:
        '''
        write temp files to help manual testing
        '''
        filename = os.path.join(tmpdir, test_name)
        with codecs.open(filename + '.rst', encoding='utf-8', mode='w') as f:
            f.write(case['rst'])

        if isinstance(error, AssertionError):
            error.args = ('%s: %s' % (test_name, error.message), )
        raise error
