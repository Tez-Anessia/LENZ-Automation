import pandas as pd
import os
from pathlib import Path
# import logger 

# log = logger.setUp()

# Dynamic function to get the file path for the files in the data folder. The function goes back to the parent dir "LENZ-Automation", then appends the file path to put folder and file name in the path
# assumes file structure where commonUtils and data folders are in the same level
def get_path(folder, fileName):
    #path gets out of commonUtils and gets us in the main folder
    parentDir = Path(__file__).parents[1]
    #combine the parent path and enter in folder file. for img send "data/imgs"
    filePath = os.path.join(parentDir, folder, fileName)
    return filePath

# General function to get a dataframe for any file and specific column
# File must be put in the data folder of the workspace
def get_df(fileName):
    filePath = get_path("data", fileName)
    df = pd.read_csv(filePath)
    return df

# Getting data from a specific column instead of a dataframe option
def get_column_data(fileName, columnName):
    df = pd.read_csv(get_path('data', fileName))
    columnData = df[columnName].tolist()
    return columnData

# Append the csv to add the workspace direct URL for a list of all of them
# The CSV should have the headers [Company, SalesRep, URL]
def add_URL(fileName, companyName, url):
    filePath = get_path('data', fileName)
    df = pd.read_csv(filePath)
    df.loc[df['Company'] == companyName, 'URL'] = url
    df.to_csv(filePath, index=False)  
   # log.info(f"Url: {url} added to Customer: {companyName}")

# Function that reads a csv, searches the column company for companyName then returns the value in the column URL that is in the same row
def get_url(fileName, companyName):
    pass