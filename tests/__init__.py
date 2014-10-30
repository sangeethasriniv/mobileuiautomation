'''
from testutils.sessionConfig import tConfig


def setup_package(self):
    tConfig.logger.info("######## Start Test Suite #########")
 
def teardown_package(self):
    tConfig.logger.info("######## End Test Suite #########")
    tConfig.closeTestApp()
    tConfig.driver.quit()
'''
