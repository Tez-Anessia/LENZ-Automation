import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.locators import global_pages_locators as locator
import config.logger

log = config.logger.setUp()

class pages:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    #Naviagates to the main pages tab
    def directNav(self):
        self.driver.get("https://admin.tez.io/pages")
    
    #navigates to the gobla pages tab
    def directNav_global(self):
        self.driver.get("https://admin.tez.io/pages?tab=Global+pages")
    
    #-----------------Global Pages-----------------
    #this function can be used to add waits to ensure the table has been loaded fully.     
    def table_wait(self):
        #Pagination box is used as the element as it only appears when its fully loaded
        self.wait.until(EC.visibility_of_element_located(locator.pagesElements.pagination_element))

    #This function uses the search bar in the global pages tab
    def search(self, pageName):
        self.table_wait()
        search = self.driver.find_element(*locator.pagesElements.search_input)
        #checks if the search input is empty, if its not clears the text from the field
        if search.get_attribute("value") == "":
            search.send_keys(pageName)
        else:
            self.clear_search()
            search.send_keys(pageName)
    
    #clear search function to clear the text from the field
    def clear_search(self):
        search = self.driver.find_element(*locator.pagesElements.search_input)
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("cleared search")
    
    #Locator function only, reads the viewable table searching for the exact name passed through the args
    def find_in_table(self, pageName):
        self.table_wait()
        isFound = True
        #returns true or false
        if self.driver.find_element(By.XPATH, f"//div[text()='{pageName}']"):
            log.info(f"Page: {pageName} can be found in the table")
            return isFound
        else:
            log.info(f"Page: {pageName} not found in the table")
            isFound = False
            return isFound

    #This function finds the page name
    def page_menu(self, pageName):
        self.table_wait()
        page_menu_XPATH = "/ancestor::tr[@class='relative']/descendant::button[contains(@class, 'max-w-xs')]"
        menubtn = self.driver.find_element(By.XPATH, f"//div[text()='{pageName}']{page_menu_XPATH}")
        menubtn.click()

    #These click the menu options, page menu must be called first
    def menu_options(self, option):
        self.wait.until(EC.visibility_of_element_located(locator.pagesElements.menu_option_edit))
        select = self.driver.find_element(By.XPATH, f"//button[.='{option} ']")
        select.click()
        log.info(f"Selected option {option}")

    #-----------------Global Pages: Edit Dialog Box-----------------
    def dialog_wait(self):
        self.wait.until(EC.visibility_of_element_located(locator.pagesElements.dialog_box))
    #Created to click the search input space, Only way to bring the dropdown into view is by clicking search input
    def dialog_click_search(self):
        self.dialog_wait()
        self.driver.find_element(*locator.pagesElements.dialog_search_input).click()
        self.wait.until(EC.visibility_of_element_located(locator.pagesElements.dialog_search_dropdown))

    #Function to click the whitespace to get out of the dropdown
    def dialog_click_whitespace(self):
        self.driver.find_element(*locator.pagesElements.dialog_whitespace).click()
    
    #searches for a workspace, checks if there is anything in it and clears the input before sending another input
    def dialog_search(self, companyName):
        search = self.driver.find_element(*locator.pagesElements.dialog_search_input)
        
        if search.get_attribute("value") == "":
            search.send_keys(companyName)
            search.click()
        else:
            self.dialog_clearSearch()
            search.send_keys(companyName)
            search.click()

        self.dialog_wait()
    
    #clears search input 
    def dialog_clear_search(self):
        search = self.driver.find_element(*locator.pagesElements.dialog_search_input)
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("cleared search")

    #Checks the dropdown to see if the company is listed
    def dialog_find_dropdown(self, companyName):
        if self.wait.until(EC.visibility_of_element_located(locator.pagesElements.dialog_search_dropdown)):
            log.info("Element found")
        else:
            self.click_dialog_search()
        self.driver.find_element(By.XPATH, f"//div[.='{companyName}']")
        log.info(f"Workspace {companyName} is found in the dropdown")
    
    #Checks if the checkbox is selected, name will need to be searched first
    def dialog_isChecked(self, companyName):
        checkbox = self.driver.find_element(By.XPATH, f"//div[.='{companyName}']//input[@type='checkbox']")
        if checkbox.is_selected():
            log.info("user is checked")
        else:
            log.info("not checked")

    #clicks submit button
    def dialog_submit(self):
        submit_btn = self.driver.find_element(*locator.pagesElements.dialog_submit_btn)
        submit_btn.click()
        self.wait.until(EC.invisibility_of_element_located(locator.pagesElements.dialog_box))
    
    #validates the function exists in the assigned section of the dialog box, returns true or false to evaluate
    def dialog_isAssigned(self, companyName):
        if self.driver.find_element(By.XPATH, f"//p[contains(text(),'{companyName}')]"):
            log.info(f"Workspace: {companyName} assigned to Page")
            #return True
        else:
            log.info(f"Workspace: {companyName} not assigned to Page")
            #return False
    
    #-----------------Actions-----------------
    def dialog_get_all_currerntly_assigned(self):
        pass

    def dialog_add_workspace(self, companyName):
        pass
    def dialog_add_multiple_workspaces(self, companyNames):
        pass