#!/usr/bin/env python
# package: sutils
# licence: MIT <https://opensource.org/licenses/MIT>
# author: Daniel Kovacs <mondomhogynincsen@gmail.com>
# file: sutils/setup.py
# file-version: 2.2.1


# ---------------------------------------------------------------------------------------
# configuration
# ---------------------------------------------------------------------------------------

NAME = "sutils"
VERSION = "0.7.1"
DESCRIPTION = """Smart utilities for smart python programmers"""
AUTHOR = "Daniel Kovacs"
AUTHOR_EMAIL = "mondomhogynincsen@gmail.com"
MAINTAINER = "Daniel Kovacs"
MAINTAINER_EMAIL = "mondomhogynincsen@gmail.com"
SCM_URL= "https://github.com/ultralightweight/sutils"
KEYWORDS = []
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.6",
]

# ---------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------

import codecs
import os
import re

from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


# ---------------------------------------------------------------------------------------
# _read()
# ---------------------------------------------------------------------------------------

def _read(*parts):
    with codecs.open(os.path.join(HOME, *parts), "rb", "utf-8") as f:
        return f.read()


# ---------------------------------------------------------------------------------------
# get_requirements
# ---------------------------------------------------------------------------------------

def get_requirements():
    packages, dependencies = [], []
    for ir in parse_requirements(os.path.join( HOME, 'requirements.txt' ), session=False):
        if ir.link:
            dependencies.append(ir.link.url)
            continue
        packages.append(str(ir.req))
    return packages, dependencies


# ---------------------------------------------------------------------------------------
# internal variables
# ---------------------------------------------------------------------------------------

HOME = os.path.abspath(os.path.dirname(__file__))
PACKAGES = find_packages(where='src')
INSTALL_REQUIRES, DEPENDENCY_LINKS = get_requirements()


# ---------------------------------------------------------------------------------------
# setup()
# ---------------------------------------------------------------------------------------

if __name__ == "__main__":
    setup(
        name=NAME,
        description=DESCRIPTION,
        license="License :: MIT",
        url=SCM_URL,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        keywords=KEYWORDS,
        long_description=_read("README.md"),
        packages=PACKAGES,
        package_dir={"": "src"},
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        dependency_links=DEPENDENCY_LINKS,
        setup_requires=[
        ],
        tests_require=[
            'pytest',
        ],
    )
