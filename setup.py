#!/usr/bin/env python
# -*- coding: utf-8 -*

import os
import pathlib

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

VERSION = "0.0.0"

REPO_ROOT = pathlib.Path(__file__).parent

# Fetch the long description from the readme
with open(REPO_ROOT / "README.md", encoding="utf-8") as f:
    README = f.read()

install_requires = [
    # Databricks
    "pyodbc",
    # tentaclio-core
    "tentaclio>=0.0.15",
]


setup_args = dict(
    name="tentaclio-databricks",
    version=VERSION,
    include_package_data=True,
    description="A python project containing all the dependencies for schema Databricks:pyodbc for tentaclio.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Octopus Energy",
    author_email="nerds@octopus.energy",
    license="Proprietary",
    package_dir={"": "src"},
    packages=find_packages("src", include=["*tentaclio_databricks*"]),
    install_requires=install_requires,
    #dependency_links=["https://github.com/octoenergy/tentaclio.git"],
    process_dependency_links=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)


if __name__ == "__main__":

    # Make install or pip install -e
    setup(**setup_args)
