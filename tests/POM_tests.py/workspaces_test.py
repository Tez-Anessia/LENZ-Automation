from typing import Self
import pageobjects.pages.login as loginPage
import pageobjects.pages.workspaces as workspace
import pageobjects.pages.common as common
import commonUtils.logger as logger
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

log = logger.setUp()

#-----------------variables----------------
userName = 'qa@email.com'
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
customerName = "Asta Parking" #should be in table
customerName2 = "AMS TEST2"
#-----------------Set-Up-----------------
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
actions = ActionChains(driver)

login = loginPage.Login(driver)
nav = common.Common(driver)
ws = workspace.workspaces(driver)
login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)

#driver.set_page_load_timeout(30)
url = "https://admin.tez.io/workspaces/65d82c9058521dc38ff91d35" #A test customer 1 URL 

log.info("------------Starting workspaces test------------")
#ws.directNav()
ws.search(customerName)
ws.find_in_table(customerName)
ws.clear_search()
ws.find_in_table(customerName)
ws.getURL(customerName)
print(ws.returnURL(customerName))

ws.createWorkspace(customerName2)
ws.validateWorkspace(customerName2)

