from selenium.webdriver.common.by import By

'''
nameColumn_elements - gets all elements in the name column
last_WS = gets the last visible element in the name column (used for waits)

Dynamic Paths:
- get workspace url: f"//table/tbody/tr/td[.//div[contains(text(),'{companyName}')]]/div/a[contains(@href,'/workspaces')]"
- find workspace in table(locate only): f"//div[contains(text(),'{companyName}')]"  
'''
class pageElements:
    search_input = (By.XPATH, "//input[@id='search']")
    
    #Table
    nameColumn_elements = (By.XPATH, "(//div[@class='w-full flex gap-x-3 items-center relative'])")
    last_WS = (By.XPATH, "(//div[@class='w-full flex gap-x-3 items-center relative'])[last()]")

    #Add Workspace
    addWorkspace = (By.XPATH, "//button[@data-tooltip-id='Add a workspace-custom-link']")
    #--Dialog box when pressing addworkspace button
    wsName_input = (By.XPATH, "//input[@name='name']")
    cancel_Btn = (By.XPATH, "//button[normalize-space()='Cancel']")
    save_Btn = (By.XPATH, "//button[normalize-space()='Save']")
    dialog_whiteSpace = (By.XPATH, "//div[contains(@class,'flex justify-between py-4 px-4')]")

'''
These elements here are the elements for a workspace profile
'''
class profileElements:
    workspaceName = (By.XPATH, "//input[@name='workspace-name']")
    pagesTab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Pages']")
    usersTab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Users']")
    groupsTab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Groups']")
    editorTab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Editor Permissions']")
    LayoutTab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Layout & Styles']")
    SettingsTab = (By.XPATH, "//span[@class='block whitespace-nowrap'][normalize-space()='Settings']")

class wspagesElements:
    pages_search = (By.XPATH, "//input[@id='search']")
    pages_addpgBtn = (By.XPATH, "(//button[contains(@class,'h-full inline-flex')])")
    
    """
    To get the menu button you need to combine paths:
        - pgPath = f"//table/tbody/tr//td[.//div[contains(.,'{companyName}')]]"
        - inlineButton = pgPath + "/following-sibling::td[.//button[contains(@id, 'headlessui-menu')]][1]//button[contains(@id, 'headlessui-menu')]"
    If you just want to search to see if the page has been added you can use this xpath: 
        - //div[contains(text(),'"+ pageName +"')]
    """
    pages_previewPage = (By.XPATH, "(//button[normalize-space()='Preview'])") #this will only be after you click the menu button
    pages_menuBtn = (By.XPATH, "//div[@class='py-3 px-1 rounded-full hover:bg-gray-100 transition-colors duration-100 flex items-center justify-center']")

class wsuserElements:
    #Table
    noDataFound = (By.XPATH, "//p[text()='No Data Found']") #when theres no users assigned
    #--paths to elements
    checkbox = (By.XPATH, "(//input[@type='checkbox'])") #they differ by index starts at 2, header is 1 (//input[@type='checkbox'])[2]
    
    nameColumn = (By.XPATH, "//table/tbody/tr//td[.//div[@class='flex items-center']]")
    #general to userNames in the table
    userName = (By.XPATH, "//table/tbody/tr//td[.//div[@class='flex items-center']]//div[@class='flex items-center gap-x-2 font-medium text-gray-900']")
    #combine with //a[normalize-space()='{user}'] to find the specific user
    userName_Path = "//table/tbody/tr//td[.//div[@class='flex items-center']]//div[@class='flex items-center gap-x-2 font-medium text-gray-900']"
    
    createdDate = (By.XPATH, "//table/tbody/tr//td[.//div[@class='flex items-center']]//div[@class='text-gray-500']")
    
    emailColumn = (By.XPATH, "(//td[@class='hidden whitespace-nowrap px-3 py-3 text-sm text-gray-500 sm:table-cell'])")
    statusButton = (By.XPATH, "(//button[contains(@class,'bg-green')])")

    search = (By.XPATH, "//input[@id='search']")

    # once you check the box for a user, these icons are clickable
    reinviteSelected = (By.XPATH, "//button[contains(@data-tooltip-id, 'Resend welcome invites')]")
    deactivateSelected = (By.XPATH, "//button[contains(@data-tooltip-id, 'Deactivate users')]")
    deleteSelected = (By.XPATH, "//button[contains(@data-tooltip-id, 'Delete users')]")

    #this is the general path, and selects the first found. to use this path search for the user specifically then use this locator
    userMenu = (By.XPATH, "//button[contains(@class, 'max-w-xs bg-white')]")
    menu_viewProfile = (By.XPATH, "//button[normalize-space()='View Profile']")
    menu_Workspaces = (By.XPATH, "//button[normalize-space()='Workspaces']")
    menu_DataAccess = (By.XPATH, "//button[normalize-space()='Data Access']")
    menu_RemoveAccess = (By.XPATH, "//button[normalize-space()='Remove Access']")

    exportUsers = (By.XPATH, "//div[contains(text(),'Export')]")
    exportFormat = (By.XPATH, "//button[contains(@aria-haspopup,'listbox') and //span[normalize-space()='.xls']]")
    xlsOption = (By.XPATH, "//li[(@role='option')][1]")
    csvOption = (By.XPATH, "//li[(@role='option')][2]")

class wsuserDialog:
    addUserBtn = (By.XPATH, "//button[contains(@class,'sm:w-auto')]")
    dialogWhiteSpace = (By.XPATH, "(//div[@class='flex justify-between py-4 px-4'])")
    fullNameInput = (By.XPATH, "//input[contains(@autocomplete,'new-fname')]")
    emailInput = (By.XPATH, "//input[@name='email']")

    #there needs to be page groups on the workspace for anything to populate here
    assignGroupsSearch = (By.XPATH, "//div[@class='relative rounded-md shadow-sm w-full flex']//input[@id='search']")

    addExistingUserBtn = (By.XPATH, "//div[contains(text(),'Add an existing user')]")
    searchExisitingUsers = (By.XPATH, "//input[@placeholder='Search']")
    #General path to all elements in the dropdown
    exisitingUserDropdown = (By.XPATH, "(//div[contains(@class,'cursor-pointer w-full truncate flex items-center px-4 py-2 gap-x-3 border-white hover:bg-gray-100')])")
    exsitingUserWhiteSpace = (By.XPATH, "//div[contains(@class, 'flex justify-between py-4 px-4')]")
    #these work in both dialog boxes
    CancelBtn = (By.XPATH, "//button[normalize-space()='Cancel']")
    SubmitBtn = (By.XPATH, "//button[normalize-space()='Submit']")

class wsgroupsElements:
    pass
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


    