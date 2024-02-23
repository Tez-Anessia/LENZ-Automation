import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('your_file.csv')

# Open the browser (assuming you've already set up your WebDriver, like ChromeDriver)
driver = webdriver.Chrome('path_to_chromedriver')

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Assuming 'Customer Name' is one of the columns in your CSV
    customer_name = row['Customer Name']
    
    # Assuming 'Workspace Name' is another column in your CSV
    workspace_name = row['Workspace Name']
    
    # Open the page where you want to create the workspace
    driver.get('url_of_the_page')

    # Find the fields and fill them with the values from the CSV
    customer_name_field = driver.find_element_by_id('customer_name_id')
    customer_name_field.clear()  # Clear any existing value
    customer_name_field.send_keys(customer_name)

    workspace_name_field = driver.find_element_by_id('workspace_name_id')
    workspace_name_field.clear()
    workspace_name_field.send_keys(workspace_name)

    # Add any additional fields and actions as needed
    
    # Submit the form or perform any other actions to create the workspace
    submit_button = driver.find_element_by_id('submit_button_id')
    submit_button.click()

    # Optionally, add a delay to allow the page to load
    time.sleep(2)

# Close the browser when done
driver.quit()
