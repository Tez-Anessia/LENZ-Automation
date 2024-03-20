from selenium.webdriver.common.by import By

'''
These locators currently only have global pages mapped. If All Pages has a need in the future it will be added here
'''
class pagesElements:
    #-----------------General-----------------
    all_pages_tab = (By.XPATH, "//span[.='All pages']")
    global_pages_tab = (By.XPATH, "//span[.='Global pages']")

    #-----------------Global Pages-----------------
    search_input = (By.XPATH, "//input[@id='search']")
    add_page = (By.XPATH, "//div[@class='relative z-50 inline-block text-left']//button[contains(@id, 'headlessui-menu-button')]")
    #while this is in the commons locator, adding here to use this as the page load wait element
    pagination_element = (By.XPATH, "//button[@aria-haspopup='listbox']")
    #This will get all menu buttons
    page_menu_buttons = (By.XPATH, "//button[@aria-haspopup='menu'][contains(@class, 'max-w-xs')]")
    #Note: there needs to be a space after the text in the options
    menu_option_edit = (By.XPATH, "//button[.='Edit ']")
    menu_option_preview = (By.XPATH, "//button[.='Preview ']")
    menu_option_delete = (By.XPATH, "//button[.='Delete ']")

    #-----------------XPATHS-----------------
    #Full path is name_column_XPATH + page_menu_XPATH
    name_column_XPATH = "//div[text()='{pageName}']"
    page_menu_XPATH = "/ancestor::tr[@class='relative']/descendant::button[contains(@class, 'max-w-xs')]"

    #-----------------Edit Page Dialog Box-----------------
    dialog_box = (By.XPATH, "//div[@role='dialog']/div/div/div[@data-headlessui-state='open']")
    dialog_whitespace = (By.XPATH, "//div[@class='flex justify-between py-4 px-4']")
    dialog_search_input = (By.XPATH, "//input[@placeholder='Search']")
    dialog_search_dropdown = (By.XPATH,"//div[@class='cursor-pointer w-full truncate flex items-center px-4 py-2 gap-x-3 border-white hover:bg-gray-100']")
    dialog_submit_btn = (By.XPATH, "//button[normalize-space()='Submit']")
    
    #Add this to the end of the dialog search dropdown to find the element with the specific customer
    #//div to the beginning will find it in the search dropdown
    #//p in the beginning will find it in the exisiting section(purple bubbles)
    specific_dropdown_XPATH = "[contains(text(),'{companyName}')]"
    specific_bubble_XPATH = "//p[contains(text(),'{companyName}')]"
    specific_checkbox_XPATH = "//div[.='{companyName}']//input[@type='checkbox']"