import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import common_locators as locator
import config.logger

log = config.logger.setUp()

class common:

    def __init__(self, driver):
        self.driver = driver
    
    def click_account(self):
        self.driver.find_element(*locator.elements.account_Menu).click()
    
    def signout(self):
        self.driver.find_element(*locator.elements.account_Menu).click()
        signout = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator.elements.signout))
        signout.click()
        log.info("user signed out")
    
    def setPagination(self,viewable):
        log.info(f"Setting pagination to {viewable}")
        pagination = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator.elements.pgBox))
        pagination.click()

        match viewable:
            case '10': 
                option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator.elements.see10))
                option.click()
            case '20':                
                option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator.elements.see20))
                option.click()
            case '50':
                option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator.elements.see50))
                option.click()
            case '75':
                option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator.elements.see75))
                option.click()
            case '100':
                option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator.elements.see100))
                option.click()
            case 'All':
                option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator.elements.seeAll))
                option.click()
            case _:
                log.error("no element matched")
        
        log.info("pagination set for page")
        