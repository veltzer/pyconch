""" python depedencies for this project """
from typing import List


console_scripts: List[str] = [
    "pyconch=pyconch.endpoints.main:main",
]
dev_requires: List[str] = [
    "pypitools",
    "black",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pytconf",
    "prompt_toolkit",
    "ptterm",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
