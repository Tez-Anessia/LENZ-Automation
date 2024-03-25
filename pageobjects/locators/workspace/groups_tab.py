from selenium.webdriver.common.by import By

#This section contains the workspace group tab. This has several layers. the most basic layer will be the main page
#which contains the group package, then the group itself which is the expanded group package
class GroupsElements:
    #-----------------General-----------------
    main_section = (By.XPATH, "//div[contains(@class,'grid space-y')]")
    add_new_btn = (By.XPATH, "//div[contains(@class, 'flex sm:items-center')]/descendant::button[contains(@class,'group inline-flex items-center justify-center')]")

    #-----------------Group Package-----------------
    # General paths to the elements. Since the components duplicate, it will need to be called in the specified group path
    # This element is the general path to find all of the group sections   
    group_package = (By.XPATH, "//div[contains(@class,'flex items-center justify-between py-4 px-6 gap-10')]")
    package_name_input = (By.XPATH, "//input[contains(@name,'workspace-name') and contains (@class, 'w-full pr-4')]") 
    #Settings menu button and options    
    settings_btn = (By.XPATH, "//button[contains(@id, 'headlessui-menu-button') and contains(@class, 'max-w-xs')]")
    # These options only show once settings button has been pressed
    settings_manage = (By.XPATH, "//button[normalize-space()='Manage users']")
    settings_add_page = (By.XPATH, "//button[normalize-space()='Add page']")
    settings_clone = (By.XPATH, "//button[normalize-space()='Clone group']")
    settings_add_icon = (By.XPATH, "//button[normalize-space()='Add icon']")
    settings_delete = (By.XPATH, "//button[normalize-space()='Delete group']")
    #-----------------Group Package: Expanded Section-----------------
    expand_button = (By.XPATH, "//button[contains(@class, '!shadow-non')]") #same expanded and not expanded

    #-----------------Group Package: XPATHS-----------------
    # Add the exact group Path then exact group options then either settings buttons or expand button path to get the exact line
    group_name_XPATH = "//input[@value='{groupName}'"
    group_options_XPATH = "/ancestor::div[contains(@class, 'relative bg-white')]/descendant::"

    #-----------------Group Elements-----------------
    # This portion only shows once expand button is clicked
    group_pages_components = (By.XPATH, "//div[contains(@class,'relative max-h-[200000px] py-3 sm:py-4 px-3 sm:px-6 border-t border-slate-200')]")
    add_page_btn = (By.XPATH, "//div[2]/div[2]/div/div[2]/button/div")
    # These show after pressing the add page button
    page_dropdown = (By.XPATH, "//div[@class='flex pr-4 min-w-[200px]']")
    page_options_XPATH = "//option[. = '{pageName}']"
    # These buttons have a disabled status
    update_group_btn = (By.XPATH, "//button[contains(@class, 'sm:w-auto') and contains(., 'Update')]")
    undo_changes_btn = (By.XPATH, "//button[contains(@class, 'sm:w-auto') and contains(., 'Undo changes')]")

class DialogElements:
    #-----------------General-----------------
    ws_dialog_whitespace = (By.XPATH, "//div[contains(@class, 'flex justify-between py-4 px-4')]")
    group_name_input = (By.XPATH, "//input[@name='name']")
    assign_users_search = (By.XPATH, "//input[@name='search']")
    assign_users_selections = (By.XPATH, "(//div[contains(@class,'cursor-pointer w-full truncate')])")
    add_page_btn =(By.XPATH, "//div[contains(text(),'Add Page')]")
    page_dropdown = (By.XPATH, "//div[@data-headlessui-state='open']//div//div//div//div//div//div//div[@data-rbd-droppable-id='droppable']//div//form[@action='#']//div//div//div//div//select[@name='page_id']")
    last_page_dropdown = (By.XPATH, "(//div[@data-headlessui-state='open']//div//div//div//div//div//div//div[@data-rbd-droppable-id='droppable']//div//form[@action='#']//div//div//div//div//select[@name='page_id'])[last()]")
    save_btn = (By.XPATH, "//button[normalize-space()='Save']")

    #-----------------XPATHS-----------------
    # This xpath will bring the name in view once searched to be clicked 
    users_in_list_XPATH ="//div[contains(@class, 'flex relative items-center justify-center') and contains(.,'{userName}')]"
    specific_checkbox_XPATH= "//div[contains(text(),'{userName'}')]/ancestor::div[contains(@class, 'cursor-pointer')]/input[@type='checkbox']"
    checkbox_XPATH = "//input[@type='checkbox']"