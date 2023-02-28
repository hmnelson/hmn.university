# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import hmn.university


class HmnUniversityLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=hmn.university)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "hmn.university:default")


HMN_UNIVERSITY_FIXTURE = HmnUniversityLayer()


HMN_UNIVERSITY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(HMN_UNIVERSITY_FIXTURE,),
    name="HmnUniversityLayer:IntegrationTesting",
)


HMN_UNIVERSITY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(HMN_UNIVERSITY_FIXTURE,),
    name="HmnUniversityLayer:FunctionalTesting",
)


HMN_UNIVERSITY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        HMN_UNIVERSITY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="HmnUniversityLayer:AcceptanceTesting",
)
