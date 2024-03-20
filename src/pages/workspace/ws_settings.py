'''
Note this is only formatted to do one workspace filter for initial creation, when needed can be updated to add multiple
addColumnName needs refactoring to add multiple when above is requested. Issue with accepting a value and inputting it into the 
column
'''
import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import ws_locators as locator
import config.logger
import time

log = config.logger.setUp()

class wssettings:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
    
    def directNav(self, url):
        url = url + "?tab=Settings"
        log.info(f"Navigating to {url}")
        self.driver.get(url)

    def settingsTabClick(self):
        tab = self.wait.until(EC.presence_of_element_located((locator.wsprofileElements.settings_tab)))
        tab.click()
    
    def clickAddFilter(self):
        filter_btn = self.wait.until(EC.presence_of_element_located((locator.wsSettingsElements.add_filter_btn)))
        filter_btn.click()
        self.wait.until(EC.presence_of_element_located((locator.wsSettingsElements.column_name_input)))
        log.info("new filter space created")
    
    # default is corporation name
    def addColumnName(self):
        #column_value = columnName.text
        log.info("adding corporation to column name")
        columnName = self.wait.until(EC.presence_of_element_located((locator.wsSettingsElements.column_name_input)))
        columnName.click()
        columnName.send_keys("corporation.name")

    #current is set to equal but can be updated later if needed
    def setOperator(self):
        log.info("selecting equals to operator")
        self.driver.find_element(*locator.wsSettingsElements.logic_dropdown).click()
        equals_option = self.wait.until(EC.presence_of_element_located((locator.wsSettingsElements.equaltoOption)))
        equals_option.click()
    
    def setFilterParams(self, params):
        log.info(f"setting the parameter to {params}")
        param_input = self.driver.find_element(*locator.wsSettingsElements.textValueInput)
        param_input.click()
        param_input.send_keys(params)
        #time.sleep(4) #uncomment when debugging since there is not save option here
    
    #function brings it all together for one callable function
    def setWorkspaceFilter(self, companyName):
        self.addColumnName()
        self.setOperator()
        self.setFilterParams(companyName)
        log.info(f"Filter for workspace {companyName} has been set")