
from selenium import webdriver
from selenium.webdriver import ActionChains

import commonUtils.logger as logger
from  pageobjects.pages.login import Login
from pageobjects.pages.workspaces import Workspaces


log = logger.setUp()

#-----------------variables----------------
userName = 'qa@email.com'
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
customerName = "Asta Parking"
customerName2 = "AMS TEST2"
#-----------------Set-Up-----------------
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)
actions = ActionChains(driver)
login = Login(driver)


login.adminLogin(userName, passW)
#Workspaces.

