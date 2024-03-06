from selenium.webdriver.common.by import By


class LoginPage: 

    def __init__(self, driver):
        self.driver = driver
        #----elements locators------
        self.userName_textbox = (By.NAME, "contact-email")
        self.passW_textbox = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, ".group")

#---Functions for the actions we want to do ---
    def open_page(self, url):
        self.driver.get(url)
    
    def enter_user(self, userName):
        self.driver.find_element(self.userName_textbox).send_keys(userName)
    
    def enter_pass(self, passWord):
        self.driver.find_element(self.passW_textbox).send_keys(passWord)
    
    def click_login(self):
        self.driver.find_element(self.login_button).click()


    