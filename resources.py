from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def addElementWait(driver, element):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((element)))