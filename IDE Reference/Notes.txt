#checkbox
# Find the checkbox element
checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")

# Check if the checkbox is selected
if checkbox.is_selected():
    print("Checkbox is selected")
    # Perform actions when the checkbox is selected
else:
    print("Checkbox is not selected")
    # Perform actions when the checkbox is not selected


import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Testsheet.csv')

# Extract the 'Customer Name' column from the DataFrame and convert it to an array
customer_names_array = df['Customer Name'].values

# Print the array to verify the result
print(customer_names_array)