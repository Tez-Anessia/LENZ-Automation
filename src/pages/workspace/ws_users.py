import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys;
from src.locators import ws_locators as locator
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common.exceptions import StaleElementReferenceException
import time

import config.logger

log = config.logger.setUp()

class wsusers:
        
    def __init__(self, driver):
        self.driver = driver

    def pageLoadWait(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='py-3 px-1 rounded-full hover:bg-gray-100 transition-colors duration-100 flex items-center justify-center']")))
        except:
            log.error("no elements in table")

    def directNav(self, url):
        url = url + "?tab=Users"
        log.info(f"Navigating to {url}")
        self.driver.get(url)
        self.pageLoadWait()  

    def usersTabClick(self):
        self.driver.find_element(*locator.wsprofileElements.users_tab).click()
        self.pageLoadWait()

    def searchUsers(self, user):
        log.info(f"Searching for page: {user}")
        search = self.driver.find_element(*locator.wsuserElements.search_input) 
        search.click()
        search.send_keys(user)

    def clearSearch(self):
        search = self.driver.find_element(*locator.wsuserElements.search_input) 
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
    
    def findInTable(self, user):
        self.pageLoadWait()
        log.info(f"starting process to find {user} in table")
        if self.driver.find_element(By.XPATH, f"{locator.wsuserElements.userName_XPATH}//a[normalize-space()='{user}']"):
            log.info(f"{user} found in table")
        else:
            log.error(f"{user} not found in table")

    def clickAddUser(self):
        self.driver.find_element(*locator.wsuserElements.add_user_btn).click()
    
    #needs to have the dialog box present before using
    def clickAddExisting(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex justify-between py-4 px-4']")))

        self.driver.find_element(*locator.wsuserDialog.add_existing_btn).click()
    
    def assignUser(self, user):
        #self.driver.find_element(*locator.wsuserDialog.exsitingUserWhiteSpace).click()
        try:
            search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            search.click()
            search.send_keys(user)
        except StaleElementReferenceException:
            # Element is stale, find it again
            search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            search.click()
            search.send_keys(user)
            # Retry actions on the element

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator.wsuserDialog.dropdown_viewable))
        
        #confirm if theyre found in dropdown
        if self.driver.find_element(By.XPATH, f"//div[contains(text(),'{user}')]"):
            log.info(f"User {user} found, selecting user")
            dropdownOption = self.driver.find_element(By.XPATH, f"//div[contains(text(),'{user}')]")
            AC(self.driver).move_to_element(dropdownOption).click().perform()
            time.sleep(2)
        else: 
            log.info("user not found")
###UPDATE AFTER TESTING
        #clear input
        search = self.driver.find_element(*locator.wsuserDialog.assign_search_input) 
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("Click whitespace")
        self.driver.find_element(*locator.wsuserDialog.exsiting_user_whitespace).click()
        log.info("clicking submit ")
        self.driver.find_element(*locator.wsuserDialog.submit_btn).click()
   



