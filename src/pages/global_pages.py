import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.locators import global_pages_locators as locator
import config.logger

log = config.logger.setUp()

class globalpages:

        def __init__(self, driver):
            self.driver = driver
    
 #--------Singular Functions--------
        def directNav(self):
            self.driver.get("https://admin.tez.io/pages?tab=Global+pages")
        