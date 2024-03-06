from typing import Self
import logger
from login import adminLogin
import getdata as data
from page.login_page import LoginPage
from page.workspace_page import WSPage
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


#-----------------variables----------------
userName = 'qa@email.com'
passW = "T3Z@dm!nP@$$24^"
customerList = "testSheet.csv"
#-----------------Set-Up-----------------
driver = webdriver.Chrome()
driver.implicitly_wait(0.50)
driver.maximize_window()
actions = ActionChains(driver)

login = LoginPage(driver)
login.open_page("https://admin.tez.io/login")
login.adminLogin(userName, passW)

ws = WSPage(driver)
ws.createWorkspace("Anessia Test")
ws.findWorkspace("Anessia Test")
time.sleep(4)

#//table/tbody/tr/td[.//div[contains(text(),'A Test Customer 1')]]/div/a[contains(@href,'/workspaces')]
#THIS GETS THE URL INSTEAD
    def selectWorkspace(self, customerName):
        ws = self.driver.find_element(By.XPATH, "//table/tbody/tr/td[.//div[contains(text(),'"+ customerName +"')]]/div/a[contains(@href,'/workspaces')]")
        url = ws.get_attribute('href')
        print(url)
        ws.click()
        