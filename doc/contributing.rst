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

There are various possibilities to get involved, for example you can:

* :ref:`reporting an issue`;
* Enhance this `documentation <https://bitbucket.org/andre_felipe_dias/rst2html5/src/tip/doc>`_;
* `Fork the project <http://www.bitbucket.org/andre_felipe_dias/rst2html5/>`_,
  implement new features, :ref:`test <test suite>` and send a pull request.


Setup
=====

#. Clone the repository using `Mercurial <http://mercurial.selenic.com/>`_::

    $ hg clone http://www.bitbucket.org/andre_felipe_dias/rst2html5 ~/rst2html5

#. Install `virtualenv <http://pypi.python.org/pypi/virtualenv>`_ if you do not already have it.
   Using a virtual environment will make the installation easier,
   and will help to avoid clutter in your system-wide libraries.

#. Create a virtual environment and activate it::

    $ virtualenv ~/rst2html5/env
    $ source ~/rst2html5/env/bin/activate

#. Install project's requirements via `pip <https://pypi.python.org/pypi/pip>`_::

    $ cd ~/rst2html5
    $ pip install -r requirements.txt -r test_requirements.txt

Now you are ready to hack it!

.. _test suite:

Running the test suite
======================

To run the tests, just type the following on a terminal::

    $ nosetests

To get some metrics, try::

    $ flake8 --exclude="env,build,doc" .

To get a complete test verification, run::

    $ ./runtests.sh

The complete tests save interesting metrics at :file:`rst2html5/metrics`.

Before


.. _reporting an issue:

Reporting an issue
==================

Proposals, enhancements, bugs or tasks should be directly reported on BitBucket `issue tracker`_.

When creating a bug issue, try to provide the following information at least:

#. Steps to reproduce the bug
#. The produced output
#. The expected output

.. tip::

    See https://bitbucket.org/andre_felipe_dias/rst2html5/issue/1 as a reference.

To proposals or enhancements,
you should provide input and output examples.
Whenever it is possible, you should also provide external references to articles or documentation
that endorses your request.

While it's handy to provide useful code snippets in an issue, it is better for
you as a developer to submit pull requests. By submitting pull request your
contribution to ``rst2html5`` will be recorded by BitBucket.





How to get your pull request accepted
=====================================

We want your submission.
But we also want to provide a stable experience for our users and the community.
Follow these rules and you should succeed without a problem!

Run the tests!
--------------

Before you submit a pull request, please run the entire OpenComparison test suite via::

    python manage.py test --settings=settings.test

The first thing the core committers will do is run this command. Any pull request that fails this test suite will be **rejected**.

If you add code/views you need to add tests!
--------------------------------------------

We've learned the hard way that code without tests is undependable. If your pull request reduces our test coverage because it lacks tests then it will be **rejected**.

For now, we use the Django Test framework (based on unittest).

Also, keep your tests as simple as possible. Complex tests end up requiring their own tests. We would rather see duplicated assertions across test methods then cunning utility methods that magically determine which assertions are needed at a particular stage. Remember: `Explicit is better than implicit`.

Don't mix code changes with whitespace cleanup
----------------------------------------------

If you change two lines of code and correct 200 lines of whitespace issues in a file the diff on that pull request is functionally unreadable and will be **rejected**. Whitespace cleanups need to be in their own pull request.

Keep your pull requests limited to a single issue
--------------------------------------------------

OpenComparison pull requests should be as small/atomic as possible. Large, wide-sweeping changes in a pull request will be **rejected**, with comments to isolate the specific code in your pull request. Some examples:

#. If you are making spelling corrections in the docs, don't modify the settings.py file (pydanny_ is guilty of this mistake).
#. Adding a new `repo handler`_ must not touch the Package model or its methods.
#. If you are adding a new view don't '*cleanup*' unrelated views. That cleanup belongs in another pull request.
#. Changing permissions on a file should be in its own pull request with explicit reasons why.

Follow PEP-8 and keep your code simple!
---------------------------------------

Memorize the Zen of Python::

    >>> python -c 'import this'

Please keep your code as clean and straightforward as possible. When we see more than one or two functions/methods starting with `_my_special_function` or things like `__builtins__.object = str` we start to get worried. Rather than try and figure out your brilliant work we'll just **reject** it and send along a request for simplification.

Furthermore, the pixel shortage is over. We want to see:

* `package` instead of `pkg`
* `grid` instead of `g`
* `my_function_that_does_things` instead of `mftdt`

Test any css/layout changes in multiple browsers
------------------------------------------------

Any css/layout changes need to be tested in Chrome, Safari, Firefox, IE8, and IE9 across Mac, Linux, and Windows. If it fails on any of those browsers your pull request will be **rejected** with a note explaining which browsers are not working.

How pull requests are checked, tested, and done
===============================================

First we pull the code into a local branch::

    git checkout -b <branch-name> <submitter-github-name
    git pull git://github.com/<submitter-github-name/django-twoscoops-project.git develop

Then we run the tests::

    ./runtests.py

We finish with a merge and push to GitHub::

    git checkout develop
    git merge <branch-name>
    git push origin develop



Author
======

rst2html5 is written and maintained by André Felipe Dias.
You can reach me at `google plus`_ or twitter_.

.. _issue tracker: http://www.bitbucket.org/andre_felipe_dias/rst2html5/issues
.. _twitter: https://twitter.com/andref_dias
.. _google plus: https://plus.google.com/100373126641024342168

