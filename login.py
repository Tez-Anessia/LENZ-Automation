from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



#------variables for modifiability-----------------
userName = "anessia@teztechnology.com"
passW = "Nitrogen14!"

#----Driver setup------
driver = webdriver.Chrome()
driver.implicitly_wait(0.70)

#----start of script run ---------------------------------
driver.get("https://admin.tez.io/login")

driver.find_element(By.NAME, "contact-email").send_keys(userName)
driver.find_element(By.NAME, "password").send_keys(passW)
driver.find_element(By.CSS_SELECTOR, ".group").click()

#--------validate log in success--------------------------
url = "https://admin.tez.io/workspaces"
wait = WebDriverWait(driver, 5)  # Adjust the timeout as needed
wait.until(EC.url_to_be(url))


driver.quit()