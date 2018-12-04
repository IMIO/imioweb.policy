# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from imioweb.policy.testing import IMIOWEB_POLICY_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that imioweb.policy is properly installed."""

    layer = IMIOWEB_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if imioweb.policy is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'imioweb.policy'))

    def test_browserlayer(self):
        """Test that IImiowebPolicyLayer is registered."""
        from imioweb.policy.interfaces import (
            IImiowebPolicyLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IImiowebPolicyLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = IMIOWEB_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['imioweb.policy'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if imioweb.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'imioweb.policy'))

    def test_browserlayer_removed(self):
        """Test that IImiowebPolicyLayer is removed."""
        from imioweb.policy.interfaces import \
            IImiowebPolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IImiowebPolicyLayer,
            utils.registered_layers())
