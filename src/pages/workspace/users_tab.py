import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.locators.workspace.users_tab import UserElements, DialogElements
from src.locators.workspace.ws_locators import WorkspaceProfile as profile

from selenium.common.exceptions import StaleElementReferenceException

import config.logger

log = config.logger.setUp()

class Users:
        
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def page_wait(self):
        try:
            self.wait.until(EC.presence_of_element_located(UserElements.user_menu_btn))
        except:
            log.error("no elements in table")

    def nav(self, url):
        url = url + "?tab=Users"
        log.info(f"Navigating to {url}")
        self.driver.get(url)
        self.page_wait()  

    def click_user_tab(self):
        self.driver.find_element(*profile.users_tab).click()
        self.page_wait()

    # Function which sends the value of user to the search bar input
    # If Else statement will check if the field is empty. If its not, then it will clear the input field then send the search params 
    def search(self, user):
        log.info(f"Searching for page: {user}")
        search = self.wait.until(EC.presence_of_element_located(UserElements.search_input))
        if search.get_attribute("value") == "":
            search.send_keys(user)
        else:
            self.clear_search()
            search.send_keys(user)

    # Function to clear the input from the search field
    def clear_search(self):
        search = self.driver.find_element(*UserElements.search_input) 
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("cleared search")
    
    # Function to check if the value set to the user variable is in the visible table
    # Created to work with other functions as a validation for the present element
    # Returns True of False to allow the program to evaluate
    def find_in_table(self, user):
        self.page_wait()
        isFound = True
        log.info(f"starting process to find {user} in table")
        if self.driver.find_element(By.XPATH, f"{UserElements.userName_XPATH}//a[normalize-space()='{user}']"):
            log.info(f"{user} found in table")
        else:
            log.error(f"{user} not found in table")
            isFound = False
        return isFound

    #-----------------Add Existing-----------------
    def click_add_user(self):
        log.info("clicking add user button")
        self.driver.find_element(*UserElements.add_user_btn).click()

# Currently this class functions contain interactions and actions for Add Existing option
# This class can be expanded on, locators for the other elements are available in the locator file. 
class Dialog:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.user = self.Users(self.driver)
    
    #-----------------Dialog Box: Add User-----------------
    # Needs to have the dialog box present before using
    def click_add_existing(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='flex justify-between py-4 px-4']")))
        log.info("clicking add existing button")
        button = self.wait.until(EC.presence_of_element_located(DialogElements.add_existing_btn))
        button.click()
        self.wait.until(EC.presence_of_element_located((DialogElements.exsiting_user_whitespace)))

    #-----------------Dialog Box: Add Exisiting-----------------
    def click_existing_search(self):
        try:
            log.info("clicking search input")
            search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            search.click()
        except StaleElementReferenceException:
            log.info("element not found, retrying search click")
            # Element is stale, find it again
            search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
            search.click()
            # Retry actions on the element

    # Click the whitespace in assign existing user dialog box, used to get the dialog box out of view to perform other actions
    def click_existing_whitespace(self):
        log.info("Click whitespace")
        self.driver.find_element(*DialogElements.exsiting_user_whitespace).click()
    
    # Clicks the submit button in assign existing user dialog box
    def click_existing_submit(self):
        self.driver.find_element(*DialogElements.submit_btn).click()

    #-----------------Actions-----------------
    # Function adds a single user to the workspace
    def assign_user(self, user):
        self.click_existing_search() #to bring the dialog box into view
        log.info(f"Searching for user: {user} in table ")
        user_element = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[contains(@class,'flex relative items-center')]//div[.='{user}']")))
        user_element.click()
        log.info(f"Added user {user}")
        
        # Click out of the dropdown so submit button is in view
        self.click_existing_whitespace()
        # Click submit
        self.click_existing_submit()
    
        # Wait for the table to populate with the new users
        self.page_wait()
        
        # Validate that the users have been added
        self.find_in_table(user)
        log.info(f"User: {user} found in table")
 
    # Function which accepts an array and iterates through users adding multiple at once then validates that the users were added to the workspace 
    def assign_users(self, users):
        self.click_existing_search() #to bring the dialog box into view
        log.info(f"Searching for user: {user} in table ")
        
        # Iterate through the opened dropdown and find the array of users
        for user in users:
            user_element = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[contains(@class,'flex relative items-center')]//div[.='{user}']")))
            user_element.click()
            log.info(f"Added user {user}")
        
        # Click out of the dropdown so submit button is in view
        self.click_existing_whitespace()
        # Click submit
        self.click_existing_submit()
        # Wait for the table to populate with the new users
        self.page_wait()
        # Validate that the users have been added
        log.info("Validating users have been added to workspace")
        for user in users:
            self.find_in_table(user)
            log.info(f"User: {user} found in table")

