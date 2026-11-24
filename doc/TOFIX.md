# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `pyproject.toml:7` - `version = "0.0.5"` disagrees with `config/version.lua:2` (`0, 0, 6`), from which `src/pyconch/static.py:2` and `README.md:12` are generated; an installed package reports 0.0.5 in its metadata but `pyconch --version` prints 0.0.6. Bring pyproject.toml to the version in `config/version.lua` (and release, or roll version.lua back to 0.0.5).

## Low

- `src/pyconch/configs.py:9` - `ConfigDummy` with a `param` placeholder and a docstring copied from another tool ("Parameters for the symlink install tool") is never used by `main.py`; delete the module (and its `sphinx/pyconch.rst:7` entry) or give it real options.
- `rsconstruct.toml:28` - the ruff and mypy processors (`rsconstruct.toml:32` too) list `config` in `src_dirs`, but `config/` holds only `.lua` files (mypy reports "There are no .py[i] files in directory 'config'"); drop `config` from both lists.
- `doc/TODO.txt:1` - empty tracked file; delete it.
