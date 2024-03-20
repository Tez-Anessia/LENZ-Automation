import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from src.locators import ws_locators as locator
import config.logger
import time

log = config.logger.setUp()

class wsgroups:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
    #direct navigation if base url is known
    def directNav(self, url):
        url = url + "?tab=Groups"
        log.info(f"Navigating to {url}")
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located((locator.wsgroupsElements.add_new_btn)))

#Adding a new group section
    def clickAddGroup(self):
        self.driver.find_element(*locator.wsgroupsElements.add_new_btn).click()
        log.info("clicking add group button")
    
#Dialog Box actions
    def dialog_clickwhitespace(self):
        self.driver.find_element(*locator.wsgroupsDialog.ws_dialog_whitespace).click()
        log.info("clicking whitespace in dialog")
    
    def dialog_addGroupName(self, groupName):
        name_input = self.wait.until(EC.presence_of_element_located((locator.wsgroupsDialog.group_name_input)))
        name_input.click()
        name_input.send_keys(groupName)
        log.info(f"group name input sent as {groupName}")

#Dialog: Add users section
    #user should use either a full name or an email address for exact results
    def dialog_clickuserSearch(self):
        self.driver.find_element(*locator.wsgroupsDialog.assign_users_search).click()
        log.info("clicking user search bar")
        self.wait.until(EC.presence_of_element_located((locator.wsgroupsDialog.assign_users_selections)))
    
    #this is to use the search bar
    def dialog_searchUser(self, userName):
        self.dialog_clickuserSearch()
        log.info(f"starting search for {userName}")
        input =  self.driver.find_element(*locator.wsgroupsDialog.assign_users_search)
        input.send_keys(userName)
    
    #clicks the element that contains the user name "selecting it" can also "deselect" this can be used to select directly instead of searching and validating
    def dialog_selectUser(self, userName):
        log.info("selecting user")
        user = self.driver.find_element(By.XPATH, f"//div[contains(text(),'{userName}')]")
        user.click()
    
    #clear the search input, to be used before a new search
    def dialog_clearsearch(self):
        search = self.driver.find_element(*locator.wsgroupsDialog.assign_users_search)
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        self.wait.until(EC.presence_of_element_located((locator.wsgroupsDialog.assign_users_selections)))
        log.info("cleared search")

    #this determines if the user is even in the list
    def dialog_findUserinList(self, userName):
        log.info(f"looking for {userName} in list")
        if self.driver.find_element(By.XPATH, f"//div[contains(@class, 'flex relative items-center justify-center') and contains(.,'{userName}')]"):
            log.info(f"{userName} found in table")
        else:
            log.error(f"{userName} not found")

    #returns a boolean value if the user has a checkbox next to their name
    def dialog_isChecked(self, userName):
        checkbox = self.driver.find_element(By.XPATH, f"//div[contains(text(),'{userName}')]/ancestor::div[contains(@class, 'cursor-pointer')]/input[@type='checkbox']")
        if checkbox.is_selected():
            print(f"Checkbox is  selected for: {userName}")
            checked = True
        else:
            print(f"Checkbox is not selected for: {userName}")
            checked = False
        return checked
    
#Dialog: Add Pages Section
    #clicks the add page button, uncomment time.sleep if debugging
    def dialog_addPageBtn(self):
        log.info("Adding pages")
        add_pg = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator.wsgroupsDialog.add_page_btn)))
        add_pg.click()
        log.info("New Page created")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='w-full flex items-center justify-between py-3 px-4']")))
        #time.sleep(5) 
    
    #function to select the dropdown, using action chains else the element is not interactable. 
    #once action chains is able to click the dropdown then select methods can be used
    def dialog_selectPage(self, pageName):
        log.info(f"Selecting page: {pageName}")
        dropdown = self.driver.find_element(*locator.wsgroupsDialog.page_dropdown)
        ac = ActionChains(self.driver)
        ac.move_to_element(dropdown)
        ac.click()
        ac.perform()
        log.info("element clickable")
        #time.sleep(5)
        select = Select(dropdown)
        select.select_by_visible_text(pageName)
        log.info(f"page has been set to {pageName}")
    
    #This is to add more pages after the initial page has been added, the element is looking for the last in the group
    #process will press the add page button then locate the last (newest) dropdown in the list, made to be iterable
    def dialog_addPage(self, pageName):
        self.dialog_addPageBtn()
        dropdown = self.driver.find_element(*locator.wsgroupsDialog.last_page_dropdown)
        ac = ActionChains(self.driver)
        ac.move_to_element(dropdown)
        ac.click()
        ac.perform()
        #time.sleep(5)
        select = Select(dropdown)
        select.select_by_visible_text(pageName)
        log.info(f"selected {pageName}")
    
    #clicks the dialog save button
    def dialog_save(self):
        save = self.driver.find_element(*locator.wsgroupsDialog.save_btn)
        log.info("saving new group")
        save.click()
        log.info("New Group Saved")
    
    #should be called to validate the new group and the pages have been made    
    def validateNewGroup(self, groupName):
        log.info(f"Validating group: {groupName} has been created")
        self.findGroup(groupName)
        self.expandGroup(groupName)
        self.countPages(groupName)
        listed_pages = self.findPages(groupName)
        return listed_pages  
    
    #Group Actions in tab
    def findGroup(self, groupName):
        log.info(f"searching for {groupName} on page")
        #WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "div[contains(@class, 'relative bg-white')]")))
        if self.driver.find_element(By.XPATH, f"//input[@value='{groupName}']"):
            log.info(f"Group: {groupName} Created")
        else:
            log.info(f"Group: {groupName} not found")
    
    #expands a specified group to see more details
    def expandGroup(self, groupName):
        group_options_XPATH = "/ancestor::div[contains(@class, 'relative bg-white')]/descendant::"
        expand_XPATH = "button[contains(@class,'!shadow-non')]"
        expand = self.driver.find_element(By.XPATH, f"//input[@value='{groupName}']{group_options_XPATH}{expand_XPATH}")
        expand.click()

    #function will count all the pages found in the group package
    def countPages(self, groupName):
        elements = self.driver.find_elements(By.XPATH, f"//input[contains(@value,'{groupName}')]/ancestor::div[contains(@class, 'relative bg-white')]/descendant::form")
        total = len(elements)
        log.info(f"{groupName} current has {total} pages assigned")
        return total
    
    #function will iterate through the select elements related to the searched group and return an array of the selected options 
    def findPages(self, groupName):
        log.info(f"Retrieving pages in {groupName}")
        select_elements = self.driver.find_elements(By.XPATH, f"//input[contains(@value,'{groupName}')]/ancestor::div[contains(@class, 'relative bg-white')]/descendant::select[@name='page_id']")
        listed_pages = []
        for select_element in select_elements:
            select = Select(select_element)
            selected_option = select.first_selected_option
            log.info(f"Page {selected_option.text} found")
            listed_pages.append(selected_option.text)
        return listed_pages