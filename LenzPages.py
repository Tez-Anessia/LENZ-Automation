import logger
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

log = logger.setUp()
allPages = "https://admin.tez.io/pages?tab=All+pages"
globalPages = "https://admin.tez.io/pages?tab=Global+pages"

#-------Paths-----------
search = "//input[@id='search']"

pagination = "//button[contains(@id, 'headlessui-listbox-button-')]"
showAll = "//p[contains(.,\'All\')]"

inlineMenuBtn = "/following-sibling::td[.//button[contains(@id, 'headlessui-menu')]][1]//button[contains(@id, 'headlessui-menu')]"
menuEditBtn = "//button[contains(.,\'Edit\')]"
menuPreviewBtn = "//button[contains(.,\'Preview\')]"
menuDeleteBtn = "//button[contains(.,\'Delete\')]"

dialogWhiteSpace = "//div[@class='p-4 flex justify-end space-x-4']"
dialogSearch ="(//input[@placeholder='Search'])"
cb = "//input[contains(@type,'checkbox')]"
dialogSubmit = "//button[contains(.,\'Submit\')]"
dialogCancel = "//button[contains(.,\'Cancel\')]"

def getGlobalPages(driver):
    #----navigate to pages-------
    driver.get(globalPages)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".relative:nth-child(2) > .break-all > .flex > .relative > div")))
    

#-----display all items in page------
def showAllPages(driver):
    paginationBox = driver.find_element(By.XPATH, "//button[contains(@id, 'headlessui-listbox-button-')]")
    paginationBox.click()
###delete after test
    time.sleep(2)

    showAll = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(.,\'All\')]")))
    showAll.click()
###delete after test
    time.sleep(2)

def getPagePath(pageName):
    pagePath = "//table/tbody/tr//td[.//div[contains(.,'" + pageName +"')]]"
    return pagePath

def clickpageMenu(driver, pagePath):
    inlineButton = pagePath + "/following-sibling::td[.//button[contains(@id, 'headlessui-menu')]][1]//button[contains(@id, 'headlessui-menu')]"
    menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, inlineButton)))
    menu.click()

def menuEdit(driver):
    #select the edit option
    driver.find_element(By.XPATH, "//button[contains(.,\'Edit\')]").click()

def menuPreview(driver):
    driver.find_element(By.XPATH, "//button[contains(.,\'Preview\')]").click()

def menuDelete(driver):
    driver.find_element(By.XPATH, "//button[contains(.,\'Delete\')]").click()

def addWS(driver, customerName):
    dialogSearchPath ="(//input[@placeholder='Search'])"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dialogSearchPath)))
    search = driver.find_element(By.XPATH, dialogSearchPath)
    search.click()
    search.send_keys(customerName)
    
    time.sleep(2)
    
    workSpaceName = "//div[contains(text(),'"+ customerName +"')]"
    #full checkbox path //div[contains(text(),' "+ var +" ')]//input[contains(@type,'checkbox')]
    cbPath = workSpaceName + "//input[contains(@type,'checkbox')]"
    checkbox = driver.find_element(By.XPATH, cbPath)

    if checkbox.is_selected():
        print("Checkbox is selected.")
    else:
        print("Checkbox is not selected.")
        driver.find_element(By.XPATH, workSpaceName).click()
        time.sleep(4)

def submitWS(driver):
    driver.find_element(By.XPATH, "//div[@class='p-4 flex justify-end space-x-4']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[contains(.,\'Submit\')]").click()
    time.sleep(2)


