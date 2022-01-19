#!/usr/bin/env python
# -*- coding: utf-8 -*
import os
import pathlib
import sys

from setuptools import find_packages, setup
from setuptools.command.install import install

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

VERSION = "1.0.0"

REPO_ROOT = pathlib.Path(__file__).parent


# Fetch the long description from the readme
with open(REPO_ROOT / "README.md", encoding="utf-8") as f:
    README = f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version."""

    description = "verify that the git tag matches our version"

    def run(self):
        tag = os.getenv("CIRCLE_TAG")

        if tag != VERSION:
            info = f"Git tag: {tag} does not match the version of this app: {VERSION}"
            sys.exit(info)


install_requires = [
    "tentaclio",
    "databricks-sql-connector",
]


setup_args = dict(
    name="tentaclio-databricks",
    version=VERSION,
    include_package_data=True,
    description="A python project containing all the dependencies for the databricks+thrift tentaclio schema.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Octopus Energy",
    author_email="nerds@octopus.energy",
    license="Proprietary",
    package_dir={"": "src"},
    packages=find_packages("src", include=["*tentaclio_databricks*"]),
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    cmdclass={"verify": VerifyVersionCommand},
)


if __name__ == "__main__":
    setup(**setup_args)
