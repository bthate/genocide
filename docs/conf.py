#!/usr/bin/env python3
# GENOCIDE - the king of the netherlands commits genocide
# -*- coding: utf-8 -*-
#

import unittest
import doctest
import sys
import os

sys.path.insert(0, os.getcwd())

#curdir = os.path.abspath(".")
curdir = os.getcwd()

__version__ = 10

from triple.req import __version__

from sphinx.ext import autodoc
from sphinx.util import inspect
autodoc.repr = inspect.repr = str

needs_sphinx='1.1'
nitpick_ignore=[
                ('py:class', 'builtins.BaseException'),
               ]

extensions=[
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
]

html_theme_options = {
     "nosidebar": False,
     'body_max_width': '90%'
}

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
#html_static_path = ['_static']
sphinx_style="pyramid"
autosummary_generate=True
autodoc_default_flags=['members', 'undoc-members', 'private-members', "imported-members", 'show-inheritance']
autodoc_docstring_signature=True
autodoc_inherit_docstrings=False
autodoc_member_order='bysource'
autodoc_typehints="description"
autoclass_content="class"
doctest_global_setup=""
doctest_global_cleanup=""
doctest_test_doctest_blocks="default"
trim_doctest_flags=True
doctest_flags=doctest.REPORT_UDIFF
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
project = "GENOCIDE"
version = '%s' % __version__
release = '%s' % __version__
language = ''
today = ''
today_fmt = '%B %d, %Y'
exclude_patterns = ['txt', '_build', "_sources", "_templates"]
default_role = ''
add_function_parentheses = True
add_module_names = False
show_authors = False
pygments_style = 'sphinx'
modindex_common_prefix = [""]
keep_warnings = True
html_short_title = "GENOCIDE %s" % __version__
html_favicon = "smile3.png"
html_extra_path = []
html_last_updated_fmt = '%Y-%b-%d'
html_additional_pages = {}
html_domain_indices = False
html_use_index = False
html_split_index = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
html_copy_source = False
html_use_opensearch = 'http://genocide.rtfd.io/'
html_file_suffix = '.html'
rst_prolog = """.. image:: genocideline2.png
    :width: 100%

.. title:: OTP-CR-117/19/001 | otp.informationdesk@icc-cpi.int | https://genocide.rtfd.io

""" 
htmlhelp_basename = 'pydoc'
intersphinx_mapping = {
                       'python': ('https://docs.python.org/3', 'objects.inv'),
                       'sphinx': ('http://sphinx.pocoo.org/', None),
                      }
intersphinx_cache_limit=1
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': '',

    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',
}

