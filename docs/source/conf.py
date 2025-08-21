# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Avnir Models documentation"
copyright = "2024-2025, Avnir"
author = "Avnir"

release = ""
version = ""

# -- General configuration

extensions = [
    "sphinx.ext.autodoc",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]
html_extra_path = []
# -- Options for HTML output

html_theme = "furo"

html_logo = "assets/logo_avnir_long.png"

html_theme_options = {}

html_title = "Avnir Models Documentation Manual"

extensions = ["myst_parser"]

source_suffix = [".rst", ".md"]
