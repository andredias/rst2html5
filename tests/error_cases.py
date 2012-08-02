#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains test data to rst2html5 in the form:
# case = {'rst': rst_text, 'out': expected_output, ...}

from __future__ import unicode_literals

# stderr should present: <string>:1: (ERROR/3) Unknown target name: "target"
system_message = {
    'rst': 'target_',
    'out': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
</head>
<body>
    <p><a href="#id1" id="id2" class="problematic">target_</a></p>
    <section class="system-messages">
        <h1>Docutils System Messages</h1>
        <a id="id1"></a>
        <div>
            <h1>System Message: ERROR/3 (&lt;string&gt; line 1) <a href="#id2">Backref</a></h1>
            <p>Unknown target name: "target".</p>
        </div>
    </section>
</body>
</html>''',
    'indent_output': True,
}

def local_file_content(filename):
    from os.path import split, join
    from codecs import open
    local_path = join(split(__file__)[0], filename)
    with open(local_path, 'r', 'utf-8') as f:
        return f.read()

docutils_test_case = {
    'rst': local_file_content('docutils.html4css1.rst'),
    'out': local_file_content('rst2html5_result.html'),
    'indent_output': True,
    'option_limit': 14,
}