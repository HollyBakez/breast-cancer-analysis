# HW 4
# Name: Holland Ho
# Class: CPSC 223P Mon-Wed 

import pandas as pd
import sqlite3

# read the data set as dataFrame
data = pd.read_csv('breast-cancer-wisconsin.csv')
# dropping id to only get the columns with values needed
data_no_id = data.drop(['id'], axis = 1)
# transfering the contents of the data into SQL data base
conn = sqlite3.connect('breast_cancer_analysis.db')
data.to_sql('breast', con = conn, if_exists = 'replace')

# checking if data exported to sqlite
df_db = pd.read_sql_query("SELECT * FROM breast", conn)

conn.close()

# convert the data set into JSON format
data.to_json('breast.json', orient = 'split')
df_json = pd.read_json('breast.json', orient = 'split')

# finding the mean and standard deviation
def findMean_STD(column_Choice):
    col_mean = data[column_Choice].mean()
    col_std = data[column_Choice].std()
    return print("The", column_Choice, "Mean is:", col_mean, "\nThe", column_Choice,"STD is: ", col_std)
    #return print("The",column_Choice,"mean is:",data[column_Choice].mean(), "\nThe", column_Choice, "STD is: ", data[column_Choice].std())

print(type(data))
#print(df_db)
print(df_json)
# displaying the mean and std of every column
'''
findMean_STD('clump_thickness')
findMean_STD('size_uniformity')
findMean_STD('shape_uniformity')
findMean_STD('marginal_adhesion')
findMean_STD('epithelial_size')
findMean_STD('bare_nucleoli')
findMean_STD('bland_chromatin')
findMean_STD('normal_nucleoli')
findMean_STD('mitoses')
findMean_STD('class')
'''
for index in data_no_id.columns:
    print(index)
    findMean_STD(index)