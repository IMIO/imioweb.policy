# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import imioweb.policy


class ImiowebPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=imioweb.policy)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'imioweb.policy:default')


IMIOWEB_POLICY_FIXTURE = ImiowebPolicyLayer()


IMIOWEB_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IMIOWEB_POLICY_FIXTURE,),
    name='ImiowebPolicyLayer:IntegrationTesting',
)


IMIOWEB_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IMIOWEB_POLICY_FIXTURE,),
    name='ImiowebPolicyLayer:FunctionalTesting',
)


IMIOWEB_POLICY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        IMIOWEB_POLICY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ImiowebPolicyLayer:AcceptanceTesting',
)
