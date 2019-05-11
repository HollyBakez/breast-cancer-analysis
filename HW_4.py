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

# transfering the contents of the data into SQL data base
conn = sqlite3.connect('breast_cancer_analysis.db')
data.to_sql('breast', con = conn, if_exists = 'replace')

# checking if data exported to sqlite
df_db = pd.read_sql_query("SELECT * FROM breast", conn)

conn.close()

# convert the data set into JSON format
data.to_json('breast.json', orient = 'split')
df_json = pd.read_json('breast.json', orient = 'split')

def visualGraphs(column_Choice):
    plt.clf()
    data[column_Choice].plot(kind = 'box')
    plt.show()

# shows datafram obj
print(type(data))
# shows json format
print(df_json)
# shows sql database contents
print(df_db)

# finding the mean and standard deviation
print("Data Mean: \n",data_no_id.mean())
print("Data STD: \n",data_no_id.std())

# showing the graphs of each column
for index in data_no_id.columns:
    visualGraphs(index)
'''
========== Similar Shapes ============
 size_uniformity & shape_uniformity 
 marginal_adhesion & normal_nucleoli 
======================================
'''
# Using the dataframe method
# and scatter plots
# we can tell that the two columns 
# "size_uniformity" & "shape_uniformity"
# are positively correlated
plt.clf()
data_no_id.plot(kind = 'scatter', x = 'size_uniformity', y = 'shape_uniformity')
plt.show()

# groups the records 
# using the class column
# shows the mean & std and boxplot
g_data = data_no_id.groupby('class')
print("class mean: \n",g_data.mean())
print("class std: \n",g_data.std())

#drop class column 
data_no_class = data_no_id.drop(['class'], axis = 1)
# plots the grouped class records into boxplot
# plots for each column by 'class' group
for index in data_no_class.columns:
    plt.clf()
    data_no_id.boxplot(column = [index], by = 'class')
    plt.show()
