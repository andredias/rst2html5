===================
rst2html5 Changelog
===================

Here you can see the full list of changes between each rst2html5 releases.


1.8 - 2016-06-04
================

* New directives :code:`define`, :code:`undef`, :code:`ifdef` and :code:`ifndef`
  to conditionally include (or not) a rst snippet.

1.7.5 - 2015-05-14
==================

* fixes the stripping of leading whitespace from the highlighted code

1.7.4 - 2015-04-09
==================

* fixes deleted blank lines in <table><pre> during Genshi rendering
* Testing does not depend on ordered tag attributes anymore

1.7.3 - 2015-04-04
==================

* fix some imports
* Sphinx dependency removed

1.7.2 - 2015-03-31
==================

* Another small bugfix related to imports

1.7.1 - 2015-03-31
==================

* Fix 1.7 package installation. :literal:`requirements.txt` was missing

1.7 - 2015-03-31
================

* Small bufix in setup.py
* LICENSE file added to the project
* Sublists are not under <blockquote> anymore
* Never a <p> as a <li> first child
* New CodeBlock directive merges docutils and sphinx CodeBlock directives
* Generated codeblock cleaned up to a more HTML5 style: <pre data-language="...">...</pre>

1.6 - 2015-03-09
================

* code-block's :literal:`:class:` value should go to <pre class="value"> instead of <pre><code class="value">
* Fix problem with no files uploaded to Pypi in 1.5 version


1.5 - 2015-23-02
================

* rst2html5 generates html5 comments
* A few documentation improvementss

1.4 - 2014-09-21
================

* Improved packaging
* Using tox for testing management
* Improved compatibility to Python3
* Respect initial_header_level_setting
* Container and compound directives map to div
* rst2html5 now process field_list nodes
* Additional tests
* Multiple-time options should be specified multiple times, not with commas
* Metatags are declared at the top of head
* Only one link to mathjax script is generated


1.3 - 2014-04-21
================

* Fixes #16 | New --template option
* runtests.sh without parameter should keep current virtualenv


1.2 - 2014-02-16
================

* Fix doc version


1.1 - 2014-02-16
================

* rst2html5 works with docutils 0.11 and Genshi 0.7


1.0 - 2013-06-17
================

* Documentation improvement
* Added html-tag-attr, script-defer and script-async options
* Dropped option-limit option
* Fix bug with caption generation within table
* Footer should be at the bottom of the page
* Indent raw html
* field-limit and option-limit are set to 0 (no limit)


0.10 - 2013-05-11
=================

* Support docutils 0.10
* Force syntax_hightlight to 'short'
* Conforming to PEP8 and PyFlakes
* Testing structure simplified
* rst2html5.py refactored
* Some bugfixes

0.9 - 2012-08-03
================

* First public preview release
