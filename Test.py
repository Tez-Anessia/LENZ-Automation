from typing import Self
import src.pages.login_page as loginPage
import src.pages.workspaces_page as wsPage
import src.pages.workspace.pages_tab as wsPages
import src.pages.workspace.user_tab as wsUser
import src.pages.common as common
import config.logger
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

log = config.logger.setUp()

#-----------------variables----------------
userName = 'qa@email.com'
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
customerName = "Asta Parking"
customerName2 = "AMS TEST2"
#-----------------Set-Up-----------------
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
actions = ActionChains(driver)

login = loginPage.login(driver)
ws_Main = wsPage.workspaces(driver)
ws_Pages = wsPages.wspages(driver)
ws_user = wsUser.wsusers(driver)
nav = common.common(driver)
login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)

#driver.set_page_load_timeout(30)

driver.get("https://admin.tez.io/workspaces/65f06f2558521dc38ffe0067")
url = "https://admin.tez.io/workspaces/65d82c9058521dc38ff91d35"
ws_user.directNav(url)

user = "Anessia Mejia-Santillana"
newUser = "Divisha Eppalapalli"
log.info("trying click add user")
ws_user.clickAddUser()
log.info("trying click addexisting")
ws_user.clickAddExisting()
log.info("trying assignuser")
ws_user.assignUser(newUser)
