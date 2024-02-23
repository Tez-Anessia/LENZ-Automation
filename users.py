import logger
import getdata as data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

log = logger.setUp()

#Note: add existing users will not populate users already added as an option
def navUser(driver, url):
    #click on user tab within a specific workspace
    usertab = url + "?tab=Users"
    print(usertab)
    driver.get(usertab)

def addUsers(driver, salesPerson):

    #get standard user list and add the sales rep to the array
    users = combineUsers(salesPerson)
    log.info(f"users list: {users}")

    # add users button (after first click this css changes)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'text-regular')]")))
    addUserButton = driver.find_element(By.XPATH, "//button[contains(@class, 'text-regular')]")
    addUserButton.click()
    
    # add existing user button
    existingUser = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".stroke-gray-600")))
    existingUser.click()
    
    try:
        searchInput = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search")))
        searchInput.click()
    except StaleElementReferenceException:
        # Re-locate the element
        searchInput = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search")))
        searchInput.click()

    # Type into the search input
    searchInput.send_keys("Anessia@teztechnology.com")
    searchInput.click()
    # Wait for the element to be located
    checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'cursor-pointer') and contains(@class, 'rounded') and contains(@class, 'text-highlightColor') and contains(@class, 'focus:ring-highlightColor')]")))

    # Once located, interact with the element
    checkbox.click()

    # Locate and click the submit button
    submit = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Submit')]")))
    submit.click()

    

def combineUsers(salesPerson):
    df = data.getdf('standardUserList.csv')
    df.loc[len(df), 'User'] = salesPerson

    return df

    
#get standard user list and add the sales rep to the array
    #users = combineUsers(salesPerson)
    #log.info(f"users list: {users}")
    #----------start iteration here----------
    # for index, value in users.iterrows():
    # searchBar.send_keys(value['User'])
    
