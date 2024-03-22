'''
Pages includes 2 classes currently: pages and dialog.

Pages class: navigation and interactions for Global Pages tab.
Dialog class: navigation, actions and interaction for the pop up when "Edit" menu option is selected for a specific page

'''

import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.locators.pages import PagesElements, DialogElements
import config.logger

log = config.logger.setUp()

class Pages:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    # Naviagates to the main pages tab
    def nav(self):
        self.driver.get("https://admin.tez.io/pages")
    
    # Navigates to the global pages tab
    def nav_global(self):
        self.driver.get("https://admin.tez.io/pages?tab=Global+pages")
    
    #-----------------Global Pages-----------------
    # Function which can be used to add waits to ensure the table has been loaded fully.  
    def table_wait(self):
        # Pagination box is used as the element as it only appears when its fully loaded
        self.wait.until(EC.visibility_of_element_located(PagesElements.pagination_element))

    # Function which sends the value of pageName to the search bar input
    # If Else statement will check if the field is empty. If its not, then it will clear the input field then send the search params 
    def search(self, pageName):
        self.table_wait()
        search = self.driver.find_element(*PagesElements.search_input)
        # Checks if the search input is empty, if its not clears the text from the field
        if search.get_attribute("value") == "":
            search.send_keys(pageName)
        else:
            self.clear_search()
            search.send_keys(pageName)
    
    # Clear search function to clear the text from the field
    def clear_search(self):
        search = self.driver.find_element(*PagesElements.search_input)
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("cleared search")
    
    # Function reads the viewable table searching for the exact name passed through the args
    # Returns True or False
    def find_in_table(self, pageName):
        self.table_wait()
        isFound = True
        if self.driver.find_element(By.XPATH, f"//div[text()='{pageName}']"):
            log.info(f"Page: {pageName} can be found in the table")
            return isFound
        else:
            log.info(f"Page: {pageName} not found in the table")
            isFound = False
            return isFound

    # This function selects a menu option for a specified page
    # menuOption must be exact and case sensitive
    def select_menu_option(self, pageName, menuOption):
        # Find the menu button for the specified page (pageName)
        self.table_wait()
        page_menu_XPATH = "/ancestor::tr[@class='relative']/descendant::button[contains(@class, 'max-w-xs')]"
        menubtn = self.driver.find_element(By.XPATH, f"//div[text()='{pageName}']{page_menu_XPATH}")
        menubtn.click()

        # Select menu option
        # Once the menu option is visible, select the option passed through menuOption
        self.wait.until(EC.visibility_of_element_located(PagesElements.menu_option_edit))
        select = self.driver.find_element(By.XPATH, f"//button[.='{menuOption} ']")
        select.click()
        log.info(f"Selected option {menuOption}")

        # Wait until the dialog box appears
        self.wait.until(EC.visibility_of_element_located(DialogElements.dialog_whitespace))

class Dialog:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        # Pages object created to get to the correct dialog box to perform the desired actions
        self.pages = Pages(driver)
    
    #-----------------Global Pages: Edit Dialog Box-----------------
    def dropdown_wait(self):
        self.wait.until(EC.visibility_of_element_located(DialogElements.dialog_box))
    
    # Function created to click the search input space, Only way to bring the dropdown into view is by clicking search input
    def click_search(self):
        self.wait()
        self.driver.find_element(*DialogElements.search_input).click()
        self.wait.until(EC.visibility_of_element_located(DialogElements.search_dropdown))

    # Function to click the whitespace to get out of the dropdown
    def click_whitespace(self):
        self.driver.find_element(*DialogElements.dialog_whitespace).click()
    
    # Searches for a workspace, checks if there is anything in it and clears the input before sending another input
    def search(self, companyName):
        search = self.driver.find_element(*DialogElements.search_input)
        
        if search.get_attribute("value") == "":
            search.send_keys(companyName)
            search.click()
        else:
            self.dialog_clearSearch()
            search.send_keys(companyName)
            search.click()
        self.wait()
    
    # Clears search input 
    def clear_search(self):
        search = self.driver.find_element(*DialogElements.search_input)
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("cleared search")

    # Checks the dropdown to see if the company is listed
    def find_in_dropdown(self, companyName):
        if self.wait.until(EC.visibility_of_element_located(DialogElements.search_dropdown)):
            log.info("Element found")
        else:
            self.click_dialog_search()
        self.driver.find_element(By.XPATH, f"//div[.='{companyName}']")
        log.info(f"Workspace {companyName} is found in the dropdown")
    
    # Checks if the checkbox is selected, name will need to be searched first
    def isChecked(self, companyName):
        checkbox = self.driver.find_element(By.XPATH, f"//div[.='{companyName}']//input[@type='checkbox']")
        if checkbox.is_selected():
            log.info("user is checked")
        else:
            log.info("not checked")

    # Clicks submit button
    def click_submit(self):
        submit_btn = self.driver.find_element(*DialogElements.submit_btn)
        submit_btn.click()
        self.wait.until(EC.invisibility_of_element_located(DialogElements.dialog_box))
    
    # Function which validates the function exists in the assigned section of the dialog box, returns true or false to evaluate
    def isAssigned(self, companyName):
        if self.driver.find_element(By.XPATH, f"//p[contains(text(),'{companyName}')]"):
            log.info(f"Workspace: {companyName} assigned to Page")
            #return True
        else:
            log.info(f"Workspace: {companyName} not assigned to Page")
            #return False
    
    #-----------------Actions-----------------
    # Function which will iterate through all the currently assigned workspaces and return an array of the workspaces assigned
    def get_assigned(self, pageName):
        self.pages.select_menu_option(pageName, "Edit")
        assigned=[] #array to hold the workspace names
        elements = self.driver.find_elements(*DialogElements.dialog_bubbles)
        #count can be used for debugging in the logs to ensure the company names returned match the elements counted
        count = len(elements)
        log.info(f"There are {count} workspaces assigned to {pageName}")
        log.info(f"Getting list of workspaces")
        for element in elements:
            workspace = element.text
            assigned.append(workspace)
        
        log.info(f"Workspaces assigned to {pageName} are: {assigned}")

    # This function will add a workspace to the page. This function should be called once the dialog has already been opened
    def add_workspace(self, companyName):
        #check for presence of dialog

        #click search
        #send workspace keys
        #validate the dropdown is present, else click the search bar
        #find in dropdown
        #click dropdown element
        #validate the page has been added 
        pass

    # Works the same as add_workspace except anticpates companyNames is an array it can iterate through
    def add_multiple_workspaces(self, companyNames):
        pass
    
    # Function which will check to see if the workspace passed as companyName is present in the assigned section of the dialog box
    # Will return True or false to evaluate how to proceed
    def validate(self):
        pass