# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'rootmeapi',
    version = '1.1',
    description = 'Root Me API',
    url = 'http://github.com/Remigascou/rootmeapi',
    author = 'Podalirius',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author_email = 'podalirius@protonmail.com',
    packages = setuptools.find_packages(),
    license = 'GPL2',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.4',
)
