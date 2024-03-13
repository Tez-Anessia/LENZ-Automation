import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
import time
from src.locators import login_locators as locator
import config.logger

log = config.logger.setUp()

class login: 

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
    
    def enter_user(self, userName):
        self.driver.find_element(*locator.login.username_input).send_keys(userName)
    
    def enter_pass(self, passWord):
        self.driver.find_element(*locator.login.password_input).send_keys(passWord)
    
    def click_login(self):
        self.driver.find_element(*locator.login.login_btn).click()

    def validateLogin(self):
        currentURL = self.driver.current_url
        if currentURL == "https://admin.tez.io/workspaces":
            log.info("login successful")
        else:
            log.info("unable to login")

#---Functions for Actions---
    def adminLogin(self, userName, passWord):
        log.info("Starting login process")
        self.driver.find_element(*locator.login.username_input).send_keys(userName)
        self.driver.find_element(*locator.login.password_input).send_keys(passWord)
        self.driver.find_element(*locator.login.login_btn).click()
        time.sleep(2)
        log.info("Validating login success")
        self.validateLogin()
    