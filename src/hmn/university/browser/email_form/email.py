from hmn.university import _
from zope.interface import Interface
from zope import schema
from z3c.form import form, button, field
from plone.z3cform import layout
import logging
from plone import api
from hmn.university.database import get_connection

logger = logging.getLogger('email_form')


class IEmailFormSchema(Interface):
    from_address = schema.TextLine(title=_(u'From'))
    to_address = schema.TextLine(title=_(u'To'))
    subject = schema.TextLine(title=_(u'Subject'))
    body = schema.Text(title=_(u'Body'))


class EmailForm(form.Form):
    schema = IEmailFormSchema
    ignoreContext = True
    fields = field.Fields(IEmailFormSchema)

    @button.buttonAndHandler(_(u'Send'))
    def handleApply(self, action):
        data, errors = self.extractData()

        # send data in email

        logger.info(data)
        logger.info(errors)

        # create connection with mysql
        connection = get_connection()
        with connection:
            with connection.cursor() as cursor:
                # Create a new record
                sql = """INSERT INTO `email_msgs` (
                             `from_address`,
                             `to_address`,
                             `subject`,
                             `body`,
                         ) VALUES (%s, %s, %s, %s)"""
                cursor.execute(
                    sql,
                    (data.get('from_address'),
                     data.get('to_address'),
                     data.get('subject'),
                     data.get('body'))
                )

            # connection is not autocommit by default. So you must commit
            # to save your changes.
            connection.commit()

            with connection.cursor() as cursor:
                # Read a single record
                sql = """SELECT `id`, `to_address`, `subject`, `body`
                         FROM `email_msgs`
                         WHERE `email`=%s"""
                cursor.execute(sql, (data.get('from_address'),))
                result = cursor.fetchone()
                logger.info(result)
                # do something

            api.portal.show_message(message='Success!', request=self.request)


EmailFormView = layout.wrap_form(EmailForm)
