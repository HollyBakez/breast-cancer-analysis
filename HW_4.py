# HW 4
# Name: Holland Ho
# Class: CPSC 223P Mon-Wed 

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# read the data set as dataFrame
data = pd.read_csv('breast-cancer-wisconsin.csv')

#drops incomplete rows and changes bare_nucleoli to all ints
indexQuestion = data[ data['bare_nucleoli'] == '?'].index
data.drop(indexQuestion, inplace = True)
data.bare_nucleoli = data.bare_nucleoli.astype(int)
# dropping id to only get the columns with values needed
data_no_id = data.drop(['id'], axis = 1)

print(data_no_id.bare_nucleoli.unique)

# transfering the contents of the data into SQL data base
conn = sqlite3.connect('breast_cancer_analysis.db')
data.to_sql('breast', con = conn, if_exists = 'replace')

# checking if data exported to sqlite
df_db = pd.read_sql_query("SELECT * FROM breast", conn)

conn.close()

# convert the data set into JSON format
data.to_json('breast.json', orient = 'split')
df_json = pd.read_json('breast.json', orient = 'split')

'''
def findMean_STD(column_Choice):
    col_mean = data[column_Choice].mean()
    col_std = data[column_Choice].std()
    print("The", column_Choice, "Mean is:", col_mean, "\nThe", column_Choice,"STD is: ", col_std)
'''
def visualGraphs(column_Choice):
    plt.clf()
    data[column_Choice].plot(kind = 'box')
    plt.show()
    
print(type(data))
print(df_json)

# finding the mean and standard deviation
print(data_no_id.mean())
print(data_no_id.std())
'''
# displaying the mean and std of every column
for index in data_no_id.columns:
    findMean_STD(index)
'''
#visualGraphs('bare_nucleoli')
#TODO 
# compare curves generated and determine which columns have distrubution functions of similar shape
for index in data_no_id.columns:
    visualGraphs(index)

