#!/usr/bin/python
"""
@author: Sangeetha Srinivasan
@copyright: Copyright(c) 2014 VMware, Inc. All rights reserved.
"""

from tests.testapp.TestappBaseTst import TestappBaseTst
from testdata.testapp.LoginData import LoginData
from pages.testapp.LoginPage import LoginPage
from framework.testutils.wait import wait

class TestSomeModule(TestappBaseTst):
    @classmethod
    def setUpClass(cls):
        super(TestSomeModule,cls).setUpClass()
        cls._loginData = LoginData()
        cls.username = cls._loginData.username
        cls.password = cls._loginData.password
        cls._loginPage = LoginPage()
 
    def setUp(self):
        super(TestSomeModule,self).setUp()

    def test1_enterusername(self):
        if (self._appStates.appNotAuthenticated()):
            self._loginPage.enterCredentials(self.username, self.password)
        self.assertTrue(self._loginPage.getUserName())

    def tearDown(self):
        super(TestSomeModule,self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(TestSomeModule,cls).tearDownClass()