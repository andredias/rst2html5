import os
from pathlib import Path

from pytest import fixture


@fixture(autouse=True, scope='session')
def chdir():
    os.chdir(Path(__file__).parent)
