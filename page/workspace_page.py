from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WSPage:

    def __init__(self, driver):
        self.driver = driver
        #--------Locators--------
        #---add new workspace----
        self.addWorkSpacebtn = (By.XPATH, "//button[@data-tooltip-id='Add a workspace-custom-link']")
        self.newWS_nametxtbox = (By.XPATH, "//input[@name='name']")
        self.newWS_savebtn = (By.XPATH, "//button[normalize-space()='Save']")
        self.newWS_cancelbtn = (By.XPATH, "//button[normalize-space()='Cancel']")
        
        #-----Worspaces page------
        self.searchWS_txtbox = (By.XPATH, "//input[@id='search']")
        #-----Table Elemements-----
        /following-sibling::td[.//a[contains(@href,'?tab=Users')][1]]
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

    def clickCreateBtn(self):
        self.driver.get_element(self.addWorkSpacebtn).click()
    
    def addWSName(self, companyName):
        self.driver.get_element(self.newWS_nametxtbox).click()
        self.driver.get_element(self.newWS_nametxtbox).send_keys(companyName)
    
    def saveNewWS(self):
        self.driver.get_element(self.newWS_savebtn).click()
    
    def cancelNewWS(self):
        self.driver.get_element(self.newWS_cancelbtn).click()

    def searchFor(self, companyName):
        self.driver.get_element(self.searchWS_txtbox).click()
        self.driver.find_element(self.searchWS_txtbox).clear()
        self.driver.get_element(self.searchWS_txtbox).send_keys(companyName)

    def clearSearch(self):
        self.driver.get_element(self.searchWS_txtbox).click()
        self.driver.find_element(self.searchWS_txtbox).clear()
    
    def seeAllWS(self):
        self.driver.find_element(self.paginationBox).click()
        self.addElementWait(self.seeAll)
        self.driver.find_element(self.seeAll).click()
    
    def findInTable(self, customerName):
       self.driver.find_element(By.XPATH, "//div[contains(text(),'"+ customerName +"')]")                        

    def selectWorkspace(self, customerName):
        ws = self.driver.find_element(By.XPATH, "//table/tbody/tr/td[.//div[contains(text(),'"+ customerName +"')]]")
        ws.click()
        
    def getWSpath(self, customerName):
        ws = "//table/tbody/tr/td[.//div[contains(text(),'"+ customerName +"')]]"
        return ws 
    
    #this works off the getWSpath function
    def clickWSPages(self, path):
        wsPath = path
        pagesPath = wsPath + self.pages
        self.driver.get_element(pagesPath).click()
    

#--------Actions--------
    def createWorkspace(self, companyName):
        self.addElementWait(self.addWorkSpacebtn)
        self.clickCreateBtn()

        self.addElementWait(self.newWS_nametxtbox)
        self.addWSName(companyName)
        self.saveNewWS()
        