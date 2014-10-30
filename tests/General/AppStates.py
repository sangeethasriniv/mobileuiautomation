#!/usr/bin/python
"""
@author: Diana Menezes
@copyright: Copyright(c) 2014 VMware, Inc. All rights reserved.
"""
from framework.testutils.Page import Page

class AppStates(Page):
    
      
    def __init__(self):
        Page.__init__(self)
             
    def appNotAuthenticated(self):
        return True