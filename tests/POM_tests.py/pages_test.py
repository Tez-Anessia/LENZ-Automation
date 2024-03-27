import sys
sys.path.append('.')

import pageobjects.pages.login as loginPage
import pageobjects.pages.common as common
from pageobjects.pages import pages
import commonUtils.logger as logger
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import time


log = logger.setUp()

#-----------------variables----------------
userName = 'qa@email.com'
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
customerName = "Asta Parking" #should be in table
customerName2 = "AMS TEST2"
pageName = "Total Revenue & TEZ Fee"

workspace1 = "A Test Customer 1"
workspace2 = "Benjamin Test"

workspaces = [workspace1, workspace2]
#-----------------Set-Up-----------------
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)
actions = ActionChains(driver)

login = loginPage.Login(driver)
nav = common.Common(driver)
pg = pages.Pages(driver)
pgdialog = pages.Dialog(driver)

log.info("-------- Starting Pages Test ----------")
login.adminLogin(userName, passW)

pg.nav_global()
nav.set_pagination("All")
pg.find_in_table(pageName)
#pg.select_menu_option(pageName, "Edit")
pgdialog.get_assigned(pageName)

pgdialog.add_multiple_workspaces(workspaces)

for workspace in workspaces:
    pgdialog.isAssigned(workspace)
# pgdialog.add_workspace(workspace1)
# pgdialog.isAssigned(workspace1)
#pages.search("LENZ Admin")
# pgdialog.get_assigned("TEZ Home")
# pages.dialog_search(customerName)
# pages.dialog_click_search()
# pages.dialog_wait()
# pages.dialog_isChecked(customerName)
# pages.dialog_click_whitespace()
# pages.dialog_findCurrentlyAssigned(customerName)
# pages.dialog_submit()
time.sleep(5)