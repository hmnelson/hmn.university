# -*- coding: utf-8 -*-
from hmn.university.content.course import ICourse  # NOQA E501
from hmn.university.testing import HMN_UNIVERSITY_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class CourseIntegrationTest(unittest.TestCase):

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

    def test_ct_course_schema(self):
        fti = queryUtility(IDexterityFTI, name="Course")
        schema = fti.lookupSchema()
        self.assertEqual(ICourse, schema)

    def test_ct_course_fti(self):
        fti = queryUtility(IDexterityFTI, name="Course")
        self.assertTrue(fti)

    def test_ct_course_factory(self):
        fti = queryUtility(IDexterityFTI, name="Course")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICourse.providedBy(obj),
            "ICourse not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_course_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.parent,
            type="Course",
            id="course",
        )

        self.assertTrue(
            ICourse.providedBy(obj),
            "ICourse not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("course", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("course", parent.objectIds())

    def test_ct_course_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Course")
        self.assertFalse(fti.global_allow, "{0} is globally addable!".format(fti.id))

    def test_ct_course_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Course")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "course_id",
            title="Course container",
        )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type="Document",
                title="My Content",
            )
