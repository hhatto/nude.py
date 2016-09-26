nude.py
=======

.. image:: https://travis-ci.org/hhatto/nude.py.svg?branch=master
    :target: https://travis-ci.org/hhatto/nude.py
    :alt: Build status

About
-----
Nudity detection with Python. Port of `nude.js`_ to Python.

.. _`nude.js`: https://github.com/pa7/nude.js


Installation
------------
from pip::

    $ pip install --upgrade nudepy

from easy_install::

    $ easy_install -ZU nudepy


Requirements
------------
* Python2.7+ and Python3.3+
* Cython
* Pillow


Usage
-----
via command-line

.. code-block:: sh

    $ nudepy IMAGE_FILE

via Python Module

.. code-block:: python

    import nude
    from nude import Nude

    print(nude.is_nude('./nude.rb/spec/images/damita.jpg'))

    n = Nude('./nude.rb/spec/images/damita.jpg')
    n.parse()
    print("damita :", n.result, n.inspect())

see examples_ .

.. _examples: https://github.com/hhatto/nude.py/tree/master/examples

Links
-----
* PyPI_
* GitHub_

.. _PyPI: http://pypi.python.org/pypi/nudepy/
.. _GitHub: https://github.com/hhatto/nude.py
