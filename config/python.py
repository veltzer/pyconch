console_scripts = [
    "pyconch=pyconch.endpoints.main:main",
]
dev_requires = [
    "pypitools",
]
config_install = []
install_requires = [
    "pytconf",
    "prompt_toolkit",
    "ptterm",
]
make_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
