import logger
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


log = logger.setUp()

#----This creates the workspace itself----
def createWorkspace(driver, companyName):
    log.info(f"Creating workspace for {companyName}")
    
    #wait until an element is found due to page loading
    newWSButton = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".-right-2")))
    #click new workspace button
    newWSButton.click()

    #enter workspace name
    workspaceName = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='name']")))
    workspaceName.click()
    workspaceName.send_keys(companyName)

    saveButton = driver.find_element(By.CSS_SELECTOR, ".inline-flex:nth-child(2)")
    try:
        saveButton.click()
        # wait time is added
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    except Exception as e:
        log.error(f"Failed to click element: {e}")

    log.info(f"Workspace for {companyName} created")

#---searches workspace and returns the name of the first element in the list -----
def searchWorkspace(driver, companyName):
    driver.get("https://admin.tez.io/workspaces")
    time.sleep(3)  # Optional initial sleep
    
    search_input = driver.find_element(By.ID, "search")
    search_input.click()
    search_input.clear()  # Clear existing text
    search_input.send_keys(companyName)

    # Wait for the element to become visible
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".relative:nth-child(1) > .break-all .w-\\[100px\\]")))
    time.sleep(5)  # Additional wait time after sending keys

    element = driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(1) > .break-all .w-\\[100px\\]")
    name = element.text
    return name


def clearSearch(driver):
    # Click on the search field to focus on it
    driver.find_element(By.ID, "search").click()

    # Clear any existing text in the search field
    driver.find_element(By.ID, "search").clear()

#---Workspace will keep searching for the company name until the first element found matches what we are searching
    #---Since its an exact search, it should always be the first element found
def validateWorkspaceURL(driver, companyName):
    maxTries = 5
    tries = 0

    while tries < maxTries:
        try:
            name = searchWorkspace(driver, companyName)
            if name == companyName:
                log.info("matched")
                driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(1) > .break-all .border .transition-all").click()
                url = driver.current_url
                return url
            else:
                log.info("Doesn't match. Trying again...")
                tries += 1
        except NoSuchElementException as e:
            log.error("NoSuchElementException: " + str(e))
            log.info(f"Element {companyName} not found in workspace")
            return "not in workspace"
            
    if tries == maxTries: 
        log.info("Unable to find workspace after {} tries".format(maxTries))
        return "not in workspace"

#Same function with out url for appending the csv
def validateWorkspace(driver, companyName):
    maxTries = 5
    tries = 0
    while tries < maxTries:
        name = searchWorkspace(driver, companyName)
        if name == companyName:
            log.info("matched")
            driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(1) > .break-all .border .transition-all").click()
            url = driver.current_url
            log.info(f"workspace validated, url: {url}")
        else:
            log.info("Doesn't match. Trying again...")
            tries += 1
        
    
    if tries == maxTries: 
        log.info("unable to find workspace")


        

