# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from nva.testbootstrap.testing import NVA_TESTBOOTSTRAP_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that nva.testbootstrap is properly installed."""

    layer = NVA_TESTBOOTSTRAP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if nva.testbootstrap is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'nva.testbootstrap'))

    def test_browserlayer(self):
        """Test that INvaTestbootstrapLayer is registered."""
        from nva.testbootstrap.interfaces import (
            INvaTestbootstrapLayer)
        from plone.browserlayer import utils
        self.assertIn(
            INvaTestbootstrapLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NVA_TESTBOOTSTRAP_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['nva.testbootstrap'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if nva.testbootstrap is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'nva.testbootstrap'))

    def test_browserlayer_removed(self):
        """Test that INvaTestbootstrapLayer is removed."""
        from nva.testbootstrap.interfaces import \
            INvaTestbootstrapLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            INvaTestbootstrapLayer,
            utils.registered_layers())
