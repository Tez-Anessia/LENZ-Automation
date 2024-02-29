import logger
from login import adminLogin
import getdata as data
import workspace as ws
import pages as pg
from selenium import webdriver
from selenium.webdriver import ActionChains


#-----------------variables----------------
userName = "qa@email.com"
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
#-----------------Set-Up-----------------
driver = webdriver.Chrome()
driver.implicitly_wait(0.50)
driver.maximize_window()
actions = ActionChains(driver)
log = logger.setUp()

adminLogin(driver, userName, passW)

pg.getGlobalPages(driver)
pg.findPage(driver, "SMS Valet")