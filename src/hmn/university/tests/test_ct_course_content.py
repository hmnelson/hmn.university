# -*- coding: utf-8 -*-
from hmn.university.content.course_content import ICourseContent  # NOQA E501
from hmn.university.testing import HMN_UNIVERSITY_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class CourseContentIntegrationTest(unittest.TestCase):

    layer = HMN_UNIVERSITY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            "Course",
            self.portal,
            "parent_container",
            title="Parent container",
        )
        self.parent = self.portal[parent_id]

    def test_ct_course_content_schema(self):
        fti = queryUtility(IDexterityFTI, name="Course content")
        schema = fti.lookupSchema()
        self.assertEqual(ICourseContent, schema)

    def test_ct_course_content_fti(self):
        fti = queryUtility(IDexterityFTI, name="Course content")
        self.assertTrue(fti)

    def test_ct_course_content_factory(self):
        fti = queryUtility(IDexterityFTI, name="Course content")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICourseContent.providedBy(obj),
            "ICourseContent not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_course_content_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.parent,
            type="Course content",
            id="course_content",
        )

        self.assertTrue(
            ICourseContent.providedBy(obj),
            "ICourseContent not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("course_content", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("course_content", parent.objectIds())

    def test_ct_course_content_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="Course content")
        self.assertFalse(fti.global_allow, "{0} is globally addable!".format(fti.id))
