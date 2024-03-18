import src.pages.login as loginPage
import src.pages.common as common
import src.pages.workspace.ws_users as ws_users
import config.logger
from selenium import webdriver
from selenium.webdriver import ActionChains


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

login = loginPage.login(driver)
nav = common.common(driver)
ws_users = ws_users.wsusers(driver)
login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)

#driver.set_page_load_timeout(30)
url = "https://admin.tez.io/workspaces/65d82c9058521dc38ff91d35" #A test customer 1 URL 
log.info("------------Starting ws_users test------------")
ws_users.directNav(url)
ws_users.searchUsers("Anessia Mejia-Santillana")
ws_users.findInTable("Anessia Mejia-Santillana")
ws_users.clearSearch()

ws_users.findInTable("Divisha Eppalapalli")
log.info("Assigning user process")
ws_users.clickAddUser()
ws_users.clickAddExisting()
ws_users.assignUser("Craig McCrary")