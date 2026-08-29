#!/bin/bash
# Run pytest inside this repo's own uv-locked venv instead of the ambient
# Python environment: ptterm pins prompt_toolkit<3, which cannot coexist
# with the prompt_toolkit>=3 tooling (ipython, etc.) in the shared
# environment. `uv run --frozen` creates/syncs .venv from uv.lock
# (including the dev group, which carries pytest) and runs inside it.
set -euo pipefail
unset VIRTUAL_ENV
exec uv run --frozen pytest "$@"
