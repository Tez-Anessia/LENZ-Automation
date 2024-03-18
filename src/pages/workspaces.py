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
    
 #--------Singular Functions--------
    def directNav(self):
        self.driver.get("https://admin.tez.io/workspaces")   

    def searchFor(self, companyName):
        log.info(f"Searching for {companyName}")
        #pagination will only appear once the page is fully loaded 
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'bg-white relative')]")))
        
        search = self.driver.find_element(*locator.workspacesElements.search_input)
        if search.get_attribute("value") == "":
            search.send_keys(companyName)
        else:
            self.clearSearch()
            search.send_keys(companyName)

    def clearSearch(self):
        log.info("clearing search bar")
        
        #pagination will only appear once the page is fully loaded 
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'bg-white relative')]")))

        search = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator.workspacesElements.search_input)))
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)

    #locate only, should have view set to All
    def findInTable(self, companyName):
        #wait until table loads
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        log.info(f"starting process to find {companyName} in table")
        if self.driver.find_element(By.XPATH, f"//table//div[contains(text(),'{companyName}')]"):
            log.info(f"{companyName} found in table")
        else:
            log.error(f"{companyName} not found in table")
    
    def getURL(self, companyName):
        if self.driver.find_element(By.XPATH, f"//table//div[contains(text(),'{companyName}')]"):
            ws = self.driver.find_element(By.XPATH, f"//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]/div/a[contains(@href,'/workspaces')]")
            url = ws.get_attribute('href')
            log.info(f"found url for: {companyName}, {url}")
        else:
            log.error(f"{companyName} not found in table")

    def returnURL(self, companyName):
            if self.driver.find_element(By.XPATH, f"//table//div[contains(text(),'{companyName}')]"):
                ws = self.driver.find_element(By.XPATH, f"//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]/div/a[contains(@href,'/workspaces')]")
                url = ws.get_attribute('href')
                log.info(f"found url for: {companyName}, {url}")
                return url
            else:
                log.error(f"{companyName} not found in table")

    #----Create Workspace Specific----
    def clickCreateBtn(self):
        btn = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator.workspacesElements.add_ws_btn))
        btn.click()
    
    def addWSName(self, companyName):
        input = self.driver.find_element(*locator.workspacesElements.dialog_wsName_input)
        input.click()
        input.send_keys(companyName)
    
    def saveNewWS(self):
        self.driver.find_element(*locator.workspacesElements.dialog_save_Btn).click()
    
    #--------Actions--------
    def createWorkspace(self, companyName):
        log.info(f"Creating workspace for {companyName}")
        self.clickCreateBtn()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator.workspacesElements.dialog_whiteSpace))
        self.addWSName(companyName)
        self.saveNewWS()
        log.info(f"Created workspace for {companyName}")

    def validateWorkspace(self, companyName):
        log.info(f"Validating workspace for {companyName} exists")
        self.searchFor(companyName)
        self.findInTable(companyName)
        self.getURL(companyName)
    

    