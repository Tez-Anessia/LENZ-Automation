''''
The purpose of this script is to update the customer list csv will 
the urls of any workspaces that have already been created in LENZ. 
This should help with not creating duplicates and helping the mass create script
ensure its not overwriting any customer's data
'''
import logger
from login import adminLogin
import getdata as data
import workspace as ws
from selenium import webdriver
from selenium.webdriver import ActionChains
import pandas as pd

#-----------------variables----------------
userName = "qa@email.com"
passW = "T3Z@dm!nP@$$24^"
customerList = "customerList.csv"

#-----------------Set-Up-----------------
driver = webdriver.Chrome()
driver.implicitly_wait(0.50)
driver.maximize_window()
actions = ActionChains(driver)
log = logger.setUp()

#-----------------Data Gathering -----------------
companydf = data.getdf(customerList)

#-----------------start of script-----------------
adminLogin(driver, userName, passW)

#----Iterate through the CSV------
for index, value in companydf.iterrows():
    nameValue = value['Company']

    if pd.isna(value['URL']):
        result = ws.validateWorkspaceURL(driver, nameValue)
        if result == "not in workspace":
            log.info(f"No URL found for {nameValue}")
        else:
            log.info(f"Found workspace for: {nameValue} under {result}")
            companydf.loc[companydf['Company'] == nameValue, 'URL'] = str(result)
            data.addURL(customerList, nameValue, result)
    else:
        print(f"Skipping validation for {nameValue} as URL is not empty")

log.info("Script complete, worksheet has been updated with any new URLs")
driver.quit()

