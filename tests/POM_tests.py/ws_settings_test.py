import pageobjects.pages.login as loginPage
import pageobjects.pages.common as common
import pageobjects.pages.workspace.settings_tab as settings_tab
import commonUtils.logger as logger
from selenium import webdriver
from selenium.webdriver import ActionChains


log = logger.setUp()

#-----------------variables----------------
userName = 'qa@email.com'
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
customerName = "Asta Parking" #should be in table
customerName2 = "A Test Customer 1"

#-----------------Set-Up-----------------
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
actions = ActionChains(driver)

login = loginPage.Login(driver)
nav = common.Common(driver)
settings_tab = settings_tab.wssettings(driver)
login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)

#driver.set_page_load_timeout(30)
url = "https://admin.tez.io/workspaces/65d82c9058521dc38ff91d35" #A test customer 1 URL 
log.info("------------Starting ws_settings test------------")

settings_tab.directNav(url)
settings_tab.click_add_filter()
settings_tab.add_column_name()
settings_tab.set_operator()
settings_tab.set_filter_params(customerName2)