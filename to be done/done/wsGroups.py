import config.logger as logger
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = logger.setUp()

#---new group elements----
addGroupBtn = (By.CSS_SELECTOR, ".-right-2") #altpath //div[@class='relative ml-[-2px] group']

#Add new Group Dialog box
dialogWS = "//div[contains(@class,'flex justify-between py-4 px-4')]"
dialogGroupName = (By.XPATH, "//input[@name='name']")
dialogSaveBtn = "//button[contains(text(),'Save')]"

#----Assigned Users section = AU ----
dialogAUSearch = (By.XPATH, "//input[@placeholder='Search']")
dialogAUList = "//div[contains(text(),'"+ customerName +"')]"
dialogAUCB = "//input[contains(@type,'checkbox')]"

#----Add Pages section----
dialogAPbtn = "//div[contains(text(),'Add Page')]"
#//div[contains(@data-headlessui-state,'open')]//div//div//div//div//div//div//div[contains(@data-rbd-droppable-id,'droppable')]//div//form[contains(@action,'#')]//div//div//div//div//select[contains(@name,'page_id')]
dialogPageSelect = "(//select[@name='page_id'])" #multiple would have (//select[@name='page_id'])[1], etc where 1 goes up. 

#---group settings for existing groups----
groupSettings = "//div[@class='text-gray-400 hover:text-gray-500 h-full hover:bg-gray-50 py-2 px-2 rounded-md flex items-center justify-center']"
gsMenuUsers = "//button[contains(text(),'Manage Users')]"
gsMenuPage = "//button[contains(text(),'Add page')]"
gsMenuClone = "//button[contains(text(),'Clone group')]"
gsMenuDelete = "//button[contains(text(),'Delete group')]"

groupPgDropdown = "//select[@name='page_id']"

#----Groups Tab----
def addGroup(driver):
    driver.find_element(By.CSS_SELECTOR, ".-right-2").click()

#----Dialog Box Functions----
def clickWhiteSpace(driver):
    driver.get_element(By.XPATH, "//div[contains(@class,'flex justify-between py-4 px-4')]").click()

def enterName(driver, groupName):
    search = driver.get_element(By.XPATH, "//input[@name='name']")
    search.click()
    search.send_keys(groupName)

#----Dialog: Add Users section ----
# user should use either a full name or an email address for exact results
def searchUser(driver, user):
    #search user in search bar
    searchUser = driver.get_element(By.XPATH, "//input[@placeholder='Search']")
    searchUser.click()
    #clear any text that may be in the search
    searchUser.clear()
    searchUser.send_keys(user)

#this function only works after search user since there should only be one result
def isChecked(driver):
    checkbox = driver.get_element(By.XPATH, "//input[contains(@type,'checkbox')]")
    if checkbox.is_selected():
        print("Checkbox is selected.")
        checked = True
    else:
        print("Checkbox is not selected.")
        checked = False
    return checked

def selectUser(driver, user):
    user = driver.get_element(By.XPATH, "//div[contains(text(),'"+ user +"')]")
    user.click()

#----Dialog: Add Pages ----
def addPageBtn(driver):
    addPagebtn = driver.get_element(By.XPATH, "//div[contains(text(),'Add Page')]")
    addPagebtn.click()

#use this function when adding a page to a group with no exisiting pages
def addPage(driver, pageName):
    dropdown = driver.find_element(By.XPATH, "//select[@name='page_id']")
    dropdown.click()
    dropdown.find_element(By.XPATH, f"//option[. = '{pageName}']").click()

#use this function to add a page to an exisiting list
def addMorePages(driver, pageName):
    #get last element using [last()] for the index
    dropdown = driver.find_element(By.XPATH, "(//select[@name='page_id'])[last()]")
    dropdown.click()
    dropdown.find_element(By.XPATH, f"//option[. = '{pageName}']").click()

def saveDialog(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click

