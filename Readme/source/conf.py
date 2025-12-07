
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SPHY Pre-Processing Tool'
copyright = '2025, jingheng'
author = 'jingheng'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = [
#     "sphinx.ext.autodoc",
#     "myst_parser",
#     ]

extensions = [
    "sphinx.ext.autodoc",
    "myst_parser",
    "sphinx.ext.mathjax",
    ]



templates_path = ['_templates']
exclude_patterns = []

language = 'yes'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
# # html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

myst_enable_extensions = [
    "amsmath",    # 支持 {math} 环境
    "dollarmath"  # 支持 $...$、$$...$$、\(...\)、\[...\]
]