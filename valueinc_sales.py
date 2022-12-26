#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:00:47 2022

@author: mamadou
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') ---> format read csv

data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv', sep=';')

#Summary of the data
data.info()

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingCostPerItem = 21.11
NumbersOfItemsPurchases = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingCostPerItem - CostPerItem

ProfitPerTransaction = NumbersOfItemsPurchases * ProfitPerItem

CostPertransaction = CostPerItem * NumbersOfItemsPurchases
SellingPriceByTransaction = SellingCostPerItem * NumbersOfItemsPurchases


#CostPertransaction columns calculation

#CostPertransaction = CostPerItem * NumbersOfItemsPurchases
#variable  dataframe['column_name'


CostPerItem = data['CostPerItem']
NumbersOfItemsPurchased =data['NumberOfItemsPurchased']

CostPertransaction = CostPerItem * NumbersOfItemsPurchased

#Adding a new column to a dataframe

data['CostPertransaction']= CostPertransaction

data['CostPertransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales Per Transactions

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit = sales - Cost

#Markup= (Sale-Cost) / Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPertransaction']

data['Markup'] = data['ProfitPerTransaction'] / data['CostPertransaction']


#rounding Markup
roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#Concatening data fields
my_name = 'Mamadou'+'Dembele'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

my_date= data['Day']
data.info()

#Checking Columns datatype
print(data['Day'].dtype)

#Changing columns type

day = data['Day'].astype(str)
year =data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['my_date'] = my_date

#Using iloc to view specific coloumns/rows

data.iloc[0] #view the row with index = 0

data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows


data.head(5) #First 5 rows

data.tail(5) #Last  5 rows

data.iloc[:,2]
data.iloc[4,2] # brings in all fourth row and second column


#Using split to split split client keyword
#new_var = columns.str.split('sep' ,. expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand =True)


#Creating new columns for the splis in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthContrat'] = split_col[2]

#Using the replace function 
data['ClientAge']= data['ClientAge'].str.replace('[' , '')
data['LengthContrat'] = data['LengthContrat'].str.replace(']' , '')

#Using the lower function to change item to lowercase

data['ItemDescription']= data['ItemDescription'].str.lower()



#How to merge file

#Briging a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')


#merging file: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#Droping Columns
#df =df.drop('Columnname', axis =1)

data = data.drop ('ClientKeywords' , axis =1)
data = data.drop ('Day', axis = 1)
#data = data.drop (['Year' , 'Month', 'MarkupPerTransaction' ] , axis = 1 )


#Export into csv

data.to_csv('valueInc_Clean.csv', index = False)
























































