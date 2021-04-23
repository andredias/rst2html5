from io import StringIO
from pathlib import Path
from tempfile import gettempdir
from typing import Any, Dict, Iterable, Tuple

import pytest
from bs4 import BeautifulSoup
from docutils.core import publish_parts

from rst2html5 import HTML5Writer

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
    case_error = case.get('error', '')
    if case['part'] in ('head', 'body', 'whole'):
        result = BeautifulSoup(result, 'html.parser').find_all()
        expected = BeautifulSoup(expected, 'html.parser').find_all()
    if result != expected or case.get('error', '') != error:
        filename = Path(tmpdir, test_name)
        filename.with_suffix('.rst').write_text(case['rst'])
        filename.with_suffix('.result').write_text(result_)
        filename.with_suffix('.expected').write_text(case['out'])
    if case_error != error:
        filename.with_suffix('.error.expected').write_text(error)
        filename.with_suffix('.error.result').write_text(case_error)
    assert expected == result
    assert case_error == error
