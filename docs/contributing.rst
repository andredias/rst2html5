=========================
Contributing to rst2html5
=========================

Contributions are welcome!
So don't be afraid to contribute with anything that you think will be helpful.
Help with maintaining the English documentation are particularly appreciated.

The bugtracker, wiki and Mercurial repository can be found at the
`rst2html5 projects's page <https://bitbucket.org/andre_felipe_dias/rst2html5>`_ on BitBucket.


How to contribute
=================

Please, follow the procedure:

#. Check for the open issues or open a new issue on the BitBucket `issue tracker`_
   to start a discussion about a feature or a bug.
#. Fork the `rst2html5 project`_ on BitBucket and start making your modifications.
#. Send a pull request.


Setup
=====

#. Clone the repository using `Mercurial <http://mercurial.selenic.com/>`_::

    $ hg clone http://www.bitbucket.org/andre_felipe_dias/rst2html5

#. Install `virtualenv <http://pypi.python.org/pypi/virtualenv>`_ if you do not already have it.
   Using a virtual environment will make the installation easier,
   and will help to avoid clutter in your system-wide libraries.

#. Create a virtual environment and activate it::

    $ virtualenv rst2html5/env
    $ source rst2html5/env/bin/activate

#. Install project's requirements via `pip <https://pypi.python.org/pypi/pip>`_::

    $ cd rst2html5
    $ pip install -r requirements.txt -r test_requirements.txt

Now you are ready!

.. _test suite:

Running the test suite
======================

To run the tests, just type the following on a terminal::

    $ nosetests

To get some metrics, try::

    $ flake8 --exclude="env,build,doc" .

To get a complete test verification, run::

    $ ./runtests.sh

The complete tests save some interesting metrics at :file:`rst2html5/metrics`.

.. important::

    Before sending a patch or a pull request,
    ensure that all tests pass and there is no flake8 error or warning codes.


Documentation
=============

Contributing to documentation is as simple as editing the specified file in the doc directory
of the source.
We use restructuredtext markup and `Sphinx <http://sphinx-doc.org/>`_ for building the documentation.


.. _reporting an issue:

Reporting an issue
==================

Proposals, enhancements, bugs or tasks should be directly reported on BitBucket `issue tracker`_.

If there are issues please let us know.
So we can improve rst2html5. If you don’t report it, we probably wont fix it.
When creating a bug issue, try to provide the following information at least:

#. Steps to reproduce the bug
#. The produced output
#. The expected output

..
    #. What version of ``rst2html5`` you are using
    #. Any additional relevant information

.. tip::

    See https://bitbucket.org/andre_felipe_dias/rst2html5/issue/1 as a reference.

For proposals or enhancements,
you should provide input and output examples.
Whenever possible, you should also provide external references to articles or documentation
that endorses your request.

While it's handy to provide useful code snippets in an issue, it is better for
you as a developer to submit pull requests. By submitting pull request your
contribution to ``rst2html5`` will be recorded by BitBucket.

..
    Sending a pull request
    ======================

    #. Test what you code. Any new code should have one or more test cases. See :ref:`tests`.
    #. Don't mix

    code changes with whitespace cleanup.


Contacting the author
=====================

``rst2html5`` is written and maintained by André Felipe Dias.
You can reach me at `google plus`_ or twitter_.

.. _rst2html5 project: https://bitbucket.org/andre_felipe_dias/rst2html5
.. _issue tracker: http://www.bitbucket.org/andre_felipe_dias/rst2html5/issues
.. _twitter: https://twitter.com/andref_dias
.. _google plus: https://plus.google.com/100373126641024342168
