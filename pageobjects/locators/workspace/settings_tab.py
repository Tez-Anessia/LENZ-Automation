from selenium.webdriver.common.by import By

class SettingsElements:
    add_filter_btn = (By.XPATH, "//div[2]/div[(@class='w-full justify-between flex items-center gap-4')]/button")
    column_name_input = (By.NAME, "column-name")
    logic_dropdown = (By.XPATH, "//div[@class='w-full h-full flex justify-between items-center']//button[contains(@class,'h-10 relative')]")
    equaltoOption = (By.XPATH, "(//li[@role='option'])[1]")
    allOptions = (By.XPATH, "(//li[@role='option'])")
    textValueInput = (By.XPATH, "//input[@name='column-value']")
    deleteWorkspace = (By.XPATH, "//button[@class='group inline-flex items-center justify-center transition-all duration-200 rounded-md border px-4 py-2 text-regular font-medium focus:ring-2 focus:border-highlightColor bg-white text-highlightColor border-[1px] border-highlightColor hover:shadow-sm  sm:w-auto h-12 !text-red-300 !border-red-300']")


