#! /usr/bin/env python3

from setuptools import setup
from glob import glob

url = "https://github.com/chuanconggao/extratools"
version = "0.6.12"

setup(
    name="extratools",

    packages=["extratools"],
    scripts=glob("bin/extratools-*"),
    include_package_data=True,

    url=url,

    version=version,
    download_url=f"{url}/tarball/{version}",

    license="MIT",

    author="Chuancong Gao",
    author_email="chuancong@gmail.com",

    description="Extra Functional Tools beyond Standard and Third-Party Libraries",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    keywords=[
        "functional",
        "tools"
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],

    python_requires=">= 3",
    install_requires=[
        line.strip() for line in open("requirements.txt")
    ]
)
