import sys
sys.path.append('.')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.locators import workspaces_locators as locator
import config.logger

log = config.logger.setUp()

class wseditor:

    def __init__(self, driver):
        self.driver = driver