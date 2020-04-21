=========================
Contributing to rst2html5
=========================

Contributions are welcome!
So don't be afraid to contribute with anything that you think will be helpful.
Help with maintaining the English documentation is particularly appreciated.

The `rst2html5 project <https://foss.heptapod.net/doc-utils/rst2html5>`_
is hosted on Heptapod by Octobus and Clever Cloud!


How to contribute
=================

Please, follow the procedure:

#. Check for the open issues or open a new issue on the Heptapod `issue tracker`_
   to start a discussion about a feature or a bug.
#. Fork the `rst2html5 project`_ and start making your modifications.
#. Send a merge request.


Installing OS Packages
======================

You will need:

#. pipenv_. A tool for installing and managing Python packages.
#. Mercurial_. Version control used by rst2html5 project.



Project Setup
=============

::

    $ hg clone https://foss.heptapod.net/doc-utils/rst2html5
    $ cd rst2html5
    $ pipenv install --dev
    $ pipenv shell

Now you are ready!


.. _test suite:

Running the test suite
======================

To run the tests, just type the following on a terminal::

    $ nosetests


.. important::

    Before sending a patch or a merge request,
    ensure that all tests pass and there is no flake8 error or warning codes.


Documentation
=============

Contributing to documentation is as simple as
editing the specified file in the :literal:`docs` directory.
We use restructuredtext markup and Sphinx_ for building the documentation.


.. _reporting an issue:

Reporting an issue
==================

Proposals, enhancements, bugs or tasks should be directly reported on Heptapod `issue tracker`_.

If there are issues please let us know so we can improve rst2html5.
If you don’t report it, we probably won't fix it.
When creating a bug issue, try to provide the following information at least:

#. Steps to reproduce the bug
#. The resulting output
#. The expected output

..
    #. What version of ``rst2html5`` you are using
    #. Any additional relevant information

.. tip::

    See https://foss.heptapod.net/doc-utils/rst2html5/issues/1 as a reference.

For proposals or enhancements,
you should provide input and output examples.
Whenever possible, you should also provide external references to articles or documentation
that endorses your request.

While it's handy to provide useful code snippets in an issue,
it is better for you as a developer to submit merge requests.
By submitting pull request your contribution to ``rst2html5`` will be recorded by Heptapod.

..
    Sending a pull request
    ======================

    #. Test what you code. Any new code should have one or more test cases. See :ref:`tests`.
    #. Don't mix code changes with whitespace cleanup.


Contacting the author
=====================

``rst2html5`` is written and maintained by André Felipe Dias.
You can reach me at Twitter_ or by email (andre.dias@pronus.io).

.. _pipenv: https://pypi.org/project/pipenv/
.. _Mercurial: https://www.mercurial-scm.org/
.. _rst2html5 project: https://foss.heptapod.net/doc-utils/rst2html5
.. _Sphinx: http://sphinx-doc.org/
.. _issue tracker: https://foss.heptapod.net/doc-utils/rst2html5/issues
.. _Twitter: https://twitter.com/andref_dias
