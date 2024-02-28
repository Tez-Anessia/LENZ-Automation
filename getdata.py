import pandas as pd
import os
import logging

#dynamic function to get the current path to use when getting the data for the data frame
def getPath(folder, fileName): 
    currDir = os.getcwd()
    filePath = os.path.join(currDir, folder, fileName)
    return filePath

#general function to get a dataframe for any file and specific column
#file must be put in the data folder of the workspace
def getdf(fileName):
    df = pd.read_csv(getPath('data', fileName))
    return df

#----getting data from a specific column instead of a dataframe option------
def getColumnData(fileName, columnName):
    df = pd.read_csv(getPath('data', fileName))
    columnData = df[columnName].tolist()
    return columnData

#-----append the csv to add the workspace direct URL for a list of all of them-------
def addURL(fileName, companyName, url):
    filePath = getPath('data', fileName)
    df = pd.read_csv(filePath)
    df.loc[df['Company'] == companyName, 'URL'] = url
    df.to_csv(filePath, index=False)  
    logging.info(f"Url: {url} added to Customer: {companyName}")

#Test usage iteration:
#df = getdf('customerList.csv')
#for index, value in df.iterrows():
  #  print(value['Company']) 
