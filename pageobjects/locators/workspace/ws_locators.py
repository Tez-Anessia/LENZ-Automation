from selenium.webdriver.common.by import By
'''
These elements here are the elements for a workspace profile
'''
class WorkspaceProfile:
    #-----------------Workspace Name-----------------
    ws_name_input = (By.XPATH, "//input[@name='workspace-name']") #is autocomplete

    #-----------------Tabs-----------------
    pages_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Pages']")
    users_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Users']")
    groups_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Groups']")
    editor_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Editor Permissions']")
    layout_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Layout & Styles']")
    settings_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Settings']")

    #-----------------Common Elements-----------------
    #This appears when nothing is assigned to the workspace
    no_data_element = (By.XPATH, "//p[normalize-space()='No Data Found']") 
    
class wslayoutElements:
    pass
