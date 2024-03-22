import sys
sys.path.append('.')
import src.pages.login as loginPage
import src.pages.workspaces as wsPage
import src.pages.workspace.pages_tab as wsPages
import src.pages.workspace.Users as wsUser
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
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)
actions = ActionChains(driver)

login = loginPage.Login(driver)
ws_Main = wsPage.workspaces(driver)
ws_Pages = wsPages.wspages(driver)
ws_user = wsUser.Users(driver)
nav = common.Common(driver)
login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)

#driver.set_page_load_timeout(30)
'''
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
'''

