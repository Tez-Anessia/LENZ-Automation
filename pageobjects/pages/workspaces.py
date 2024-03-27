import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pageobjects.locators.workspaces import WorkspacesElements as workspace
import commonUtils.logger as logger

log = logger.setUp()

class Workspaces:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
 
    def nav(self):
        self.driver.get("https://admin.tez.io/workspaces")

    # Function which sends the value of companyName to the search bar input
    # If Else statement will check if the field is empty. If its not, then it will clear the input field then send the search params 
    def search(self, companyName):
        log.info(f"Searching for {companyName}")
        #pagination will only appear once the page is fully loaded 
        self.wait.until(EC.presence_of_element_located(workspace.pagination_element))
        search = self.driver.find_element(*workspace.search_input)
        #If there is then it will clear the text and then send the search params
        if search.get_attribute("value") == "":
            search.send_keys(companyName)
        else:
            self.clear_search()
            search.send_keys(companyName)

    def clear_search(self):     
        # Pagination will only appear once the page is fully loaded 
        self.wait.until(EC.presence_of_element_located(workspace.pagination_element))
        # Keys sent her since the .clear() wont work in search inputs 
        search = self.wait.until(EC.element_to_be_clickable((workspace.search_input)))
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("cleared search")

    # Locate only on the viewable page
    # Before using set pagination to all to locate or do a partial search then find in table to view from the results
    def find_in_table(self, companyName):
        # Wait until table loads
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        log.info(f"starting process to find {companyName} in table")
        if self.wait.until(EC.presence_of_element_located(By.XPATH, f"//table//div[contains(text(),'{companyName}')]")):
            log.info(f"{companyName} found in table")
        else:
            log.error(f"{companyName} not found in table")

    # Function to search the viewable table
    # Like findInTable() except it will read and log the url of the element if found in table    
    def getURL(self, companyName):
        if self.driver.find_element(By.XPATH, f"//table//div[contains(text(),'{companyName}')]"):
            ws_name = self.driver.find_element(By.XPATH, f"//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]/div/a[contains(@href,'/workspaces')]")
            url = ws_name.get_attribute('href')
            log.info(f"found url for: {companyName}, {url}")
        else:
            log.error(f"{companyName} not found in table")

    # Same function as getURL except it will either return the URL of the workspace or it will return "Not Found" 
    def returnURL(self, companyName):
        if self.driver.find_element(By.XPATH, f"//table//div[contains(text(),'{companyName}')]"):
            workspace_element = self.driver.find_element(By.XPATH, f"//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]/div/a[contains(@href,'/workspaces')]")
            url = workspace_element.get_attribute('href')
            log.info(f"found url for: {companyName}, {url}")
            return url
        else:
            log.error(f"{companyName} not found in table")
            url = "Not Found"
    
    def get_current_workspaces(self):
        self.wait.until(EC.presence_of_all_elements_located(workspace.nameColumn_elements))
        elements = self.driver.find_elements(*workspace.nameColumn_elements)
        count = len(elements)
        log.info(f"There are {count} workspaces in Lenz")
        log.info(f"Getting list of workspaces")
        names=[]
        for element in elements:
            wsName = element.text
            names.append(wsName)
        
        return names

    #-----------------Create Workspace Specific-----------------
    def click_create_btn(self):
        btn = self.wait.until(EC.visibility_of_element_located(workspace.add_ws_btn))
        btn.click()
    
    def set_workspace_name(self, companyName):
        input = self.driver.find_element(*workspace.dialog_wsName_input)
        input.click()
        input.send_keys(companyName)
    
    def click_save_btn(self):
        self.driver.find_element(*workspace.dialog_save_Btn).click()
    
    #-----------------Actions-----------------
    # This function is used to create the workspace combining the methods above
    def create_workspace(self, companyName):
        log.info(f"Creating workspace for {companyName}")
        self.click_create_btn()
        self.wait.until(EC.visibility_of_element_located(workspace.dialog_whiteSpace))
        self.set_workspace_name(companyName)
        self.click_save_btn()
        log.info(f"Created workspace for {companyName}")

    # This function is used to validate a workspace exists and returns the URL of the workspace
    def validate_workspace(self, companyName):
        log.info(f"Validating workspace for {companyName} exists")
        self.search(companyName)
        self.find_in_table(companyName)
        url = self.returnURL(companyName)
        return url
    

    