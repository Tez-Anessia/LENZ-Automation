''''
The purpose of this script is to update the customer list csv will 
the urls of any workspaces that have already been created in LENZ. 
This should help with not creating duplicates and helping the mass create script
ensure its not overwriting any customer's data
'''
from commonUtils import logger
from pageobjects.pages import login
from pageobjects.pages import workspaces
from pageobjects.pages import common
import commonUtils.getdata as data

from selenium import webdriver
from selenium.webdriver import ActionChains
import pandas as pd
import time
#-----------------variables----------------
userName = "qa@email.com"
passW = "T3Z@dm!nP@$$24^"
customerList = "workspaces.csv"

#-----------------Set-Up-----------------
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)
actions = ActionChains(driver)

log = logger.setUp()
log_in = login.Login(driver)
ws = workspaces.Workspaces(driver)
nav = common.Common(driver)
#-----------------Data Gathering -----------------
path = data.get_path("data", customerList)

#-----------------start of script-----------------
log_in.adminLogin(userName, passW)

nav.set_pagination("All")
time.sleep(2)

names = ws.get_current_workspaces()
url=[]
for name in names:
    wsurl = ws.returnURL(name)
    url.append(wsurl)

df = pd.DataFrame({'Customer': names, 'SalesRep': " ", 'URL': url})
df.to_csv(path, mode='a', index=False, header=False)

# driver.quit()

