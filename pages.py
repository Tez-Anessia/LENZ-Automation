import logger
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

log = logger.setUp()
allPages = "https://admin.tez.io/pages?tab=All+pages"
globalPages = "https://admin.tez.io/pages?tab=Global+pages"

def getGlobalPages(driver):
    #----navigate to pages-------
    driver.get(globalPages)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".relative:nth-child(2) > .break-all > .flex > .relative > div")))
    
    #-----display all items in page------
    paginationBox = driver.find_element(By.XPATH, "//button[contains(@id, 'headlessui-listbox-button-')]")
    paginationBox.click()
    
    showAll = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(.,\'All\')]")))
    showAll.click()

def findPage(driver, pageName, customerName):
    tableElement = "//table/tbody/tr"
    pageNameElement= tableElement + "//td[.//div[contains(.,'" + pageName +"')]]"
    inlineButton = pageNameElement + "/following-sibling::td[.//button[contains(@id, 'headlessui-menu')]][1]//button[contains(@id, 'headlessui-menu')]"
    
    #full button path //table/tbody/tr//td[.//div[contains(.,'Text2Park')]]/following-sibling::td[.//button[contains(@id, 'headlessui-menu')]][1]//button[contains(@id, 'headlessui-menu')]
    menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, inlineButton)))
    menu.click()

    #select the edit option
    driver.find_element(By.XPATH, "//button[contains(.,\'Edit\')]").click()

    #click on search button 
    dialogSearchPath ="(//input[@placeholder='Search'])"

    workSpaceName = "//div[contains(text(),'"+ customerName +"')]"
    #full checkbox path //div[contains(text(),'8th Street Development')]//input[contains(@type,'checkbox')]
    checkbox = workSpaceName + "//input[contains(@type,'checkbox')]"
        
    time.sleep(4)
