#!/usr/bin/python
"""
@author: Sangeetha Srinivasan
@copyright: Copyright(c) 2014 VMware, Inc. All rights reserved.
"""
import os
import random
import string
import logging
from framework.testutils.JsonUtil import JsonUtil
from framework.testutils.CustomDecorators import singleton


@singleton
class LoginData():
    """
    Email Test data
    """
    def __init__(self):
        autoRoot= os.getenv('AUTOMATIONROOT')
        self.logger = logging.getLogger('uitest')
        ''' Finalize on the test email data and contacts and add it to default json data '''
        self.LOGIN_DATA=os.path.join(autoRoot,"testdata/testapp/Login_Data.json")
        self.login_json = os.path.abspath(os.getenv('LOGIN_DATA')) if (os.getenv('LOGIN_DATA') is not None) else self.LOGIN_DATA
        self.loginData = JsonUtil(self.login_json).getJsonData()
        
        self.username = self.loginData["username"]
        self.password = self.loginData["password"]

    def getRandomString(self):
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(20)])