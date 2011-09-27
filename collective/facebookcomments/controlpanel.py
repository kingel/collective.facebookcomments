from plone.app.registry.browser import controlpanel

from collective.facebookcomments.interfaces import IFacebookCommentsSettings, _


class FacebookCommentsSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IFacebookCommentsSettings
    label = _(u"Facebook Comments settings")
    description = _(u"""""")

    def updateFields(self):
        super(FacebookCommentsSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(FacebookCommentsSettingsEditForm, self).updateWidgets()

class FacebookCommentsSettingsControlPanel( \
        controlpanel.ControlPanelFormWrapper):
    form = FacebookCommentsSettingsEditForm
