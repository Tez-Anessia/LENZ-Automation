import sys
sys.path.append('.')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.locators.common import CommonElements as locator
import commonUtils.logger as logger

log = logger.setUp()

class Common:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def click_account(self):
        self.driver.find_element(*locator.account_Menu).click()
    
    def signout(self):
        self.driver.find_element(*locator.account_Menu).click()
        signout = self.wait.until(EC.element_to_be_clickable(locator.signout))
        signout.click()
        log.info("user signed out")
    
    def set_pagination(self, viewable):
        log.info(f"Setting pagination to {viewable}")
        pagination = self.wait.until(EC.visibility_of_element_located(locator.pgBox))
        pagination.click()

        match viewable:
            case '10': 
                option = self.wait.until(EC.element_to_be_clickable(locator.see10))
                option.click()
            case '20':                
                option = self.wait.until(EC.element_to_be_clickable(locator.see20))
                option.click()
            case '50':
                option = self.wait.until(EC.element_to_be_clickable(locator.see50))
                option.click()
            case '75':
                option = self.wait.until(EC.element_to_be_clickable(locator.see75))
                option.click()
            case '100':
                option = self.wait.until(EC.element_to_be_clickable(locator.see100))
                option.click()
            case 'All':
                option = self.wait.until(EC.element_to_be_clickable(locator.seeAll))
                option.click()
            case _:
                log.error("no element matched")
        
        log.info("pagination set for page")
        
