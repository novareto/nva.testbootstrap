# -*- coding: utf-8 -*-
from selenium import webdriver
from axe_selenium_python import Axe
from nva.testbootstrap import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ResultsView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('results_view.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = self.test_site(self.request.get('exturl'))
        self.backurl = self.context.absolute_url() + '/w3-c-view'
        return self.index()

    def test_site(self, site):
        driver = webdriver.Firefox()
        driver.get(site)
        axe = Axe(driver)
        # Inject axe-core javascript into page.
        axe.inject()
        # Run axe accessibility checks.
        results = axe.run()
        # Write results to file
        #axe.write_results(results, 'a11y.json')
        driver.close()
        return results.get('violations')
        # Assert no violations are found
        #assert len(results["violations"]) == 0, axe.report(results["violations"])
