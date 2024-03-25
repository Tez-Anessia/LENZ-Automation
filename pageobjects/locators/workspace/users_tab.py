from selenium.webdriver.common.by import By

class UserElements:
    #-----------------General-----------------
    search_input = (By.XPATH, "//input[@id='search']")
    # Pagination with start with User Records once all users have populated on the page
    pagination_indicator = (By.XPATH, "//div[starts-with(text(),'User record')]")
    
    # Once you check the box for a user, these icons are clickable
    reinvite = (By.XPATH, "//button[contains(@data-tooltip-id, 'Resend welcome invites')]")
    deactivate = (By.XPATH, "//button[contains(@data-tooltip-id, 'Deactivate users')]")
    delete = (By.XPATH, "//button[contains(@data-tooltip-id, 'Delete users')]")
    add_user_btn = (By.XPATH, "//button[contains(@class,'sm:w-auto')]")

    #-----------------Table-----------------
    # General elements to table columns
    checkbox = (By.XPATH, "(//input[@type='checkbox'])") #they differ by index starts at 2, header is 1 (//input[@type='checkbox'])[2]
    name_column_elements = (By.XPATH, "//table/tbody/tr//td[.//div[@class='flex items-center']]")
    email_column_elements = (By.XPATH, "//td[@class='hidden whitespace-nowrap px-3 py-3 text-sm text-gray-500 sm:table-cell']")
    status_column_elements = (By.XPATH, "//button[contains(@class,'bg-green')]")
    # All names in the name column
    all_usernames = (By.XPATH, "//table/tbody/tr//td[.//div[@class='flex items-center']]//div[@class='flex items-center gap-x-2 font-medium text-gray-900']")
    user_creation_info = (By.XPATH, "//table/tbody/tr//td[.//div[@class='flex items-center']]//div[@class='text-gray-500']")
    # This is the general path, and selects the first found. to use this path search for the user specifically then use this locator
    user_menu_btn = (By.XPATH, "//button[contains(@class, 'max-w-xs bg-white')]")
    menu_view_profile = (By.XPATH, "//button[normalize-space()='View Profile']")
    menu_workspaces = (By.XPATH, "//button[normalize-space()='Workspaces']")
    menu_data_access = (By.XPATH, "//button[normalize-space()='Data Access']")
    menu_remove_access = (By.XPATH, "//button[normalize-space()='Remove Access']")

    #-----------------Export Options-----------------
    export_users = (By.XPATH, "//div[contains(text(),'Export')]")
    export_format = (By.XPATH, "//button[contains(@aria-haspopup,'listbox') and //span[normalize-space()='.xls']]")
    xls_option = (By.XPATH, "//li[(@role='option')][1]")
    csv_option = (By.XPATH, "//li[(@role='option')][2]")
    
    #-----------------XPATHS-----------------
    # Combine with //a[normalize-space()='{user}'] to find the specific user
    userName_XPATH = "//table/tbody/tr//td[.//div[@class='flex items-center']]//div[@class='flex items-center gap-x-2 font-medium text-gray-900']"

class DialogElements:
    #-----------------General-----------------
    dialog_whitespace = (By.XPATH, "//div[@class='flex justify-between py-4 px-4']")

    #-----------------Create User Section-----------------
    name__input = (By.XPATH, "//input[contains(@autocomplete,'new-fname')]") #this should be a full name
    email_input = (By.XPATH, "//input[@name='email']")
    # There needs to be page groups on the workspace for anything to populate here
    assign_groups_search = (By.XPATH, "//div[@class='relative rounded-md shadow-sm w-full flex']//input[@id='search']") #autocomplete is off here
    # This just asserts the dropdown populated, this is the whole container, not the options 
    dropdown_hidden = (By.XPATH, "//div[contains(@class,'absolute hidden')]")
    dropdown_viewable = (By.XPATH, "//div[contains(@class,'absolute flex flex-col')]")
    dropdown_elements = (By.XPATH, "//div[contains(@class,'absolute flex flex-col')]/descendant::div[contains(@class,'cursor-pointer w-full truncate')]")
    # This section is the bubbles that populate when you select groups and click out of it
    added_groups_container = (By.XPATH, "//div[@class='w-full overflow-y-scroll']")
    all_bubble_elements = (By.XPATH, "//div[@class='w-full overflow-y-scroll']/descendant::div[contains(@class, 'border border-highlightColor text-highlightColor')]")
    added_group_text_XPATH = "//p[normalize-space()='{groupname}']"
    
    #-----------------Create Users: Advance Features-----------------
    advance_features_btn = (By.XPATH, "//p[contains(@class,'select-none')]")
    af_section_visible = (By.XPATH, "//div[contains(@class,'-mt-')]//*[@class='h-5']")
    af_section_hidden = (By.XPATH, "//div[contains(@class,'-mt-')]//*[@class='h-5 -rotate-90']")
    af_section_container = (By.XPATH, "//div[contains(@class,'overflow-hidden transition-all duration')]//*[@class='w-full flex flex-col']")
    send_invite_btn = (By.XPATH, "//input[@id='send-email']")
    manual_pass_btn = (By.XPATH, "manual")

    #-----------------Add Existing Users-----------------
    add_existing_btn = (By.XPATH, "//div[contains(text(),'Add an existing user')]")
    assign_search_input = (By.XPATH, "//input[@placeholder='Search']")
    # General path to all elements in the dropdown
    existing_dropdown_elements = (By.XPATH, "//div[contains(@class,'cursor-pointer w-full truncate flex items-center')]")
    exsiting_user_whitespace = (By.XPATH, "//div[contains(@class, 'flex justify-between py-4 px-4')]")
    # These work in both dialog boxes
    cancel_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
    submit_btn = (By.XPATH, "//button[normalize-space()='Submit']")
    
    #-----------------Add Existing: XPATHS-----------------
    existing_dropdown_text = "//div[contains(@class,'flex relative items-center')]//div[.='{user}']"