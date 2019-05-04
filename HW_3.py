# HW 3
# Name: Holland Ho
# Class: CPSC 223P Mon-Wed 

import pandas as pd
import sqlite3

# read the data set
data = pd.read_csv('breast-cancer-wisconsin.csv')
   
# transfering the contents of the data into SQL data base
class Database:
    pass

# convert the data set into JSON format
class Json:
    pass

def findMean(column_Choice):
    return data[column_Choice].mean()

def findSTD(column_Choice):
    return data[column_Choice].std()
    

print(findMean('clump_thickness'))
print(findSTD('clump_thickness'))


