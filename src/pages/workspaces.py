import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.locators import workspaces_locators as locator
import config.logger

log = config.logger.setUp()

class workspaces:

    #--Helpful XPATHS in the table
    table_row_XPATH = "//tbody/tr/td" #tr = row, td = column, index position. td[4] - users column
    #--Add these to the end of the workspace URL XPATH: "//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]"
    workspace_pages_XPATH = "/following-sibling::td[1]/a[contains(@href,'tab=Pages')]"
    workspace_groups_XPATH = "/following-sibling::td[2]/a[contains(@href,'tab=Groups')]"
    workspace_users_XPATH = "/following-sibling::td[3]/a[contains(@href,'tab=Users')]"
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
 
    def directNav(self):
        self.driver.get("https://admin.tez.io/workspaces")

    #function will search in the search bar, the if else statement will valiadate if there is text in the search bar already. 
    #If there is then it will clear the text and then send the search params
    def searchFor(self, companyName):
        log.info(f"Searching for {companyName}")
        #pagination will only appear once the page is fully loaded 
        self.wait.until(EC.presence_of_element_located(locator.workspacesElements.pagination_element))
        search = self.driver.find_element(*locator.workspacesElements.search_input)
        if search.get_attribute("value") == "":
            search.send_keys(companyName)
        else:
            self.clearSearch()
            search.send_keys(companyName)

    def clearSearch(self):     
        #pagination will only appear once the page is fully loaded 
        self.wait.until(EC.presence_of_element_located(locator.workspacesElements.pagination_element))
        #Keys sent her since the .clear() wont work in search inputs 
        search = self.wait.until(EC.element_to_be_clickable((locator.workspacesElements.search_input)))
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("cleared search")

    #This function purpose is to locate only on the viewable page,m before using set pagination to all to locate or do a partial search then find in table to view from the results
    def findInTable(self, companyName):
        #wait until table loads
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        log.info(f"starting process to find {companyName} in table")
        if self.wait.until(EC.presence_of_element_located(By.XPATH, f"//table//div[contains(text(),'{companyName}')]")):
            log.info(f"{companyName} found in table")
        else:
            log.error(f"{companyName} not found in table")

    #This function will search the viewable table for like findInTable() but instead will read and log the url of the element if found in table    
    def getURL(self, companyName):
        if self.driver.find_element(By.XPATH, f"//table//div[contains(text(),'{companyName}')]"):
            ws = self.driver.find_element(By.XPATH, f"//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]/div/a[contains(@href,'/workspaces')]")
            url = ws.get_attribute('href')
            log.info(f"found url for: {companyName}, {url}")
        else:
            log.error(f"{companyName} not found in table")

    #Same function as getURL except it will either return the URL of the workspace or it will return "Not Found" 
    def returnURL(self, companyName):
            if self.driver.find_element(By.XPATH, f"//table//div[contains(text(),'{companyName}')]"):
                ws = self.driver.find_element(By.XPATH, f"//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]/div/a[contains(@href,'/workspaces')]")
                url = ws.get_attribute('href')
                log.info(f"found url for: {companyName}, {url}")
                return url
            else:
                log.error(f"{companyName} not found in table")
                url = "Not Found"

#Create Workspace Specific
    def clickCreateBtn(self):
        btn = self.wait.until(EC.visibility_of_element_located(locator.workspacesElements.add_ws_btn))
        btn.click()
    
    def addWSName(self, companyName):
        input = self.driver.find_element(*locator.workspacesElements.dialog_wsName_input)
        input.click()
        input.send_keys(companyName)
    
    def saveNewWS(self):
        self.driver.find_element(*locator.workspacesElements.dialog_save_Btn).click()
    
#Actions
    #This function is used to create the workspace combining the methods above
    def createWorkspace(self, companyName):
        log.info(f"Creating workspace for {companyName}")
        self.clickCreateBtn()
        self.wait.until(EC.visibility_of_element_located(locator.workspacesElements.dialog_whiteSpace))
        self.addWSName(companyName)
        self.saveNewWS()
        log.info(f"Created workspace for {companyName}")

    #This function is used to validate a workspace exists and returns the URL of the workspace
    def validateWorkspace(self, companyName):
        log.info(f"Validating workspace for {companyName} exists")
        self.searchFor(companyName)
        self.findInTable(companyName)
        url = self.returnURL(companyName)
        return url
    

    