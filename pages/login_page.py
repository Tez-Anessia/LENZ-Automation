from selenium.webdriver.common.by import By
import time

class LoginPage: 

    def __init__(self, driver):
        self.driver = driver
        #----elements locators------
        self.userName_textbox = (By.NAME, "contact-email")
        self.passW_textbox = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, ".group")

#---Singular Functions for the actions we want to do ---
    def open_page(self, url):
        self.driver.get(url)
    
    def enter_user(self, userName):
        self.driver.find_element(*self.userName_textbox).send_keys(userName)
    
    def enter_pass(self, passWord):
        self.driver.find_element(*self.passW_textbox).send_keys(passWord)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def validateLogin(self):
        currentURL = self.driver.current_url
        if currentURL == "https://admin.tez.io/workspaces":
            print("login successful")
        else:
            print("unable to login")

#---Functions for Actions---
    def adminLogin(self, userName, passWord):
        self.driver.find_element(*self.userName_textbox).send_keys(userName)
        self.driver.find_element(*self.passW_textbox).send_keys(passWord)
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)
        self.validateLogin()
    