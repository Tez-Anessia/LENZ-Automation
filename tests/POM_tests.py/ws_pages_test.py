import pageobjects.pages.login as loginPage
import pageobjects.pages.common as common
from pageobjects.pages.workspace.pages_tab import Pages
import commonUtils.logger as logger
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

log = logger.setUp()

#-----------------variables----------------
userName = 'qa@email.com'
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
customerName = "Asta Parking" #should be in table
customerName2 = "AMS TEST2"
#-----------------Set-Up-----------------
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)

login = loginPage.Login(driver)
nav = common.Common(driver)
ws_pg = Pages(driver)
login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)


#driver.set_page_load_timeout(30)
url = "https://admin.tez.io/workspaces/65d82c9058521dc38ff91d35" #A test customer 1 URL 
log.info("------------Starting WS_Pages test------------")
ws_pg.directNav(url)
ws_pg.search("SMS Valet")
ws_pg.find_in_table("SMS Valet")
ws_pg.clear_search()
ws_pg.get_all_pages()
