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
        first_name = str(context.firstName).replace(' ', '-').lower()
        last_name = str(context.lastName).replace(' ', '-').lower()
        generated_title = ''.join([c for c in f"{last_name}-{first_name}" if c in string.ascii_lowercase + string.digits + '-'])
        instance = super(NameFromFirstAndLastName, cls).__new__(cls)
        instance.title = generated_title
        return instance

    def __init__(self, context):
        pass
