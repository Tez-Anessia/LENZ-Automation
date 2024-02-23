from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import logger
import login
import getdata as data
import workspace as wksp
import users
from wkspsettings import setWSFilter 

#------variables for modifiability-----------------
userName = "anessia@teztechnology.com"
passW = "Nitrogen14!"
customerList = "Testsheet.csv"
#----Driver & Actions setup-------------------------
driver = webdriver.Chrome()
driver.implicitly_wait(0.50)
driver.set_window_size(2576, 1407)
actions = ActionChains(driver)

#-------------start of script run -------------
login.adminLogin(driver, userName, passW)

#-----get the data from csv-----
companyName = data.getdf(customerList)

#-----iterate through-----
for index, value in companyName.iterrows():
    nameValue = value['Company']
    salesRep = value['SalesRep']
    #----create workspace----
    wksp.createWorkspace(driver, nameValue)
    #----validate workspace----
    url = wksp.validateWorkspaceURL(driver, nameValue)
    #----update url in csv----
    data.addURL(customerList, nameValue, url)
    #----add users----
    users.navUser(driver, url)
    users.addUsers(driver, salesRep)
    #----add settings----
    setWSFilter(driver, nameValue)

