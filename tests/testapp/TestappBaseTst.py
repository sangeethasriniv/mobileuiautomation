#!/usr/bin/python
"""
@author: Sangeetha Srinivasan
@copyright: Copyright(c) 2014 VMware, Inc. All rights reserved.
"""
from framework.testutils.BaseTest import BaseTest
from pages.testapp.LoginPage import LoginPage
from tests.General.AppStates import AppStates

class TestappBaseTst(BaseTest):
    """
    Base Test class - All test classes inherit this class for general test setup
    """
    @classmethod
    def setUpClass(cls):
        super(TestappBaseTst,cls).setUpClass()
        cls.tConfig.setApp("testapp")
        cls._loginPage = LoginPage()
        cls._appStates = AppStates()
        

    @classmethod
    def tearDownClass(cls):
        super(TestappBaseTst,cls).tearDownClass()
        cls.tConfig.cleanApp(True)
        cls.tConfig.quitDriver()
