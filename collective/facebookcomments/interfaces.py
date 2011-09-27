from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.facebookcomments')


class IFacebookCommentsSettings(Interface):
    """Global facebookcomments settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    facebook_appid = schema.TextLine(title=_(u"Facebook AppID"),
                                  description=_(u"help_facebook_appid",
                                                default=u"Enter in your Facebook AppID here"),
                                  required=False,
                                  default=u'',)

