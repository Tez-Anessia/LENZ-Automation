'''
Note this page needs work to add wait elements when there are less than 10 pages assigned to a workspace.
wait is currently set to work when there is the presence of a pagination box. 
'''
import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys;
from src.locators import ws_locators as locator
import config.logger

log = config.logger.setUp()

class wspages:
    
    def __init__(self, driver):
        self.driver = driver

    def pageLoadWait(self):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[starts-with(text(),'User record')]")))
        except:
            log.error("no elements in table")

    def directNav(self, url):
        url = url + "?tab=Pages"
        log.info(f"Navigating to {url}")
        self.driver.get(url)
        self.pageLoadWait()

    def pagesTabClick(self):
        self.driver.find_element(*locator.wsprofileElements.pages_tab).click()
        self.pageLoadWait()

    def searchPages(self, pageName):
        log.info(f"Searching for page: {pageName}")
        search = self.driver.find_element(*locator.wspagesElements.search_input) 
        search.click()
        search.send_keys(pageName)
    
    def clearSearch(self):
        log.info("clearing search input")
        search = self.driver.find_element(*locator.wspagesElements.search_input)
        search.send_keys(Keys.CONTROL, "a")
        search.send_keys(Keys.DELETE)
        self.pageLoadWait()

    def findInTable(self, pageName):
        self.pageLoadWait()
        log.info(f"starting process to find {pageName} in table")
        if self.driver.find_element(By.XPATH, f"//table/tbody/tr//td[.//div[contains(.,'{pageName}')]]"):
            log.info(f"{pageName} found in table")
        else:
            log.error(f"{pageName} not found in table")
    
    #set pagination to all before using this, only reads the visible table
    def listCurrentPages(self):
        try:
            self.pageLoadWait()
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