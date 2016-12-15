# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.rfd17


class PlonethemeRfd17Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.rfd17)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.rfd17:default')


PLONETHEME_RFD17_FIXTURE = PlonethemeRfd17Layer()


PLONETHEME_RFD17_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_RFD17_FIXTURE,),
    name='PlonethemeRfd17Layer:IntegrationTesting'
)


PLONETHEME_RFD17_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_RFD17_FIXTURE,),
    name='PlonethemeRfd17Layer:FunctionalTesting'
)


PLONETHEME_RFD17_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_RFD17_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeRfd17Layer:AcceptanceTesting'
)
