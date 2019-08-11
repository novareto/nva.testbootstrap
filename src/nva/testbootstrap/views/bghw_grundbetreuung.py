# -*- coding: utf-8 -*-

from nva.testbootstrap import _
from Products.Five.browser import BrowserView
from plone import api as ploneapi

class BghwGrundbetreuung(BrowserView):
    """Test the Bootstrap Content Section"""

    def static(self):
        portal = ploneapi.portal.get().absolute_url()
        return portal + '/++resource++nva.testbootstrap'
