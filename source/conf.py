# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys, os

sys.path.insert(0, os.path.abspath("..."))


# -- Project information -----------------------------------------------------

project = "FLO-2D Tutorials"
copyright = "2022, Karen O'Brien"
author = "Karen O'Brien"
html_logo = "FLO-2D_logo.jpg"
# -- General configuration ---------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["style"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_static_path = ["style"]
html_css_files = ["static/style.css"]

# -- Options for DOCX output ------------------------------------------------

extensions = [
    # other extensions...
    'sphinx.ext.intersphinx',
]

docx_documents = [
    ('index', 'FLO-2D Tutorials.docx', {
         'title': 'FLO-2D Plugin for QGIS Tutorials',
         'created': 'Karen O\'Brien',
         'subject': 'Sphinx builder extension',
         'keywords': ['sphinx']
     }, True),
]
docx_pagebreak_before_section = 1

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
