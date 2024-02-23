import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

log = logger.setUp()

def createWorkspace(driver, companyName):
    log.info(f"Creating workspace for {companyName}")
    
    #wait until an element is found due to page loading
    newWSButton = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".-right-2")))
    #click new workspace button
    newWSButton.click()

    #enter workspace name
    workspaceName = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "name")))
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

#this validates the workspace was made and adds the URL to the spreadsheet
def validateWorkspaceURL(driver, companyName):
    driver.get("https://admin.tez.io/workspaces")
    time.sleep(3)

    driver.find_element(By.ID, "search").click()
    driver.find_element(By.ID, "search").send_keys(companyName)
   
    try:
        driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(1) > .break-all .border .transition-all").click()
        url = driver.current_url
        log.info(f"workspace validated, url: {url}")
    except:
        log.info(f"workspace could not be validated")
        url = "not made"

    return url

#Same function with out url for appending the csv
def validateWorkspace(driver, companyName):
    driver.get("https://admin.tez.io/workspaces")
    time.sleep(3)

    driver.find_element(By.ID, "search").click()
    driver.find_element(By.ID, "search").send_keys(companyName)

    try:
        driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(1) > .break-all .border .transition-all").click()
        url = driver.current_url
        log.info(f"workspace validated, url: {url}")
    except:
        log.info(f"workspace could not be validated")

