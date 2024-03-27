import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from pageobjects.locators.workspace.groups_tab import GroupsElements, DialogElements
import commonUtils.logger as logger
import time

log = logger.setUp()

class Groups:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    # -----------General-----------
    # Direct navigation if base url is known
    def nav(self, url):
        url = url + "?tab=Groups"
        log.info(f"Navigating to {url}")
        self.driver.get(url)
        self.wait.until(EC.presence_of_element_located((GroupsElements.add_new_btn)))

    #this add group will bring up the dialog box 
    def click_add_group(self):
        self.driver.find_element(*GroupsElements.add_new_btn).click()
        log.info("clicking add group button")

    # Expands a specified group to see more details
    def click_expand_group(self, groupName):
        group_options_XPATH = "/ancestor::div[contains(@class, 'relative bg-white')]/descendant::"
        expand_XPATH = "button[contains(@class,'!shadow-non')]"
        expand = self.driver.find_element(By.XPATH, f"//input[@value='{groupName}']{group_options_XPATH}{expand_XPATH}")
        expand.click()
    
    # This clicks the add page button within the expanded group
    def click_add_page(self):
        add_pg = self.wait.until(EC.visibility_of_element_located(GroupsElements.add_page_btn))
        add_pg.click()
    
    # -----------Validations-----------
    # Function looks for a specific group name within the groups tab
    # Returns a True or False 
    def find_group(self, groupName):
        log.info(f"searching for {groupName} on page")
        # WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "div[contains(@class, 'relative bg-white')]")))
        if self.driver.find_element(By.XPATH, f"//input[@value='{groupName}']"):
            log.info(f"Group: {groupName} Created")
            return True
        else:
            log.info(f"Group: {groupName} not found")
            return False

    # Function will count all the pages found in the group package. groupName should be exact and is case sensitive
    # Returns the total count of the pages in the specified group
    def count_pages(self, groupName):
        elements = self.driver.find_elements(By.XPATH, f"//input[contains(@value,'{groupName}')]/ancestor::div[contains(@class, 'relative bg-white')]/descendant::form")
        total = len(elements)
        log.info(f"{groupName} current has {total} pages assigned")
        return total
    
    # Function will iterate through the pages within the groupName passed through the args. groupName should be exact and is case sensitive
    # Returns an array of the pages assigned to the group. 
    def find_pages(self, groupName):
        log.info(f"Retrieving pages in {groupName}")
        select_elements = self.driver.find_elements(By.XPATH, f"//input[contains(@value,'{groupName}')]/ancestor::div[contains(@class, 'relative bg-white')]/descendant::select[@name='page_id']")
        listed_pages = []
        for select_element in select_elements:
            select = Select(select_element)
            selected_option = select.first_selected_option
            log.info(f"Page {selected_option.text} found")
            listed_pages.append(selected_option.text)
        return listed_pages

    # Function validates the contents of the newly created group. Expectation is the group exists
    # This will return a list of the pages that is currently assigned to the group
    def validate_group(self, groupName):
        log.info(f"Validating group: {groupName} has been created")
        self.click_expand_group(groupName)
        actual_count = self.count_pages(groupName)
        log.info(f"{groupName}: has {actual_count} pages assigned")
        listed_pages = self.find_pages(groupName)
        log.info(f"{groupName} contains pages: {listed_pages}")
        return listed_pages
    
    # -----------Actions-----------
    # This function adds a page to a specified group. The function assumes the group does exist
    def add_group_page(self, groupName, pageName):
        log.info(f"Adding page {pageName} to group: {groupName}")
        # expand the specified group
        self.click_expand_group(groupName)
        # click add page
        self.click_add_page()
        # add new page
        new_page = self.wait.until(EC.presence_of_element_located(GroupsElements.last_page_dropdown))
        ac = ActionChains(self.driver)
        ac.move_to_element(new_page)
        ac.click()
        ac.perform()
        log.info("element clickable")
        #time.sleep(5)
        select = Select(new_page)
        select.select_by_visible_text(pageName)
        log.info(f"page has been set to {pageName}")

