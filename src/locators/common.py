from selenium.webdriver.common.by import By

#this will contain elements that are shown in each page
class CommonElements: 
    #-----------------User Settings-----------------
    account_Menu = (By.XPATH, "//button[@id='headlessui-menu-button-1']")
    #Must click on account menu first before these are findable
    myAccount = (By.XPATH, "//a[normalize-space()='My account']")
    userPortal= (By.XPATH, "//a[normalize-space()='User portal']")
    signout = (By.XPATH, "//button[normalize-space()='Sign out']")

    #-----------------Pagination-----------------
    pgBox = (By.XPATH, "//button[contains(@class, 'bg-white relative')]")
    #--found only after paginationBox element is clicked
    see10 = (By.XPATH, "//p[normalize-space()='10']")
    see20 = (By.XPATH, "//p[normalize-space()='20']")
    see50 = (By.XPATH, "//p[normalize-space()='50']")
    see75 = (By.XPATH, "//p[normalize-space()='75']")
    see100 = (By.XPATH, "//p[normalize-space()='100']")
    seeAll = (By.XPATH, "//p[normalize-space()='All']")