#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import codecs
import unittest

from html5css3 import HTML5Writer
from docutils.core import publish_parts
from nose.tools import assert_equals
from tempfile import gettempdir

tmpdir = gettempdir()

def rst_to_html5(rst, indent_output=False, show_id=False):
    overrides = {'indent_output': indent_output, 'show_id': show_id}
    parts = publish_parts(writer=HTML5Writer(), source=rst,
                          settings_overrides=overrides)
    return parts


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
    import test_data_head
    for test_name, case in extract_variables(test_data_head):
        out = case.pop('out')
        yield _test_part, 'head', test_name, case, out


def test_body():
    '''
    test the body part of a rst2html5 conversion
    '''
    import test_data_body
    for test_name, case in extract_variables(test_data_body):
        out = case.pop('out')
        yield _test_part, 'body', test_name, case, out


def _test_part(part_name, test_name, params, out):
    try:
        assert_equals(rst_to_html5(**params)[part_name], out)
    except Exception as error:
        '''
        write temp files to help manual testing
        '''
        filename = os.path.join(tmpdir, test_name)
        with codecs.open(filename + '.rst', encoding='utf-8', mode='w') as f:
            f.write(params['rst'])

        if isinstance(error, AssertionError):
            error.args = ('%s: %s' % (test_name, error.message), )
        raise error
