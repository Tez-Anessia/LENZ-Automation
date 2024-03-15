from selenium.webdriver.common.by import By
'''
These elements here are the elements for a workspace profile
'''
class wsprofileElements:
#Workspace name 
    ws_name_input = (By.XPATH, "//input[@name='workspace-name']") #is autocomplete
#Tabs
    pages_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Pages']")
    users_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Users']")
    groups_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Groups']")
    editor_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Editor Permissions']")
    layout_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Layout & Styles']")
    settings_tab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Settings']")
#Common Elements
#---this appears when nothing is assigned to the workspace
    no_data_element = (By.XPATH, "//p[normalize-space()='No Data Found']") 

class wspagesElements:
    search_input = (By.XPATH, "//input[@id='search']")
    addpg_btn = (By.XPATH, "//button[contains(@class,'h-full inline-flex')]")
    
#Table
    name_column_elements = (By.XPATH, "//tbody/tr/td[1]") #all elements in the name column
    all_menu_btn = "//div[@class='py-3 px-1 rounded-full hover:bg-gray-100 transition-colors duration-100 flex items-center justify-center']"
    open_menu_btn = (By.XPATH, "//button[@aria-expanded='true']")
    pages_previewPage = (By.XPATH, "//button[normalize-space()='Preview']") #this will only be after you click the menu button
#-XPATHS
#---general XPATH you can use to find if the element is on the page
    find_page_XPATH = "//div[contains(text(),'{pageName}')"
#---to click on the menu button of a specific page, you need the absolute path of the page and menu
#---full XPATH = specific_page_XPATH + specific_menu_btn_XPATH
    specific_page_XPATH = "//table/tbody/tr//td[.//div[contains(.,'{pageName}')]]"
    specific_menu_btn_XPATH = "/following-sibling::td[.//button[contains(@id, 'headlessui-menu')]][1]//button[contains(@id, 'headlessui-menu')]"
    
class wsuserElements:
#General
    search_input = (By.XPATH, "//input[@id='search']")
#---once you check the box for a user, these icons are clickable
    reinviteSelected = (By.XPATH, "//button[contains(@data-tooltip-id, 'Resend welcome invites')]")
    deactivateSelected = (By.XPATH, "//button[contains(@data-tooltip-id, 'Deactivate users')]")
    deleteSelected = (By.XPATH, "//button[contains(@data-tooltip-id, 'Delete users')]")
    add_user_btn = (By.XPATH, "//button[contains(@class,'sm:w-auto')]")
#Table
#-General paths to table columns
    checkbox = (By.XPATH, "(//input[@type='checkbox'])") #they differ by index starts at 2, header is 1 (//input[@type='checkbox'])[2]
    name_column_elements = (By.XPATH, "//table/tbody/tr//td[.//div[@class='flex items-center']]")
    email_Column_elements = (By.XPATH, "//td[@class='hidden whitespace-nowrap px-3 py-3 text-sm text-gray-500 sm:table-cell']")
    status_column_elements = (By.XPATH, "//button[contains(@class,'bg-green')]")
#---All names in the name column
    all_usernames = (By.XPATH, "//table/tbody/tr//td[.//div[@class='flex items-center']]//div[@class='flex items-center gap-x-2 font-medium text-gray-900']")
    user_creation_info = (By.XPATH, "//table/tbody/tr//td[.//div[@class='flex items-center']]//div[@class='text-gray-500']")
#---This is the general path, and selects the first found. to use this path search for the user specifically then use this locator
    user_Menu_btn = (By.XPATH, "//button[contains(@class, 'max-w-xs bg-white')]")
    menu_view_profile = (By.XPATH, "//button[normalize-space()='View Profile']")
    menu_workspaces = (By.XPATH, "//button[normalize-space()='Workspaces']")
    menu_data_access = (By.XPATH, "//button[normalize-space()='Data Access']")
    menu_remove_access = (By.XPATH, "//button[normalize-space()='Remove Access']")
#Export Options
    export_users = (By.XPATH, "//div[contains(text(),'Export')]")
    export_format = (By.XPATH, "//button[contains(@aria-haspopup,'listbox') and //span[normalize-space()='.xls']]")
    xls_option = (By.XPATH, "//li[(@role='option')][1]")
    csv_option = (By.XPATH, "//li[(@role='option')][2]")
#-XPATHS
#---combine with //a[normalize-space()='{user}'] to find the specific user
    userName_XPath = "//table/tbody/tr//td[.//div[@class='flex items-center']]//div[@class='flex items-center gap-x-2 font-medium text-gray-900']"

class wsuserDialog:
#General
    dialog_whitespace = (By.XPATH, "//div[@class='flex justify-between py-4 px-4']")
#Create User Section
    name__input = (By.XPATH, "//input[contains(@autocomplete,'new-fname')]") #this should be a full name
    email_input = (By.XPATH, "//input[@name='email']")
#---there needs to be page groups on the workspace for anything to populate here
    assign_groups_search = (By.XPATH, "//div[@class='relative rounded-md shadow-sm w-full flex']//input[@id='search']") #autocomplete is off here
#---this just asserts the dropdown populated, this is the whole container, not the options 
    dropdown_hidden = (By.XPATH, "//div[contains(@class,'absolute hidden')]")
    dropdown_viewable = (By.XPATH, "//div[contains(@class,'absolute flex flex-col')]")
    dropdown_elements = (By.XPATH, "//div[contains(@class,'absolute flex flex-col')]/descendant::div[contains(@class,'cursor-pointer w-full truncate')]")
