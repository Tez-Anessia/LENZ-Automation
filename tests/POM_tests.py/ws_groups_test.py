import sys
sys.path.append('.')

import src.pages.login as loginPage
import src.pages.common as common
import src.pages.workspace.groups_tab as wsgroups
import config.logger
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

log = config.logger.setUp()

#-----------------variables----------------
userName = 'qa@email.com'
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
customerName = "A Test Customer 1" #should be in table
Url = "https://admin.tez.io/workspaces/65d82c9058521dc38ff91d35"
groupName = "Group class test"
userName1 = "Anessia Mejia-Santillana"
userName2 = "Craig McCrary"
pageName = "Company Performance"
pageName2 = "SMS Valet"

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)

actions = ActionChains(driver)

groups = wsgroups.wsgroups(driver)
group_dialog = wsgroups.Dialog(driver)

login = loginPage.Login(driver)
nav = common.Common(driver)
log.info("------------Starting WS_groups test------------")

login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)
time.sleep(3)

groups.directNav(Url)

groups.click_add_group()

#DIALOG
group_dialog.set_group_name(groupName)

group_dialog.search_user(userName1)
group_dialog.find_in_list(userName1)
if group_dialog.isChecked(userName1) == True:
    log.info("User already selected")
else:
    group_dialog.select_user(userName1)
group_dialog.clear_search()
group_dialog.find_in_list(userName2)
group_dialog.select_user(userName2)

group_dialog.click_whitespace()
group_dialog.add_page_btn()

group_dialog.select_page(pageName)
group_dialog.add_more_pages(pageName2)
time.sleep(3)
group_dialog.click_save_btn()
time.sleep(3)

pages = groups.validateNewGroup(groupName)
print(pages)
