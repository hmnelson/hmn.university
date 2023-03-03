# -*- coding: utf-8 -*-
from __future__ import absolute_import

from Acquisition import aq_inner
from hmn.university import _
from plone import schema
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from z3c.form import field
from zope.component import getMultiAdapter
from zope.interface import implementer

import json
import six.moves.urllib.error
import six.moves.urllib.parse
import six.moves.urllib.request


class IDepartmentCoursesPortlet(IPortletDataProvider):
    """"""

    # place_str = schema.TextLine(
    #    title=_("Name of your place with country code"),
    #    description=_("City name along with country code i.e Delhi,IN"),  # NOQA: E501
    #    required=True,
    #    default="delhi,in",
    # )


@implementer(IDepartmentCoursesPortlet)
class Assignment(base.Assignment):
    schema = IDepartmentCoursesPortlet

    # def __init__(self, place_str="delhi,in"):
    #    self.place_str = place_str.lower()

    @property
    def title(self):
        return _("Department Courses Portlet")


class AddForm(base.AddForm):
    schema = IDepartmentCoursesPortlet
    form_fields = field.Fields(IDepartmentCoursesPortlet)
    label = _("Add Department Courses portlet")
    description = _("Menu of links for managing department courses.")

    def create(self, data):
        return Assignment(
            # place_str=data.get("place_str", "delhi,in"),
        )


class EditForm(base.EditForm):
    schema = IDepartmentCoursesPortlet
    form_fields = field.Fields(IDepartmentCoursesPortlet)
    label = _("Edit Department Courses portlet")
    description = _(
        "This portlet displays a menu of links for managing department courses."
    )


class Renderer(base.Renderer):
    schema = IDepartmentCoursesPortlet
    _template = ViewPageTemplateFile("department_courses_portlet.pt")

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        context = aq_inner(self.context)
        portal_state = getMultiAdapter(
            (context, self.request), name="plone_portal_state"
        )
        self.anonymous = portal_state.anonymous()

    def render(self):
        return self._template()

    @property
    def available(self):
        """Show the portlet only if there are one or more elements and
        not an anonymous user."""
        return not self.anonymous
