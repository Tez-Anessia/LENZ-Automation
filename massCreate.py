import commonUtils.logger as logger
from login import defaultLogin
import commonUtils.getdata as data
import workspace as ws
import wsUsers
from wsSettings import setWSFilter
from selenium import webdriver
from selenium.webdriver import ActionChains

#-----------------variables----------------
userName = "qa@email.com"
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
#-----------------Set-Up-----------------
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
actions = ActionChains(driver)
log = logger.setUp()

#-----------------Data Gathering -----------------
companyName = data.get_df(customerList)

#-----------------start of script-----------------
defaultLogin(driver)

#-----------------iterate through-----------------
for index, value in companyName.iterrows():
    nameValue = value['Company']
    salesRep = value['SalesRep']
    
    #----create workspace----
    ws.createWorkspace(driver, nameValue)
    
    #----validate workspace----
    url = ws.validateWorkspaceURL(driver, nameValue)
    
    #----update url in csv----
    data.add_url(customerList, nameValue, url)
    
    #----add users----
    wsUsers.navUser(driver, url)
    wsUsers.addUsers(driver, salesRep)
    
    #----add settings----
    setWSFilter(driver, nameValue)

# ------ Future State TBD  ------ 
    # after all workspaces were created the plan would be to then do another iteration through the customer list adding them to the pages. 
    # I Created globalReportsSplit.csv in the event it was easy to get the data who had what and possibly automate adding in the correct reporting
    # lastly I have made most of this modular with the thought we may be able to utilize this for other things 
