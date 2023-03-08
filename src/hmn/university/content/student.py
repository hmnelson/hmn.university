# -*- coding: utf-8 -*-
from hmn.university import _
from plone.app.textfield import RichText

from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset

# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.interface import invariant
from zope.interface import Invalid
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from hmn.university.browser.widgets.price_radio_widget import PriceRadioFieldWidget


vocab_gender = SimpleVocabulary(
    [
        SimpleTerm(value="female", title=_("Female")),
        SimpleTerm(value="male", title=_("Male")),
        SimpleTerm(value="nonbinary", title=_("Nonbinary")),
        SimpleTerm(value="unspecified", title=_("Unspecified")),
    ]
)


class IStudent(model.Schema):
    """Marker interface and Dexterity Python Schema for Student"""
    firstName = schema.TextLine(title=_("First name"), required=True)
    lastName = schema.TextLine(title=_("Last name"), required=True)
    # studentName = schema.TextLine(title=_("Name of student"), required=True)
    age = schema.TextLine(title=_("Age of student"), required=True)
    gender = schema.Choice(title=_("Gender"), vocabulary=vocab_gender, required=False)
    directives.widget(studentHourlyRate=PriceRadioFieldWidget)
    studentHourlyRate = schema.Float(title=_(u'Hourly Rate'), required=False)
    bio = RichText(title=_("Biography"), required=False)
    studentPhoto = namedfile.NamedBlobImage(title=_("Student photo"), required=False)

    fieldset("Photo", fields=["studentPhoto"])
    fieldset("Bio", fields=["bio"])

    @invariant
    def validateNumber(data):
        if data.age:
            if not str(data.age).isdigit():
                raise Invalid(_("Age of student must be a number"))
            else:
                if int(data.age) >= 110:
                    raise Invalid(_("%s?! Are you kidding?!" % data.age))

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('student.xml')

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


@implementer(IStudent)
class Student(Item):
    """Content-type class for IStudent"""

    def Title(self):
        if self.firstName or self.lastName:
            return f"{self.firstName} {self.lastName}".strip()
        else:
            return self.getId()


