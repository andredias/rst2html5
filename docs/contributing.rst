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


Installing OS Packages
======================

You will need:

#. pip_. A tool for installing and managing Python packages.
#. virtualenvwrapper_.
   A set of extensions to Ian Bicking’s virtualenv_ tool.
   Using a virtual environment will make the installation easier,
   and will help to avoid clutter in your system-wide libraries.
#. Mercurial_. Version control used by rst2html5 project.


::

    sudo apt-get install python-dev python-pip mercurial
    sudo pip install virtualenvwrapper

Add these two lines to :code:`~/.bashrc`::

    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh


Project Setup
=============

#. Clone the repository::

    $ hg clone http://www.bitbucket.org/andre_felipe_dias/rst2html5
    $ cd rst2html5

#. Make a new virtual enviroment for development::

    $ mkvirtualenv rst2html5

#. Install project's requirements::

    $ pip install -r requirements.txt -r dev_test_requirements.txt

Now you are ready!

.. note::

    To come back to the virtualenv in another session,
    use the command :code:`workon rst2html5`.

.. seealso::

    * `Virtualenvwrapper command reference`_


.. _test suite:

Running the test suite
======================

To run the tests, just type the following on a terminal::

    $ nosetests

To get a complete test verification, run::

    $ tox

The complete tests save some interesting metrics at :file:`rst2html5/.tox/metrics/log`.

.. important::

    Before sending a patch or a pull request,
    ensure that all tests pass and there is no flake8 error or warning codes.


Documentation
=============

Contributing to documentation is as simple as
editing the specified file in the :literal:`docs` directory.
We use restructuredtext markup and Sphinx_ for building the documentation.


.. _reporting an issue:

Reporting an issue
==================

Proposals, enhancements, bugs or tasks should be directly reported on BitBucket `issue tracker`_.

If there are issues please let us know so we can improve rst2html5.
If you don’t report it, we probably won't fix it.
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

While it's handy to provide useful code snippets in an issue,
it is better for you as a developer to submit pull requests.
By submitting pull request your contribution to ``rst2html5`` will be recorded by BitBucket.

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

.. _pip: https://pip.pypa.io/en/latest/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _Mercurial: http://mercurial.selenic.com/
.. _Virtualenvwrapper command reference: http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html
.. _rst2html5 project: https://bitbucket.org/andre_felipe_dias/rst2html5
.. _Sphinx: http://sphinx-doc.org/
.. _issue tracker: http://www.bitbucket.org/andre_felipe_dias/rst2html5/issues
.. _twitter: https://twitter.com/andref_dias
.. _google plus: https://plus.google.com/100373126641024342168
