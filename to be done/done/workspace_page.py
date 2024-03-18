from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WSPage:

    def __init__(self, driver):
        self.driver = driver
        #--------Locators--------
        #---add new workspace----
        self.addWorkSpacebtn = (By.XPATH, "//button[@data-tooltip-id='Add a workspace-custom-link']")
        self.newWS_nametxtbox = (By.XPATH, "//input[@name='name']")
        self.newWS_savebtn = (By.XPATH, "//button[normalize-space()='Save']")
        self.newWS_cancelbtn = (By.XPATH, "//button[normalize-space()='Cancel']")
        
        #-----Worspaces page XPaths (dynamic)------
        self.searchWS_txtbox = (By.XPATH, "//input[@id='search']")
        #-----Table Elemements-----
        self.wsName = "(//div[@class='w-full flex gap-x-3 items-center relative'])"
        #/following-sibling::td[.//a[contains(@href,'?tab=Users')][1]]
        self.pages = "/following-sibling::td[.//a[contains(@href,'?tab=Pages')][1]]"
        self.groups = "/following-sibling::td[.//a[contains(@href,'?tab=Groups')][1]]"
        self.users = "/following-sibling::td[.//a[contains(@href,'?tab=Users')][1]]"
        
        #-----Pagination-----
        self.paginationBox = (By.XPATH, "//button[@aria-haspopup='listbox']")
        self.see10 = (By.XPATH, "//p[normalize-space()='10']")
        self.see20 = (By.XPATH, "//p[normalize-space()='20']")
        self.see50 = (By.XPATH, "//p[normalize-space()='50']")
        self.see75 = (By.XPATH, "//p[normalize-space()='75']")
        self.see100 = (By.XPATH, "//p[normalize-space()='100']")
        self.seeAll = (By.XPATH, "//p[normalize-space()='All']")

#--------Singular Functions--------
    def openWS(self):
        self.driver.get("https://admin.tez.io/workspaces")
    
    def addElementWait(self, element):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((element)))
    
    #----On Page----
    def searchFor(self, companyName):
        search = self.driver.get_element(*self.searchWS_txtbox)
        search.click()
        search.clear()
        search.send_keys(companyName)

    def clearSearch(self):
        search = self.driver.get_element(*self.searchWS_txtbox)
        search.click()
        search.clear()
    
    def seeAllWS(self):
        page = self.driver.find_element(*self.paginationBox)
        page.click()
        
        option = self.driver.find_element(*self.seeAll)
        self.addElementWait(self.seeAll)
        option.click()
    
    def findInTable(self, customerName):
       self.driver.find_element(By.XPATH, f"//div[contains(text(),'{customerName}')]")                        

#THIS GETS THE URL INSTEAD
    def selectWorkspace(self, customerName):
        ws = self.driver.find_element(By.XPATH, f"//table/tbody/tr/td[.//div[contains(text(),'{customerName}')]]/div/a[contains(@href,'/workspaces')]")
        url = ws.get_attribute('href')
        print(url)
        ws.click()
        
    def getWSpath(self, customerName):
        ws = f"//table/tbody/tr/td[.//div[contains(text(),'{customerName}')]]"
        return ws 
    
    #this works off the getWSpath function
    def clickWSPages(self, path):
        wsPath = path
        pagesPath = wsPath + self.pages
        self.driver.find_element(By.XPATH, pagesPath).click()
    
    #----Create Workspace Specific----
    def clickCreateBtn(self):
        btn = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((self.addWorkSpacebtn)))
        btn.click()
    
    def addWSName(self, companyName):
        input = self.driver.find_element(*self.newWS_nametxtbox)
        self.addElementWait(self.newWS_nametxtbox)
        input.click()
        input.send_keys(companyName)
    
    def saveNewWS(self):
        self.driver.find_element(*self.newWS_savebtn).click()
    
    def cancelNewWS(self):
        self.driver.find_element(*self.newWS_cancelbtn).click()
    
#--------Actions--------
    def createWorkspace(self, companyName):
        self.clickCreateBtn()

        self.addWSName(companyName)
        self.saveNewWS()
    
    def findWorkspace(self, companyName):
        self.seeAllWS()
        
        lastWS = (By.XPATH, "(//div[@class='w-full flex gap-x-3 items-center relative'])[last()]")
        self.addElementWait(lastWS)

        self.findInTable(companyName)
        self.selectWorkspace(companyName)
        time.sleep(2)
        print(self.driver.current_url)
