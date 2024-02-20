from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#----start of script run ---------------------------------
driver.get("https://admin.tez.io/login")
driver.find_element(By.NAME, "contact-email").send_keys(userName)
driver.find_element(By.NAME, "password").send_keys(passWord)
driver.find_element(By.CSS_SELECTOR, ".group").click()