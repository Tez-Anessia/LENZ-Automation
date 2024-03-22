from selenium.webdriver.common.by import By

class PagesElements:
    search_input = (By.XPATH, "//input[@id='search']")
    addpg_btn = (By.XPATH, "//button[contains(@class,'h-full inline-flex')]")
    
    #-----------------Table-----------------
    name_column_elements = (By.XPATH, "//tbody/tr/td[1]") #all elements in the name column
    all_menu_btn = "//div[@class='py-3 px-1 rounded-full hover:bg-gray-100 transition-colors duration-100 flex items-center justify-center']"
    open_menu_btn = (By.XPATH, "//button[@aria-expanded='true']")
    pages_previewPage = (By.XPATH, "//button[normalize-space()='Preview']") #this will only be after you click the menu button
    
    #-----------------Table: XPATHS-----------------
    find_page_XPATH = "//div[contains(text(),'{pageName}')" #General path to find if the element is on the page
    # To click on the menu button of a specific page, you need the absolute path of the page and menu
    # Full XPATH = specific_page_XPATH + specific_menu_btn_XPATH
    specific_page_XPATH = "//table/tbody/tr//td[.//div[contains(.,'{pageName}')]]"
    specific_menu_btn_XPATH = "/following-sibling::td[.//button[contains(@id, 'headlessui-menu')]][1]//button[contains(@id, 'headlessui-menu')]"