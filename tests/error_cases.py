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
            <h1>System Message: ERROR/3 (&lt;string&gt; line 1) <a href="#id2">id2</a></h1>
            <p>Unknown target name: "target".</p>
        </div>
    </section>
</body>
</html>''',
    'indent_output': True,
}

system_message_2 = {
    'rst': '''Target1__
Target2__

.. __: http://opensource.org/licenses/MIT
''',
    'out': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
</head>
<body>
    <p><a href="#id2" id="id3" class="problematic">Target1__</a> <a href="#id2" id="id4" \
class="problematic">Target2__</a></p>
    <section class="system-messages">
        <h1>Docutils System Messages</h1>
        <a id="id2"></a>
        <div>
            <h1>System Message: ERROR/3 (&lt;string&gt; line ) <a href="#id3">id3</a> \
<a href="#id4">id4</a></h1>
            <p>Anonymous hyperlink mismatch: 2 references but 1 targets. See "backrefs" \
attribute for IDs.</p>
        </div>
    </section>
</body>
</html>''',
    'indent_output': True,
}

problematic = {
    'rst': '''[2]_

.. [#] footnote''',
    'out': '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
</head>
<body>
    <p><a href="#id3" id="id4" class="problematic">[2]_</a></p>
    <table id="id2" class="footnote">
        <col />
        <col />
        <tbody>
            <tr>
                <th>[1]</th>
                <td>footnote</td>
            </tr>
        </tbody>
    </table>
    <section class="system-messages">
        <h1>Docutils System Messages</h1>
        <a id="id3"></a>
        <div>
            <h1>System Message: ERROR/3 (&lt;string&gt; line 1) <a href="#id4">id4</a></h1>
            <p>Unknown target name: "2".</p>
        </div>
    </section>
</body>
</html>''',
    'indent_output': True,
}