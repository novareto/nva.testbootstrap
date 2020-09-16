# -*- coding: utf-8 -*-
from nva.testbootstrap.content.portlet import IPortlet  # NOQA E501
from nva.testbootstrap.testing import NVA_TESTBOOTSTRAP_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class PortletIntegrationTest(unittest.TestCase):

    layer = NVA_TESTBOOTSTRAP_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_portlet_schema(self):
        fti = queryUtility(IDexterityFTI, name='Portlet')
        schema = fti.lookupSchema()
        self.assertEqual(IPortlet, schema)

    def test_ct_portlet_fti(self):
        fti = queryUtility(IDexterityFTI, name='Portlet')
        self.assertTrue(fti)

    def test_ct_portlet_factory(self):
        fti = queryUtility(IDexterityFTI, name='Portlet')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPortlet.providedBy(obj),
            u'IPortlet not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_portlet_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Portlet',
            id='portlet',
        )

        self.assertTrue(
            IPortlet.providedBy(obj),
            u'IPortlet not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('portlet', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('portlet', parent.objectIds())

    def test_ct_portlet_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Portlet')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
