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

MySQL
=====

CREATE TABLE `email_msgs` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email_address` varchar(255) COLLATE utf8_bin NOT NULL,
    `subject` varchar(255) COLLATE utf8_bin NOT NULL,
    `body` varchar(10000) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;

Email Form
==========

I fell off the edge of my mental map when it came to the part of the assignment 
in which I was to create a z3c form with 3 fields email address, subject and body 
and save the data into mysql. That remains untouched, although I created the mysql table.


Installation
============

Install hmn.university by adding it to your buildout::

    [buildout]

    ...

    eggs =
        hmn.university


and then running ``bin/buildout``


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
