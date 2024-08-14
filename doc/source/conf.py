import os
import sys
import django


sys.path.insert(0, os.path.abspath('../..'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
django.setup()


project = 'Orange County Lettings'
copyright = '2024, Jérémie Silva'
author = 'Jérémie Silva'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
]
autodoc_mock_imports = [
    "some_external_dependency",
    "another_dependency"
]
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
