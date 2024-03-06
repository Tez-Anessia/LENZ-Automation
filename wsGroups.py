import logger
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
//div[contains(@data-headlessui-state,'open')]//div//div//div//div//div//div//div[contains(@data-rbd-droppable-id,'droppable')]//div//form[contains(@action,'#')]//div//div//div//div//select[contains(@name,'page_id')]

#---group settings for existing groups----
groupSettings = "//div[@class='text-gray-400 hover:text-gray-500 h-full hover:bg-gray-50 py-2 px-2 rounded-md flex items-center justify-center']"
gsMenuUsers = "//button[contains(text(),'Manage Users')]"
gsMenuPage = "//button[contains(text(),'Add page')]"
gsMenuClone = "//button[contains(text(),'Clone group')]"
gsMenuDelete = "//button[contains(text(),'Delete group')]"

groupPgDropdown = "//select[@name='page_id']"

def iterate(driver):
    # Find all forms within the parent element
    forms = parent_element.find_elements(By.XPATH, ".//form")

    # Iterate through each form
    for form in forms:
        parent_element = driver.find_element(By.XPATH, "//*[@id='headlessui-dialog-panel-50']/div[2]/div/div[2]/div[2]/div[2]")

        # Find the dropdown element within the form
        dropdown = form.find_element(By.XPATH, ".//select")
        
        # Select an option from the dropdown
        select = Select(dropdown)
        select.select_by_visible_text("Option 1")  # Replace "Option 1" with the text of the option you want to select
        
        # Perform other actions on the form as needed
        
