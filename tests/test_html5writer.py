import os
from io import StringIO, open
from tempfile import gettempdir
from typing import Any, Dict, Iterable, Tuple

import pytest
from bs4 import BeautifulSoup
from docutils.core import publish_parts

from src.rst2html5_ import HTML5Writer

tmpdir = gettempdir()
TestCase = Tuple[str, Dict[str, Any]]


def rst_to_html5_part(case: Dict[str, Any]) -> Tuple[str, Any]:
    """
    The main parts of a test case dict are rst, part and out.
    Everything else are configuration settings.
    """
    overrides = case.copy()
    rst = overrides.pop('rst')
    part = overrides.pop('part')
    error = StringIO()
    overrides.pop('out')
    overrides.setdefault('indent_output', True)
    overrides['warning_stream'] = error
    return (
        publish_parts(writer=HTML5Writer(), source=rst, settings_overrides=overrides)[part],
        error.getvalue(),
    )


def extract_test_cases() -> Iterable[TestCase]:
    """
    Extract variables of a test data module.
    Variables should be a dict().
    For example, {'rst': rst, 'out':out, ...}
    """
    from . import cases

    return (
        (v, getattr(cases, v)) for v in dir(cases) if not v.startswith('__') and isinstance(getattr(cases, v), dict)
    )


def idn_func(test_case: TestCase) -> str:
    return test_case[0]


@pytest.mark.parametrize('test_case', extract_test_cases(), ids=idn_func)
def test_rst_case(test_case: TestCase) -> None:
    test_name, case = test_case
    result, error = rst_to_html5_part(case)
    result_ = result
    expected = case['out']
    if case['part'] in ('head', 'body', 'whole'):
        result = BeautifulSoup(result, 'html.parser').find_all()
        expected = BeautifulSoup(expected, 'html.parser').find_all()
    if result != expected:
        filename = os.path.join(tmpdir, test_name)
        with open(filename + '.rst', encoding='utf-8', mode='w') as f:
            f.write(case['rst'])
        with open(filename + '.result', encoding='utf-8', mode='w') as f:
            f.write(result_)
        with open(filename + '.expected', encoding='utf-8', mode='w') as f:
            f.write(case['out'])
    assert expected == result  # better diff visualization
    assert case.get('error', '') == error
