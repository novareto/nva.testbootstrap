# -*- coding: utf-8 -*-

from nva.testbootstrap import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class W3CView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('w3_c_view.pt')

    def get_url(self):
        return self.context.absolute_url() + '/results-view'
