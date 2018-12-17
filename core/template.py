from __future__ import unicode_literals

import sys

from jinja2 import Environment, PackageLoader, select_autoescape

# Enabling async template execution which allows you to take advantage
# of newer Python features requires Python 3.6 or later.
enable_async = sys.version_info >= (3, 6)

template_env = Environment(
    loader=PackageLoader('core'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=enable_async,
)
