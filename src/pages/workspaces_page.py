import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys;
from src.locators import workspaces_locators as locator
import config.logger

log = config.logger.setUp()

class workspaces:
    
    def __init__(self, driver):
        self.driver = driver
    
 #--------Singular Functions--------
    def openWS(self):
        self.driver.get("https://admin.tez.io/workspaces")   

    def searchFor(self, companyName):
        search = self.driver.find_element(*locator.pageElements.search_input)
        search.click()
        search.send_keys(companyName)

    def clearSearch(self):
        search = self.driver.find_element(*locator.pageElements.search_input)
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
        btn = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator.pageElements.addWorkspace))
        btn.click()
    
    def addWSName(self, companyName):
        input = self.driver.find_element(*locator.pageElements.wsName_input)
        input.click()
        input.send_keys(companyName)
    
    def saveNewWS(self):
        self.driver.find_element(*locator.pageElements.save_Btn).click()
    
    #--------Actions--------
    def createWorkspace(self, companyName):
        log.info(f"Creating workspace for {companyName}")
        self.clickCreateBtn()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator.pageElements.dialog_whiteSpace))
        self.addWSName(companyName)
        self.saveNewWS()
        log.info(f"Created workspace for {companyName}")

        self.validateWorkspace(companyName)

    def validateWorkspace(self, companyName):
        log.info(f"Validating workspace for {companyName} exists")
        self.clearSearch()
        self.searchFor(companyName)
        self.findInTable(companyName)
        self.getURL(companyName)
    

    