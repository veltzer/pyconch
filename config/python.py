""" python deps for this project """

scripts: dict[str,str] = {
    "pyconch": "pyconch.endpoints.main:main",
}
config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "pytconf",
    "prompt_toolkit",
    "ptterm",
]
build_requires: list[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
]
requires = config_requires + install_requires + build_requires + test_requires
