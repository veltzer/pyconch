"""
Sanity tests: the package and every module in it import cleanly.

A failed import here means a missing declared dependency, a syntax
error, or a broken import-time side effect — the failure classes a
placeholder test never catches.
"""

import importlib
import pkgutil

import pyconch

# pyconch.main imports ptterm (abandoned upstream, last release 2018),
# which requires prompt_toolkit<3, while modern tooling (ipython,
# jupyter-console) needs prompt_toolkit>=3 — no one environment can
# host both, so importing main fails wherever those tools live. Until
# pyconch is ported off ptterm or retired, main stays out of the walk.
KNOWN_BROKEN = {"pyconch.main"}


def _raise_on_package_error(name: str) -> None:
    """Surface subpackages that fail to import during the walk."""
    raise ImportError(f"failed to import package {name}")


def test_package_imports() -> None:
    """The top-level package imports and knows its own name."""
    assert pyconch.__name__ == "pyconch"


def test_all_modules_import() -> None:
    """Every module in the package imports without errors."""
    for info in pkgutil.walk_packages(pyconch.__path__, prefix="pyconch.", onerror=_raise_on_package_error):
        if info.name in KNOWN_BROKEN:
            continue
        importlib.import_module(info.name)
