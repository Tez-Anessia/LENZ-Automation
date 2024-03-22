'''
Note this page needs work to add wait elements when there are less than 10 pages assigned to a workspace.
wait is currently set to work when there is the presence of a pagination box. 
'''
import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.locators.workspace.pages_tab import PagesElements
from src.locators.workspace.ws_locators import WorkspaceProfile
import config.logger

log = config.logger.setUp()

class Pages:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def page_wait(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[starts-with(text(),'User record')]")))
        except:
            log.error("no elements in table")

    def nav(self, url):
        url = url + "?tab=Pages"
        log.info(f"Navigating to {url}")
        self.driver.get(url)
        self.page_wait()

    # Function to search using the search bar
    def search(self, pageName):
        log.info(f"Searching for page: {pageName}")
        search = self.driver.find_element(*PagesElements.search_input)
        if search.get_attribute("value") == "":
            search.send_keys(pageName)
        else:
            self.clear_search()
            search.send_keys(pageName)

    def clear_search(self):
        search = self.driver.find_element(*PagesElements.search_input)
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        log.info("cleared search input")
        self.page_wait()

    def click_pages_tab(self):
        self.driver.find_element(*WorkspaceProfile.pages_tab).click()
        self.page_wait()
    
    # Function to find the page in the visibile table
    # To search all use pagination to set to all or use the search function then find in table to find specific
    def find_in_table(self, pageName):
        self.page_wait()
        log.info(f"starting process to find {pageName} in table")
        if self.driver.find_element(By.XPATH, f"//table/tbody/tr//td[.//div[contains(.,'{pageName}')]]"):
            log.info(f"{pageName} found in table")
        else:
            log.error(f"{pageName} not found in table")
    
    #-----------------Actions-----------------   
    # Set pagination to all before using this, only reads the visible table goes through the table and puts all the pages in the workspace into an array then returns the array
    def get_all_pages(self):
        try:
            self.page_wait()
            log.info("Reading table for all pages")
            # Find the index of the 'name' column
            header_elements = self.driver.find_elements(By.XPATH, "//table//th")
            column_index = -1
            for index, header_element in enumerate(header_elements):
                if header_element.text.strip().lower() == "name":
                    column_index = index
                    break

            # Extract text from 'name' column cells
            page_titles = []
            if column_index != -1:
                rows = self.driver.find_elements(By.XPATH, "//table//tr")
                for row in rows[1:]:  # Skip the header row
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if len(cells) > column_index:
                        page_title = cells[column_index].text.strip()  # Initialize page_title here
                        #Remove '\nGlobal' if present
                        page_title = page_title.replace('\nGlobal', '')
                        page_titles.append(page_title)

            log.info(f"Workspace has {len(page_titles)} pages assigned to it")
            log.info(f"Current pages are: {page_titles}")
            return page_titles
        except Exception as e:
            log.error(f"Error occurred while extracting text from 'name' column in table: {str(e)}")
            return []