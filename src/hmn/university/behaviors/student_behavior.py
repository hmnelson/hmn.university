from plone.app.content.interfaces import INameFromTitle
# from plone.autoform import directives
# from plone.autoform.interfaces import IFormFieldProvider
# from plone.rfc822.interfaces import IPrimaryFieldInfo
# from plone.supermodel import model
# from Products.CMFPlone.utils import safe_hasattr
# from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
# from zope.interface import provider
# import datetime
import string
# import uuid


class INameFromFirstAndLastName(Interface):
    """Marker interface to enable name from filename behavior"""


@implementer(INameFromTitle)
@adapter(INameFromFirstAndLastName)
class NameFromFirstAndLastName(object):

    def __new__(cls, context):
        if not (context.firstName or context.lastName):
            generated_title = 'unknown'
        else:
            generated_title = context.firstName + ' ' + context.lastName
        instance = super(NameFromFirstAndLastName, cls).__new__(cls)
        instance.title = generated_title
        return instance

    def __init__(self, context):
        pass
