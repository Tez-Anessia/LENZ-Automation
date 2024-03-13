from selenium.webdriver.common.by import By

class login: 
    username_input = (By.XPATH, "//input[@name='contact-email']")
    password_input = (By.XPATH, "//input[@name='password']")
    login_btn = (By.XPATH, "//div[contains(text(),'Login')]")