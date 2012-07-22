#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.1'

from docutils.writers import html4css1

class Writer(html4css1.Writer):

	supported = ('html', 'xhtml', 'html5', 'html5css3')

	def __init__(self):
		html4css1.Writer.__init__(self)
		self.translator_class = HTMLTranslator


class HTMLTranslator(html4css1.HTMLTranslator):
	pass
