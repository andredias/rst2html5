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

#. Poetry_. A tool for installing and managing Python packages.
#. Mercurial_. Version control used by rst2html5 project.

.. note::

    Also, it is possible to contribute with Git using `rst2html5's GitHub mirror`_.



Project Setup
=============

::

    $ hg clone https://foss.heptapod.net/doc-utils/rst2html5
    $ cd rst2html5
    $ poetry install
    $ poetry shell

Now you are ready!


.. _test suite:

Running the test suite
======================

To run the tests, just type the following on a terminal::

    $ make test

.. attention::

    Before executing that command,
    the virtual environment must be activated,
    or simply use ``poetry run make test`` instead.


Development Tasks
=================

`Makefile <Makefile>`_ contains several development tasks,
all grouped in one place:

.. csv-table::
    :header-rows: 1

    Task Name, Description
    ``test``, Lint and then test the code
    ``lint``, Run the various linters
    ``format``, Format the code according to the linters
    ``docs``, Create the project documentation using Sphinx


To run a task, execute::

    $ poetry run make <task>

.. tip::

    If the virtual environment is already activated,
    prefixing the command with ``poetry run`` is not necessary.


``pre-commit`` and ``pre-push`` Hooks
=====================================

It is important that you run ``make lint`` and ``make test``
before committing and pushing code.
To guarantee that,
I suggest that you use version control hooks for ``pre-commit`` and ``pre-push`` events.


Mercurial Hooks
---------------

For Mercurial_, add this section in ``.hg/hgrc``:

.. code:: ini

    [hooks]
    precommit.lint = (cd `hg root`; poetry run make lint)
    pre-push.test = (cd `hg root`; poetry run make test)

.. tip::

    Execute ``hg help config`` to get more information about Mercurial
    configuration. There is a section about hooks there.

    Also, visit `this link about Mercurial Hooks <https://www.mercurial-scm.org/wiki/Hook>`_.


Git Hooks
---------

``Git`` hooks are based on files. So, you need two of them:
``.git/hooks/pre-commit`` and ``.git/hooks/pre-push``.

``pre-commit``:

.. code:: bash

    #!/bin/bash

    cd $(git rev-parse --show-toplevel)
    poetry run make lint


``pre-push``:

.. code:: bash

    #!/bin/bash

    cd $(git rev-parse --show-toplevel)
    poetry run make test


.. important::

    Both ``.git/hooks/pre-commit`` and ``.git/hooks/pre-push`` must be executable scripts.
    Use ``chmod +x`` on them.


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
By submitting a merge request,
your contribution to ``rst2html5`` will be recorded by Heptapod.

..
    Sending a pull request
    ======================

    #. Test what you code. Any new code should have one or more test cases. See :ref:`tests`.
    #. Don't mix code changes with whitespace cleanup.


Contacting the author
=====================

``rst2html5`` is written and maintained by André Felipe Dias.
You can reach me at Twitter_ or by email (andre.dias@pronus.io).

.. _Poetry: https://python-poetry.org/
.. _Mercurial: https://www.mercurial-scm.org/
.. _rst2html5 project: https://foss.heptapod.net/doc-utils/rst2html5
.. _Sphinx: http://sphinx-doc.org/
.. _issue tracker: https://foss.heptapod.net/doc-utils/rst2html5/issues
.. _Twitter: https://twitter.com/andref_dias
.. _`rst2html5's GitHub mirror`: https://github.com/andredias/rst2html5