#---this section is the bubbles that populate when you select groups and click out of it
    added_groups_container = (By.XPATH, "//div[@class='w-full overflow-y-scroll']")
    all_bubble_elements = (By.XPATH, "//div[@class='w-full overflow-y-scroll']/descendant::div[contains(@class, 'border border-highlightColor text-highlightColor')]")
    added_group_text_XPATH = "//p[normalize-space()='{groupname}']"
#-Advance Features
    advance_features_btn = (By.XPATH, "//p[contains(@class,'select-none')]")
    af_section_visible = (By.XPATH, "//div[contains(@class,'-mt-')]//*[@class='h-5']")
    af_section_hidden = (By.XPATH, "//div[contains(@class,'-mt-')]//*[@class='h-5 -rotate-90']")
    af_section_container = (By.XPATH, "//div[contains(@class,'overflow-hidden transition-all duration')]//*[@class='w-full flex flex-col']")
    send_invite_btn = (By.XPATH, "//input[@id='send-email']")
    manual_pass_btn = (By.XPATH, "manual")
#Add Existing Users
    add_existing_btn = (By.XPATH, "//div[contains(text(),'Add an existing user')]")
    assign_search_input = (By.XPATH, "//input[@placeholder='Search']")
#---General path to all elements in the dropdown
    existing_dropdown_elements = (By.XPATH, "//div[contains(@class,'cursor-pointer w-full truncate flex items-center')]")
    exsiting_user_whitespace = (By.XPATH, "//div[contains(@class, 'flex justify-between py-4 px-4')]")
#---these work in both dialog boxes
    cancel_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
    submit_btn = (By.XPATH, "//button[normalize-space()='Submit']")
#-XPATHS
    existing_dropdown_text = "//div[contains(@class,'flex relative items-center')]//div[.='{user}']"

class wsgroupsElements:
#General
    main_container = (By.XPATH, "//div[contains(@class,'grid space-y')]")
    add_new_btn = (By.XPATH, "//div[contains(@class, 'flex sm:items-center')]/descendant::button[contains(@class,'group inline-flex items-center justify-center')]")
#Group elements
    group_elements_section = (By.XPATH, "//div[contains(@class,'space-y-4 pl-10')]")
#-General paths to the elements. Since the components duplicate, it will need to be called in the specified group path
 #---This element is the general path to find all of the group sections   
    group_components = (By.XPATH, "//div[contains(@class,'flex items-center justify-between py-4 px-6 gap-10')]")
    group_name_input = (By.XPATH, "//input[contains(@name,'workspace-name')]") #specific name = //input[@value='{groupName}']
#---Settings menu button and options    
    settings_btn = (By.XPATH, "//button[contains(@id, 'headlessui-menu-button') and contains(@class, 'max-w-xs')]")
#---These options only show once settings button has been pressed
    settings_manage_users = (By.XPATH, "//button[normalize-space()='Manage users']")
    settings_add_page = (By.XPATH, "//button[normalize-space()='Add page']")
    settings_clone_group = (By.XPATH, "//button[normalize-space()='Clone group']")
    settings_add_icon = (By.XPATH, "//button[normalize-space()='Add icon']")
    settings_delete_group = (By.XPATH, "//button[normalize-space()='Delete group']")
#-Expanded Section (still general paths)
    expand_button = (By.XPATH, "//button[contains(@class, '!shadow-non')]") #same expanded and not expanded
#---This portion only shows once expand button is clicked
    expanded_section = (By.XPATH,"//div[@class='bg-white rounded-md flex justify-center items-center gap-x-4 w-full h-[120px]']")
    group_pages_components = (By.XPATH, "//div[contains(@class,'relative max-h-[200000px] py-3 sm:py-4 px-3 sm:px-6 border-t border-slate-200')]")
    
    add_page_btn = (By.XPATH, "//button[contains(.,'Add page')]")
#---These buttons have a disabled status
    update_group_btn = (By.XPATH, "//button[contains(@class, 'sm:w-auto') and contains(., 'Update')]")
    undo_changes_btn = (By.XPATH, "//button[contains(@class, 'sm:w-auto') and contains(., 'Undo changes')]")


class wsgroupsDialog:
    pass
class wslayoutElements:
    pass
class wsSettingsElements:
    addWSFilterBtn = (By.XPATH, "//div[2]/div[(@class='w-full justify-between flex items-center gap-4')]/button")
    filterColumnNameInput = (By.XPATH, "//input[contains(@name,'column-name')]")
    filterOperatordropdown = (By.XPATH, "//div[@class='w-full h-full flex justify-between items-center']//button[contains(@class,'h-10 relative')]")
    equaltoOption = (By.XPATH, "(//li[@role='option'])[1]")
    allOptions = (By.XPATH, "(//li[@role='option'])")
    textValueInput = (By.XPATH, "//input[@name='column-value']")
    
    deleteWorkspace = (By.XPATH, "//button[@class='group inline-flex items-center justify-center transition-all duration-200 rounded-md border px-4 py-2 text-regular font-medium focus:ring-2 focus:border-highlightColor bg-white text-highlightColor border-[1px] border-highlightColor hover:shadow-sm  sm:w-auto h-12 !text-red-300 !border-red-300']")
