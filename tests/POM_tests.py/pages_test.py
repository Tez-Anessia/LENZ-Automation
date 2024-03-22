import sys
sys.path.append('.')

import src.pages.login as loginPage
import src.pages.common as common
import src.pages.pages as pages
import config.logger
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import time


log = config.logger.setUp()

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
pg = pages.Pages(driver)
pgdialog = pages.Dialog(driver)
login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)

pg.directNav_global()
#pages.search("LENZ Admin")
pgdialog.get_assigned("TEZ Home")
# pages.dialog_search(customerName)
# pages.dialog_click_search()
# pages.dialog_wait()
# pages.dialog_isChecked(customerName)
# pages.dialog_click_whitespace()
# pages.dialog_findCurrentlyAssigned(customerName)
# pages.dialog_submit()
time.sleep(5)