import src.pages.login as loginPage
import src.pages.common as common
import src.pages.workspace.users_tab as Users
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

login = loginPage.Login(driver)
nav = common.Common(driver)
Users = Users.Users(driver)
login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)

#driver.set_page_load_timeout(30)
url = "https://admin.tez.io/workspaces/65d82c9058521dc38ff91d35" #A test customer 1 URL 
log.info("------------Starting ws_users test------------")
Users.directNav(url)
Users.search("Anessia Mejia-Santillana")
Users.find_in_table("Anessia Mejia-Santillana")
Users.clear_search()

Users.find_in_table("Divisha Eppalapalli")
log.info("Assigning user process")
Users.click_add_user()
Users.click_add_existing()
Users.assign_user("Craig McCrary")