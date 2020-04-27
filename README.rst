# rw_banks
============
.. image:: https://travis-ci.com/knowbee/pyrwbanks.svg?token=yN9jXnk59suszMqNsJJb&branch=master
    :target: https://travis-ci.com/knowbee/pyrwbanks
.. image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=102
    :target: https://github.com/ellerbrock/open-source-badge/

A lightweight python package that can be used to get list of licensed banks from Rwanda 
and their corresponding swift code, address, contact information, ussd code and bank code.

Installation
------------

The distribution is hosted on pypi at: https://pypi.org/project/rw_banks/. To directly install the package from pypi, run from your terminal::

    $ pip install rw_banks

Usage
----------- 

rw_banks
===========

.. code-block :: python

   from rw_banks import getBanks, getbank

   print(getBanks()); //list of licensed banks
   print(getbank("BKIGRWRW")); //dict of licensed bank with this swift code ("BKIGRWRW")

License
=========================
MIT License

Copyright (c) 2020, Igwaneza Bruce <knowbeeinc@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
