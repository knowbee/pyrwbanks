# rw_banks

[![Downloads](https://pepy.tech/badge/rw-banks)](https://pepy.tech/project/rw-banks)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

A lightweight python package that can be used to get list of licensed banks from Rwanda
and their corresponding swift code, address, contact information, ussd code and bank code.

## Installation

The distribution is hosted on pypi at: https://pypi.org/project/rw_banks/. To directly install the package from pypi, run from your terminal::

    $ pip install rw_banks

## Usage

```py

   from rw_banks import getBanks, getbank

   print(getBanks()); //list of licensed banks
   print(getbank("BKIGRWRW")); //dict of licensed bank with this swift code ("BKIGRWRW")

```
