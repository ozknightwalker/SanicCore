from __future__ import unicode_literals

import unittest

from core.exceptions import ImproperlyConfigured


class ImproperlyConfiguredTestCase(unittest.TestCase):

    def test_raises_exception(self):
        with self.assertRaises(ImproperlyConfigured):
            raise ImproperlyConfigured()
