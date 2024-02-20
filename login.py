from selenium import webdriver
from selenium.webdriver.common.by import By



#------variables for modifiability-----------------
userName = "anessia@teztechnology.com"
passWord = "Nitrogen14!"

#----Driver setup------
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)

#----start of script run ---------------------------------
driver.get("https://admin.tez.io/login")
driver.find_element(By.NAME, "contact-email").send_keys("anessia@teztechnology.com")
driver.find_element(By.NAME, "password").send_keys("Nitrogen14!")
driver.find_element(By.CSS_SELECTOR, ".group").click()

driver.quit()