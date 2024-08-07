# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'ist5001'
copyright = '2024'
author = 'IST5001'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_static_path = ['_static']

import sphinx_rtd_theme

extensions += [
    'sphinx_rtd_theme',
]

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

def setup(app):
    app.add_css_file('custom.css')
