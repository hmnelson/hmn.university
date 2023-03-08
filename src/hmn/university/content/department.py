# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
# from plone.namedfile import field as namedfile
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from hmn.university import _
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer
import datetime

class IDepartment(model.Schema):
    """Marker interface and Dexterity Python Schema for Department"""
    
    college = schema.Choice(
        title=_(u"College to which this department belongs"), 
        vocabulary="department_college"
    )

    accredited = schema.Bool(
        title=_(u'Department is accredited'),
        default=False
    )

    department_created_date = schema.Date(
        title=_(u'Date this department was instituted'), 
        min=datetime.date(1600, 1, 1),
        default=datetime.date(1900, 1, 1), 
        required=False
    )

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('department.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(IDepartment)
class Department(Container):
    """Content-type class for IDepartment"""

    def totalStudents(self):
        path = "/".join(self.getPhysicalPath())
        query_dict = {
            "path": path,
            "portal_type": "Student",
            "depth": 1,
        }
        result = self.portal_catalog.searchResults(query_dict)
        return len(result)

    def totalTeachers(self):
        path = "/".join(self.getPhysicalPath())
        query_dict = {
            "path": path,
            "portal_type": "Teacher",
            "depth": 1,
        }
        result = self.portal_catalog.searchResults(query_dict)
        return len(result)

    def totalCourses(self):
        path = "/".join(self.getPhysicalPath())
        query_dict = {
            "path": path,
            "portal_type": "Course",
            "depth": 1,
        }
        result = self.portal_catalog.searchResults(query_dict)
        return len(result)
