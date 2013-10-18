DIStributional SEmantics Composition Toolkit
============================================

.. image:: https://travis-ci.org/dimazest/dissect.png?branch=master
    :target: https://travis-ci.org/dimazest/dissect

Installation
------------

To install the package run:

   pip install dissect

Development
-----------

To run the tests execute::

    python setup.py test

To run the tests on all supperoted Python versions and implementations run::

   tox

To install the package in an isolated environment for development run::

    virtualenv .
    source bin/activate

    pip install -e .
    pip install pytest  # And any other tools you find useful.

Now you are ready to develop and test your changes::

    py.test src/unitest

If you want to execute some of the tests run (for example, similarity related)::

   py.test src/unitest -k similarity

Read py.test documentation and have fun coding!
