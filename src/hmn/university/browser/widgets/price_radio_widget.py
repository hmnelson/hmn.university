__docformat__ = "reStructuredText"
import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form.widget import Widget, FieldWidget
from z3c.form.browser import widget


import logging

logger = logging.getLogger(
    "hmn.university.widgets.price_radio_widget.py")


class IPriceRadioWidget(interfaces.ITextWidget):
    pass

@zope.interface.implementer_only(IPriceRadioWidget)
class PriceRadioWidget(widget.HTMLTextInputWidget, Widget):
    """Input type text widget implementation."""

    klass = u'price-rating-widget'
    css = u'text'
    value = None
    currency_symbol = '$'

    def update(self):
        super(PriceRadioWidget, self).update()
        # widget.addFieldClass(self)
        if getattr(self.field,'currency_symbol',None):
            self.currency_symbol = getattr(self.field,'currency_symbol')


@zope.component.adapter(zope.schema.interfaces.IField, interfaces.IFormLayer)
@zope.interface.implementer(interfaces.IFieldWidget)
def PriceRadioFieldWidget(field, request):
    """IFieldWidget factory for TextWidget."""
    return FieldWidget(field, PriceRadioWidget(request))