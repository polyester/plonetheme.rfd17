# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plonetheme.rfd17.testing import PLONETHEME_RFD17_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.rfd17 is properly installed."""

    layer = PLONETHEME_RFD17_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.rfd17 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.rfd17'))

    def test_browserlayer(self):
        """Test that IPlonethemeRfd17Layer is registered."""
        from plonetheme.rfd17.interfaces import (
            IPlonethemeRfd17Layer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeRfd17Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_RFD17_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.rfd17'])

    def test_product_uninstalled(self):
        """Test if plonetheme.rfd17 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.rfd17'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeRfd17Layer is removed."""
        from plonetheme.rfd17.interfaces import \
            IPlonethemeRfd17Layer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeRfd17Layer, utils.registered_layers())
