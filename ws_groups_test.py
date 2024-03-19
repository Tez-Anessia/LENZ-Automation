import src.pages.login as loginPage
import src.pages.common as common
import src.pages.workspace.ws_groups as wsgroups
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
groupName = "Group Test"
userName1 = "Anessia Mejia-Santillana"
userName2 = "Craig McCrary"
pageName = "Company Performance"
pageName2 = "SMS Valet"

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
actions = ActionChains(driver)

groups = wsgroups.wsgroups(driver)
login = loginPage.login(driver)
nav = common.common(driver)
log.info("------------Starting WS_groups test------------")

login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)
time.sleep(3)

groups.directNav(Url)

groups.clickAddGroup()
groups.dialog_addGroupName(groupName)

groups.dialog_searchUser(userName1)
groups.dialog_findUserinList(userName1)
if groups.dialog_isChecked(userName1) == True:
    log.info("User already selected")
else:
    groups.dialog_selectUser(userName1)
groups.dialog_clearsearch()
groups.dialog_findUserinList(userName2)
groups.dialog_selectUser(userName2)

groups.dialog_clickwhitespace()
groups.dialog_addPageBtn()

groups.dialog_selectPage(pageName)
groups.dialog_addPageBtn()
groups.dialog_addMorePages(pageName2)
time.sleep(3)
groups.dialog_save()
time.sleep(3)

pages = groups.validateNewGroup(groupName)
print(pages)
