import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = logger.setUp()

def adminLogin(driver, userName, passW):
    #--------Actions--------------------------
    driver.get("https://admin.tez.io/login")
    driver.find_element(By.NAME, "contact-email").send_keys(userName)
    driver.find_element(By.NAME, "password").send_keys(passW)
    driver.find_element(By.CSS_SELECTOR, ".group").click()

    #--------Validations-----------------------
    url = "https://admin.tez.io/workspaces"
    wait = WebDriverWait(driver, 5)  # Adjust the timeout as needed
    wait.until(EC.url_to_be(url))
    log.info("login success")