class Dialog:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.group = Groups(self.driver)

    def click_whitespace(self):
        self.driver.find_element(*DialogElements.ws_dialog_whitespace).click()
        log.info("clicking whitespace in dialog")
    
    def set_group_name(self, groupName):
        name_input = self.wait.until(EC.presence_of_element_located((DialogElements.group_name_input)))
        name_input.click()
        name_input.send_keys(groupName)
        log.info(f"group name input sent as {groupName}")

    # -----------Dialog: Add users section-----------
    # User should use either a full name or an email address for exact results
    def click_user_search(self):
        search = self.wait.until(EC.element_to_be_clickable(DialogElements.assign_users_search))
        search.click()
        log.info("clicking user search bar")
        self.wait.until(EC.presence_of_element_located((DialogElements.assign_users_selections)))
    
    # This is to use the search bar
    def search_user(self, userName):
        self.click_user_search()
        log.info(f"starting search for {userName}")
        search =  self.driver.find_element(*DialogElements.assign_users_search)

        if search.get_attribute("value") == "":
            search.send_keys(userName)
        else:
            self.clear_search()
            search.send_keys(userName)
    
    # Clear the search input, to be used before a new search
    def clear_search(self):
        search = self.driver.find_element(*DialogElements.assign_users_search)
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("cleared search")
    
    # Clicks the element that contains the user name "selecting it" can also "deselect" this can be used to select directly instead of searching and validating
    def select_user(self, userName):
        log.info("selecting user")
        user = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{userName}')]")))
        user.click()

    # This determines if the user is even in the list
    def find_in_list(self, userName):
        log.info(f"looking for {userName} in list")
        if self.driver.find_element(By.XPATH, f"//div[contains(@class, 'flex relative items-center justify-center') and contains(.,'{userName}')]"):
            log.info(f"{userName} found in table")
        else:
            log.error(f"{userName} not found")

    # Returns a boolean value if the user has a checkbox next to their name
    def isChecked(self, userName):
        checkbox = self.driver.find_element(By.XPATH, f"//div[contains(text(),'{userName}')]/ancestor::div[contains(@class, 'cursor-pointer')]/input[@type='checkbox']")
        if checkbox.is_selected():
            print(f"Checkbox is  selected for: {userName}")
            checked = True
        else:
            print(f"Checkbox is not selected for: {userName}")
            checked = False
        return checked
    
    # -----------Dialog: Add Pages Section -----------
    # Clicks the add page button, uncomment time.sleep if debugging
    def add_page_btn(self):
        log.info("Adding pages")
        add_pg = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((DialogElements.add_page_btn)))
        add_pg.click()
        log.info("New Page created")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='w-full flex items-center justify-between py-3 px-4']")))
        #time.sleep(5) 
    
    # Function to select the dropdown, using action chains else the element is not interactable. 
    # Once action chains is able to click the dropdown then select methods can be used
    def select_page(self, pageName):
        log.info(f"Selecting page: {pageName}")
        dropdown = self.driver.find_element(*DialogElements.page_dropdown)
        ac = ActionChains(self.driver)
        ac.move_to_element(dropdown)
        ac.click()
        ac.perform()
        log.info("element clickable")
        #time.sleep(5)
        select = Select(dropdown)
        select.select_by_visible_text(pageName)
        log.info(f"page has been set to {pageName}")
    
    # This is to add more pages after the initial page has been added, the element is looking for the last in the group
    # Process will press the add page button then locate the last (newest) dropdown in the list, made to be iterable
    def add_more_pages(self, pageName):
        self.add_page_btn()
        dropdown = self.driver.find_element(*DialogElements.last_page_dropdown)
        ac = ActionChains(self.driver)
        ac.move_to_element(dropdown)
        ac.click()
        ac.perform()
        #time.sleep(5)
        select = Select(dropdown)
        select.select_by_visible_text(pageName)
        log.info(f"selected {pageName}")
    
    # Clicks the dialog save button
    def click_save_btn(self):
        save = self.driver.find_element(*DialogElements.save_btn)
        log.info("saving new group")
        save.click()
        log.info("New Group Saved")
    
    # This will create a new group from the dialog button. The arguments needed are groupName, users, pageNames
    # groupName should be a string, users and pageNames should be arrays
    def create_group(self, groupName, users, pageNames):
        self.group.click_add_group()
        self.set_group_name(groupName)

        # Add users to the group
        self.click_user_search()
        # Loop clicking all users
        for user in users:
            self.search_user(user)
            if self.isChecked(user) == False:
                self.select_user(user)
            else:
                log.info(f"User {user} is already selected")
        
        # Adding pages
        for i, pageName in enumerate(pageNames):
            # using an index to differentiate the first page and the residual pages
            if i == 0:
                self.add_page_btn()
                self.select_page(pageName)
            else:
                self.add_more_pages(pageName)
        # Click the save button
        self.click_save_btn()

        

