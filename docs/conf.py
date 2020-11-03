# -*- coding: utf-8 -*-
# GENOCIDE - the king of the netherlands commits genocide
#
#

import doctest, os, sys, unittest

curdir = os.getcwd()
sys.path.insert(0, curdir + os.sep)
#sys.path.insert(0, curdir + os.sep + '..' + os.sep)
#sys.path.insert(0, curdir + os.sep + '..' + os.sep + ".." + os.sep)

from triple.req import __version__

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

project = "genocide"
version = '%s' % __version__
release = '%s' % __version__
language = ''
today = ''
today_fmt = '%B %d, %Y'
exclude_patterns = ['_build', "_sources", "_templates"]
default_role = ''
add_function_parentheses = True
add_module_names = False
show_authors = True
pygments_style = 'sphinx'
modindex_common_prefix = [""]
keep_warnings = True
html_theme = "haiku"
html_theme_path = []
#html_short_title = "GENOCIDE %s" % __version__
html_short_title=""
html_favicon = "genocidesmile.png"
html_static_path = []
html_extra_path = []
html_last_updated_fmt = '%Y-%b-%d'
html_additional_pages = {}
html_domain_indices = True
html_use_index = True
html_split_index = True
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
html_copy_source = False
html_use_opensearch = 'http://genocide.rtfd.io/'
html_file_suffix = '.html'
rst_prolog = """.. image:: genocideline2.png
    :height: 2.7cm
    :width: 95%
    
.. title:: OTP-CR-117/19 | otp.informationdesk@icc-cpi.int

"""

autosummary_generate=True
autodoc_default_flags=['members', 'undoc-members', 'private-members', "imported-members"]
#autodoc_member_order='alphabetical'
autodoc_member_order='groupwise'
autodoc_docstring_signature=True
autoclass_content="class"
doctest_global_setup=""
doctest_global_cleanup=""
doctest_test_doctest_blocks="default"
trim_doctest_flags=True
doctest_flags=doctest.REPORT_UDIFF
templates_path=['_templates',]
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
