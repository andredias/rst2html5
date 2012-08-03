Docutils has some functional tests at http://docutils.sourceforge.net/test/functional/input/
that can be used in rst2html5 also.
Although the html produced is quite different from the rst2html's one,
the functional results should be the same.

To analyze both, proceed as following::

$ rst2html html4css1.rst > /tmp/html4css1.html
$ rst2html5 html4css1.rst > /tmp/html5.html

Open both htmls in a browser and see the results.