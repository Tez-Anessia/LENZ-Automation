'''
Note this is only formatted to do one workspace filter for initial creation, when needed can be updated to add multiple
addColumnName needs refactoring to add multiple when above is requested. Issue with accepting a value and inputting it into the 
column
'''
import sys
sys.path.append('.')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.workspace.settings_tab import SettingsElements
from src.locators.workspace.ws_locators import WorkspaceProfile
import config.logger
import time

log = config.logger.setUp()

class SettingsTab:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
    
    def nav(self, url):
        url = url + "?tab=Settings"
        log.info(f"Navigating to {url}")
        self.driver.get(url)

    def click_settings_tab(self):
        tab = self.wait.until(EC.presence_of_element_located((WorkspaceProfile.settings_tab)))
        tab.click()
    
    def click_add_filter(self):
        filter_btn = self.wait.until(EC.presence_of_element_located((SettingsElements.add_filter_btn)))
        filter_btn.click()
        self.wait.until(EC.presence_of_element_located((SettingsElements.column_name_input)))
        log.info("new filter space created")
    
    # Default is corporation name
    def add_column_name(self):
        #column_value = columnName.text
        log.info("adding corporation to column name")
        columnName = self.wait.until(EC.presence_of_element_located((SettingsElements.column_name_input)))
        columnName.click()
        columnName.send_keys("corporation.name")

    # Current is set to equal but can be updated later if needed
    def set_operator(self):
        log.info("selecting equals to operator")
        self.driver.find_element(*SettingsElements.logic_dropdown).click()
        equals_option = self.wait.until(EC.presence_of_element_located((SettingsElements.equaltoOption)))
        equals_option.click()
    
    def set_filter_params(self, params):
        log.info(f"setting the parameter to {params}")
        param_input = self.driver.find_element(*SettingsElements.textValueInput)
        param_input.click()
        param_input.send_keys(params)
        #time.sleep(4) #uncomment when debugging since there is not save option here
    
    #-----------------Actions-----------------
    # Function brings it all together for one callable function
    def set_ws_filter(self, companyName):
        self.add_column_name()
        self.set_operator()
        self.set_filter_params(companyName)
        log.info(f"Filter for workspace {companyName} has been set")