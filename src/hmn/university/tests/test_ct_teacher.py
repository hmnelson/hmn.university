# -*- coding: utf-8 -*-
from hmn.university.content.teacher import ITeacher  # NOQA E501
from hmn.university.testing import HMN_UNIVERSITY_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class TeacherIntegrationTest(unittest.TestCase):

    layer = HMN_UNIVERSITY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            "Department",
            self.portal,
            "parent_container",
            title="Parent container",
        )
        self.parent = self.portal[parent_id]

    def test_ct_teacher_schema(self):
        fti = queryUtility(IDexterityFTI, name="Teacher")
        schema = fti.lookupSchema()
        self.assertEqual(ITeacher, schema)

    def test_ct_teacher_fti(self):
        fti = queryUtility(IDexterityFTI, name="Teacher")
        self.assertTrue(fti)

    def test_ct_teacher_factory(self):
        fti = queryUtility(IDexterityFTI, name="Teacher")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ITeacher.providedBy(obj),
            "ITeacher not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_teacher_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.parent,
            type="Teacher",
            id="teacher",
        )

        self.assertTrue(
            ITeacher.providedBy(obj),
            "ITeacher not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("teacher", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("teacher", parent.objectIds())

    def test_ct_teacher_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Teacher")
        self.assertFalse(fti.global_allow, "{0} is globally addable!".format(fti.id))
