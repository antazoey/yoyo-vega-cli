#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup  # type: ignore

extras_require = {
    "test": [
        "pytest>=6.0,<7.0",
    ],
    "lint": [
        "black>=21.10b0,<22.0",  # auto-formatter and linter
        "mypy>=0.910,<1.0",  # Static type analyzer
        "flake8>=3.8.3,<4.0",  # Style linter
        "isort>=5.9.3,<6.0",  # Import sorting linter
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools",  # Installation tool
        "wheel",  # Packaging tool
        "twine",  # Package upload tool
    ],
    "dev": [
        "commitizen",  # Manage commits and publishing releases
        "pre-commit",  # Ensure that linters are run prior to commiting
        "pytest-watch",  # `ptw` test watcher/runner
        "IPython",  # Console for interacting
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}

# NOTE: `pip install -e .[dev]` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["lint"]
    + extras_require["release"]
    + extras_require["dev"]
)

with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="yoyo-vega-cli",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="""yoyo-vega-cli: A CLI for the Yoyo Vega block explorer""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yoyo Blocks",
    author_email="admin@yoyo.ooo",
    url="https://github.com/unparalleled-js/yoyo-vega-cli",
    include_package_data=True,
    install_requires=[
        "importlib-metadata ; python_version<'3.8'",
        "click>=8.0.4"
    ],  # NOTE: Add 3rd party libraries here
    python_requires=">=3.7,<4",
    extras_require=extras_require,
    py_modules=["yoyo"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"yoyo": ["py.typed"]},
    entry_points={
        "console_scripts": ["yoyo=yoyo._cli:cli"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
