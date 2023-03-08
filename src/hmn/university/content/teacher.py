# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from hmn.university import _
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.interface import invariant
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


vocab_rank = SimpleVocabulary(
    [
        SimpleTerm(value="full", title=_("Professor")),
        SimpleTerm(value="associate", title=_("Associate Professor")),
        SimpleTerm(value="assistant", title=_("Assistant Professor")),
        SimpleTerm(value="emeritus", title=_("Emeritus Professor")),
    ]
)


class ITeacher(model.Schema):
    """Marker interface and Dexterity Python Schema for Teacher"""

    teacherName = schema.TextLine(title=_("Teacher name"), required=True)

    facultyRank = schema.Choice(
        title=_("Faculty rank"), vocabulary=vocab_rank, required=True
    )

    teacherPhoto = namedfile.NamedBlobImage(title=_("Teacher photo"), required=False)

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('teacher.xml')

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


@implementer(ITeacher)
class Teacher(Item):
    """Content-type class for ITeacher"""
