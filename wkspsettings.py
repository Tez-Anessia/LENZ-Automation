import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = logger.setUp()

def setWSFilter(driver, companyName):
    #----page and filter-----
    driver.find_element(By.XPATH, "//span[contains(.,\'Settings\')]").click()
    driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .w-full > .group .absolute").click()

    #----column name field----
    columnName = driver.find_element(By.NAME, "column-name")
    columnName.click()
    columnName.send_keys("corporation.name")

    #----logic dropdown----
    driver.find_element(By.CSS_SELECTOR, ".min-h-\\[17\\.5px\\]").click()
    #this selects the top element which is "=", any other will need to be listed xpath=//li[2]/span/div for second element etc
    driver.find_element(By.XPATH, "//span/div").click()

    #----txt value----
    driver.find_element(By.NAME, "column-value").click()
    driver.find_element(By.NAME, "column-value").send_keys(companyName)
    driver.find_element(By.NAME, "column-value").send_keys(Keys.ENTER)
