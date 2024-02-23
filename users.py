import logger
import getdata as data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    addUserButton = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".-right-2")))
    addUserButton.click()
    # add existing user button
    existingUser = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".hover\\3A cursor-pointer")))
    existingUser.click()
    
    #search
    time.sleep(10)
    searchInput = driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search").send_keys("Anessia@teztechnology.com")
    
    
    #get standard user list and add the sales rep to the array
    #users = combineUsers(salesPerson)
    #log.info(f"users list: {users}")
    #----------start iteration here----------
    # for index, value in users.iterrows():
    # searchBar.send_keys(value['User'])
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type=\'checkbox\'])[2]")))
    driver.find_element(By.XPATH, "(//input[@type=\'checkbox\'])[2]").click()
    
    # searchBar.clear()

    #click in whitespace to get to the submit button
    driver.find_element(By.CSS_SELECTOR, "#headlessui-dialog-title-38 > .text-gray-400").click()
    submit = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,\'Submit\')]")))
    submit.click()
    

def combineUsers(salesPerson):
    df = data.getdf('standardUserList.csv')
    df.loc[len(df), 'User'] = salesPerson

    return df

    

