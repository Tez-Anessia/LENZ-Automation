
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginscreen(self):
    # Test name: Log in screen
    # Step # | name | target | value
    # 1 | open | https://admin.tez.io/login | 
    self.driver.get("https://admin.tez.io/login")
    # 2 | setWindowSize | 1534x911 | 
    self.driver.set_window_size(1534, 911)
    # 3 | type | name=contact-email | anessia@teztechnology.com
    self.driver.find_element(By.NAME, "contact-email").send_keys("anessia@teztechnology.com")
    # 4 | type | name=password | Nitrogen14!
    self.driver.find_element(By.NAME, "password").send_keys("Nitrogen14!")
    # 5 | click | name=contact-email | 
    self.driver.find_element(By.NAME, "contact-email").click()
    # 6 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 7 | click | css=.group | 
    self.driver.find_element(By.CSS_SELECTOR, ".group").click()
  
  def test_createworkspace(self):
    # Test name: Create workspace
    # Step # | name | target | value
    # 1 | open | https://admin.tez.io/workspaces | 
    self.driver.get("https://admin.tez.io/workspaces")
    # 2 | setWindowSize | 1534x911 | 
    self.driver.set_window_size(1534, 911)
    # 3 | mouseOver | css=.-right-2 | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".-right-2")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | click | css=.-right-2 | 
    self.driver.find_element(By.CSS_SELECTOR, ".-right-2").click()
    # 5 | mouseOut | css=.-right-2 | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 6 | click | name=name | 
    self.driver.find_element(By.NAME, "name").click()
    # 7 | type | name=name | Automation Workspace Test 3
    self.driver.find_element(By.NAME, "name").send_keys("Automation Workspace Test 3")
    # 8 | click | css=.inline-flex:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".inline-flex:nth-child(2)").click()
  
  def test_addgroups(self):
    # Test name: add groups
    # Step # | name | target | value
    # 1 | open | https://admin.tez.io/workspaces/65ce778558521dc38ff6a1fd?tab=Groups | 
    self.driver.get("https://admin.tez.io/workspaces/65ce778558521dc38ff6a1fd?tab=Groups")
    # 2 | setWindowSize | 1534x911 | 
    self.driver.set_window_size(1534, 911)
    # 3 | click | css=.border-highlightColor > .block | 
    self.driver.find_element(By.CSS_SELECTOR, ".border-highlightColor > .block").click()
    # 4 | click | css=.border-highlightColor > .block | 
    # Groups Tab
    self.driver.find_element(By.CSS_SELECTOR, ".border-highlightColor > .block").click()
    # 5 | click | css=.-right-2 | 
    # add groups button
    self.driver.find_element(By.CSS_SELECTOR, ".-right-2").click()
    # 6 | mouseOver | css=.-right-2 | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".-right-2")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 7 | mouseOut | css=.-right-2 | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 8 | click | name=name | 
    self.driver.find_element(By.NAME, "name").click()
  
  def test_addusers(self):
    # Test name: add users
    # Step # | name | target | value
    # 1 | open | https://admin.tez.io/workspaces/65ce778558521dc38ff6a1fd | 
    self.driver.get("https://admin.tez.io/workspaces/65ce778558521dc38ff6a1fd")
    # 2 | setWindowSize | 1534x911 | 
    self.driver.set_window_size(1534, 911)
    # 3 | click | css=.border-transparent:nth-child(2) path | 
    self.driver.find_element(By.CSS_SELECTOR, ".border-transparent:nth-child(2) path").click()
    # 4 | click | css=.text-highlightColor > path | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-highlightColor > path").click()
    # 5 | click | css=.text-regular | 
    # add users button
    self.driver.find_element(By.CSS_SELECTOR, ".text-regular").click()
    # 6 | click | css=.hover\3A cursor-pointer | 
    # add existing user button
    self.driver.find_element(By.CSS_SELECTOR, ".hover\\3A cursor-pointer").click()
    # 7 | click | css=.relative:nth-child(2) > .relative > #search | 
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search").click()
    # 8 | type | css=.relative:nth-child(2) > .relative > #search | anes
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search").send_keys("anes")
    # 9 | click | css=.focus\3Aring-highlightColor | 
    self.driver.find_element(By.CSS_SELECTOR, ".focus\\3Aring-highlightColor").click()
    # 10 | mouseOver | css=.focus\3Aring-highlightColor | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".focus\\3Aring-highlightColor")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 11 | mouseOut | css=.focus\3Aring-highlightColor | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 12 | click | css=.relative:nth-child(2) > .relative > #search | 
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search").click()
    # 13 | click | css=.relative:nth-child(2) > .relative > #search | 
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search").click()
    # 14 | doubleClick | css=.relative:nth-child(2) > .relative > #search | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 15 | type | css=.relative:nth-child(2) > .relative > #search | divi
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search").send_keys("divi")
    # 16 | sendKeys | css=.relative:nth-child(2) > .relative > #search | ${KEY_ENTER}
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .relative > #search").send_keys(Keys.ENTER)
    # 17 | click | css=.focus\3Aring-highlightColor | 
    self.driver.find_element(By.CSS_SELECTOR, ".focus\\3Aring-highlightColor").click()
    # 18 | mouseOver | css=.focus\3Aring-highlightColor | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".focus\\3Aring-highlightColor")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 19 | mouseOut | css=.focus\3Aring-highlightColor | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 20 | click | css=.border-transparent:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".border-transparent:nth-child(2)").click()
    # 21 | mouseOver | css=.rounded-tl-md | 
    # submit
    element = self.driver.find_element(By.CSS_SELECTOR, ".rounded-tl-md")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 22 | click | css=.relative:nth-child(1) > .pl-4 | 
    # validating user
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(1) > .pl-4").click()
    # 23 | click | css=.relative:nth-child(2) > .pl-4 > .flex | 
    self.driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(2) > .pl-4 > .flex").click()
  
  def test_searchworkspace(self):
    # Test name: search workspace
    # Step # | name | target | value
    # 1 | open | https://admin.tez.io/workspaces | 
    self.driver.get("https://admin.tez.io/workspaces")
    # 2 | setWindowSize | 1534x911 | 
    self.driver.set_window_size(1534, 911)
    # 3 | click | id=search | 
    self.driver.find_element(By.ID, "search").click()
    # 4 | type | id=search | Workspace
    self.driver.find_element(By.ID, "search").send_keys("Workspace")
    # 5 | sendKeys | id=search | ${KEY_ENTER}
    self.driver.find_element(By.ID, "search").send_keys(Keys.ENTER)
  
