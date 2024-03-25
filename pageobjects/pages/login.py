'''
Lenz admin log in page - currently only configured for the Lenz admin page 
but will be expanded when needed for the frontend Lenz workspaces when needed. 
'''

import sys
sys.path.append('.')

import time
from pageobjects.locators.login import LoginElements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import commonUtils.logger as logger

log = logger.setUp()

class Login: 

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def open_page(self, url):
        self.driver.get(url)
    
    def enter_user(self, userName):
        un_input = self.wait.until(EC.visibility_of_element_located(LoginElements.username_input))
        un_input.send_keys(userName)

    
    def enter_pass(self, passWord):
        pw_input = self.wait.until(EC.presence_of_element_located(LoginElements.password_input))
        pw_input.send_keys(passWord)
    
    def click_login(self):
        login_btn = self.wait.until(EC.presence_of_element_located(LoginElements.login_btn))
        login_btn.click()

    def admin_validate(self):
        currentURL = self.driver.current_url
        if currentURL == "https://admin.tez.io/workspaces":
            log.info("login successful")
        else:
            log.info("unable to login")

    def adminLogin(self, userName, passWord):
        log.info("Starting login process")
        self.driver.find_element(*LoginElements.username_input).send_keys(userName)
        log.info(f"username set as {userName}")
        self.driver.find_element(*LoginElements.password_input).send_keys(passWord)
        log.info(f"pass set as {passWord}")
        self.driver.find_element(*LoginElements.login_btn).click()
        time.sleep(2)
        log.info("Validating login success")
        self.admin_validate()
    