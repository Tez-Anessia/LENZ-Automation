from selenium.webdriver.common.by import By
#(By.XPATH, "")
class login: 
    username_input = (By.XPATH, "//input[@name='contact-email']")
    password_input = (By.XPATH, "//input[@name='password']")
    login_btn = (By.XPATH, "//div[contains(text(),'Login')]")

#this will contain elements that are shown in each page
class commonElements: 
    account_Menu = (By.XPATH, "//button[@id='headlessui-menu-button-1']")
    # Must click on account menu first before these are findable
    myAccount = (By.XPATH, "//a[normalize-space()='My account']")
    userPortal= (By.XPATH, "//a[normalize-space()='User portal']")
    signout = (By.XPATH, "//button[normalize-space()='Sign out']")

    #Pagination
    pgBox = (By.XPATH, "//button[contains(@class, 'bg-white relative')]")
    #--found only after paginationBox element is clicked
    see10 = (By.XPATH, "//p[normalize-space()='10']")
    see20 = (By.XPATH, "//p[normalize-space()='20']")
    see50 = (By.XPATH, "//p[normalize-space()='50']")
    see75 = (By.XPATH, "//p[normalize-space()='75']")
    see100 = (By.XPATH, "//p[normalize-space()='100']")
    seeAll = (By.XPATH, "//p[normalize-space()='All']")

#Workspace Tab
    """
    Because the table is dynamic, listed here are some paths to reference
    - get url for specific workspace in table: "//table/tbody/tr/td[.//div[contains(text(),'"+ workspaceName +"')]]/div/a[contains(@href,'/workspaces')]"
    - find specific workspace in the table(locate only): "//div[contains(text(),'"+ customerName +"')]"   
    """
class workspaceTab:
    searchBar = (By.XPATH, "//input[@id='search']")
    addWorkspace = (By.XPATH, "//button[@data-tooltip-id='Add a workspace-custom-link']")
    
    #Table Paths
    #--all elements in the name column
    nameColumn_elements = (By.XPATH, "(//div[@class='w-full flex gap-x-3 items-center relative'])")
    #--last visible workspace element in the table
    lastWSinTable = (By.XPATH, "(//div[@class='w-full flex gap-x-3 items-center relative'])[last()]")

#--Dialog box when pressing addworkspace button
class addWorkspace_dialog: 
    workspaceName = (By.XPATH, "//input[@name='name']")
    cancelBtn = (By.XPATH, "//button[normalize-space()='Cancel']")
    saveBtn = (By.XPATH, "//button[normalize-space()='Save']")
    whiteSpace = (By.XPATH, "//div[contains(@class,'flex justify-between py-4 px-4')]")

#--locators for a specific workspace
class workspace: 
    workspaceName = (By.XPATH, "//input[@name='workspace-name']")
    
