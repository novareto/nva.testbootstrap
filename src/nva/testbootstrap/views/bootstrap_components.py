# -*- coding: utf-8 -*-

from nva.testbootstrap import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class BootstrapComponents(BrowserView):
    """Test the Bootstrap Components"""

    def static(self):
        portal = ploneapi.portal.get().absolute_url()
        return portal + '/++resource++nva.testbootstrap'
