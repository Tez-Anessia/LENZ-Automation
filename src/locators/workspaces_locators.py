from selenium.webdriver.common.by import By

'''
nameColumn_elements - gets all elements in the name column
last_WS = gets the last visible element in the name column (used for waits)

Dynamic Paths:
- get workspace url: f"//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]/div/a[contains(@href,'/workspaces')]"
- find workspace in table(locate only): f"//div[contains(text(),'{companyName}')]"  
'''
class workspacesElements:
    search_input = (By.XPATH, "//input[@id='search']")
    #Pagination element used for waiting strategy, any functional use will be with common pom
    pagination_element = (By.XPATH, "//button[contains(@class, 'bg-white relative')]")
    #-----------------Table-----------------
    nameColumn_elements = (By.XPATH, "//div[@class='w-full flex gap-x-3 items-center relative']")
    last_visible_name = (By.XPATH, "(//div[@class='w-full flex gap-x-3 items-center relative'])[last()]")
    #These point to all elements in the column, add an index to tr to get a specific row
    pagesColumn_elements = (By.XPATH, "//tbody/tr/td[2]")
    groupsColumn_elements = (By.XPATH, "//tbody/tr/td[3]")
    usersColumn_elements = (By.XPATH, "//tbody/tr/td[4]")

    #-----------------Table: XPATHS-----------------
    table_row_XPATH = "//tbody/tr/td" #tr = row, td = column, index position. td[4] - users column
    #Add these to the end of the workspace URL XPATH: "//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]"
    workspace_pages_XPATH = "/following-sibling::td[1]/a[contains(@href,'tab=Pages')]"
    workspace_groups_XPATH = "/following-sibling::td[2]/a[contains(@href,'tab=Groups')]"
    workspace_users_XPATH = "/following-sibling::td[3]/a[contains(@href,'tab=Users')]"
    
    #-----------------Add Workspace-----------------
    add_ws_btn = (By.XPATH, "//button[@data-tooltip-id='Add a workspace-custom-link']")
    #Dialog box when pressing addworkspace button
    dialog_wsName_input = (By.XPATH, "//input[@name='name']")
    dialog_cancel_Btn = (By.XPATH, "//button[normalize-space()='Cancel']")
    dialog_save_Btn = (By.XPATH, "//button[normalize-space()='Save']")
    dialog_whiteSpace = (By.XPATH, "//div[contains(@class,'flex justify-between py-4 px-4')]")
