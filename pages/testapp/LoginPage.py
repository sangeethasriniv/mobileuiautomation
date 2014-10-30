#!/usr/bin/python
"""
@author: Sangeetha Srinivasan 
@copyright: Copyright(c) 2014 VMware, Inc. All rights reserved.
"""

from framework.testutils.Page import Page
from framework.testutils.wait import wait


class LoginPage(Page):
    """
    Access / Manipulate UI attributes of login page
    """    
    def __init__(self):
        Page.__init__(self)
        self.logger.info("ios Workspace")

    def enterCredentials(self, user, pwd):
        self.getUserName().send_keys(user)
        wait(5)
    
    ''' Getters '''
    def getUserName(self):
        if(self.iosTest):
            return self.getElementById("username")
        if(self.androidTest):
            return self.getElementByName("UserName")