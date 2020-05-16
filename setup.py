#!/usr/bin/env python
from setuptools import setup,find_packages
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="rw_banks",
    version='0.0.4',
    description="Get a list of licensed banks from Rwanda and their corresponding swift code, address, contact info, ussd code and bank code",
    long_description=long_description,
    py_modules=["rw_banks"],
    packages = find_packages(),
    keywords=["banks",
              "rwanda",
              "banki"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
    ],
    author='Igwaneza Bruce',
    author_email='knowbeeinc@gmail.com',
    license='MIT',
    zip_safe=False,

)
