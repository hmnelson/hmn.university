.. This README is meant for consumption by humans and PyPI. PyPI can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on PyPI or github. It is a comment.

.. image:: https://github.com/collective/hmn.university/actions/workflows/plone-package.yml/badge.svg
    :target: https://github.com/collective/hmn.university/actions/workflows/plone-package.yml

.. image:: https://coveralls.io/repos/github/collective/hmn.university/badge.svg?branch=main
    :target: https://coveralls.io/github/collective/hmn.university?branch=main
    :alt: Coveralls

.. image:: https://codecov.io/gh/collective/hmn.university/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/collective/hmn.university

.. image:: https://img.shields.io/pypi/v/hmn.university.svg
    :target: https://pypi.python.org/pypi/hmn.university/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/hmn.university.svg
    :target: https://pypi.python.org/pypi/hmn.university
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/hmn.university.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/hmn.university.svg
    :target: https://pypi.python.org/pypi/hmn.university/
    :alt: License


==============
hmn.university
==============

An add-on for Plone for universities. (Training exercise.)

State of my homework
====================

I believe I've now completed all the assignments, including the Day 3 
z3c email form that saves to mySQL. 

I also added first and last names to students, and the behavior to get 
the name from them and a Title() method that returns a concatenation
of the two.

That last bit doesn't quite work the way I want it to. I'd like to 
take the title and summary fields off the Add Student page, and set 
the actual title property from the Title() method. 

I also need a refresher on how to add indexes to the catalog for 
firstName and lastName. (Can that be done in code? I can't recall.)


Installation
============

Install hmn.university by adding it to your buildout::

    [buildout]

    ...

    eggs =
        hmn.university


and then running ``bin/buildout``

Starting Docker and mySQL
=========================

From the Plone root directory, run:

./docker-mysql-5.7.sh

Authors
=======

Hilary Mark Nelson
Web Developer
College of Engineering
Purdue University
West Lafayette, Indiana
USA

License
=======

The project is licensed under the GPLv2.
