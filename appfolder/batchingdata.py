import sqlalchemy
from flask import Flask, render_template, url_for, redirect, session
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
from mainfortractortek import db, ProductSales, WarrantySales, WorkWeek, WorkYear
import pandas as pd
import numpy as np
import openpyxl

#engine essentially creates a connection to the MySQL database
#the pd.read commands essentially reads the CSV/Excel files and I set them to a variable name as a pandas dataframe
#Afterwards, I print the dataframe to confirm their creation and existence.
#Then I run the .to_sql on each dataframe to send it to the MySQL database
engine = sqlalchemy.create_engine('mysql+pymysql://root:Password1!@localhost/Appdata2')
productsalesframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\productsales.csv', index_col=False)
warrantysalesframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\warrantysales.csv', index_col=False)
weektoquarterframe = pd.read_excel(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\weektoquarter.xlsx', index_col=False)
yearframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\year.csv', index_col=False)
employeetableframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\employeetable.csv', index_col=False)
manufacturertableframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\manufacturertable.csv', index_col=False)
productpricebyquarterframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\productpricebyquarter.csv', index_col=False)
producttableframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\producttable.csv', index_col=False)
regiontableframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\regiontable.csv', index_col=False)
warrantypriceframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\warrantyprice.csv', index_col=False)

print(productsalesframe)
print(warrantysalesframe)
print(weektoquarterframe)
print(yearframe)
print(employeetableframe)
print(manufacturertableframe)
print(productpricebyquarterframe)
print(producttableframe)
print(regiontableframe)
print(warrantypriceframe)

#these commands below are commented out because I already successfully uploaded these data sets into MySQL

#productsalesframe.to_sql('productsales', engine, schema='appdata2', if_exists='append', index=False)
#warrantysalesframe.to_sql('warrantysales', engine, schema='appdata2', if_exists='append', index=False)
#weektoquarterframe.to_sql('workweek', engine, schema='appdata2', if_exists='replace', index=False)
#yearframe.to_sql('workyear', engine, schema='appdata2', if_exists='append', index=False)
#employeetableframe.to_sql('employee', engine, schema='appdata2', if_exists='append', index=False)
#manufacturertableframe.to_sql('manufacturer', engine, schema='appdata2', if_exists='append', index=False)
#productpricebyquarterframe.to_sql('productprice', engine, schema='appdata2', if_exists='append', index=False)
#producttableframe.to_sql('product', engine, schema='appdata2', if_exists='append', index=False)
#regiontableframe.to_sql('region', engine, schema='appdata2', if_exists='append', index=False)
#warrantypriceframe.to_sql('warrantyprice', engine, schema='appdata2', if_exists='append', index=False)

#I decided to create a new section of the database specifically for the denormalized data and OLAP purposes,
#therefore I had to create a new engine routed to the new database, then I repeated
#the same procedure as above, except with the denormalized data sets.

enginefordenormalizeddata = sqlalchemy.create_engine('mysql+pymysql://root:Password1!@localhost/Appdata3')
denormalizedproductsales = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\productsalesdenormalized.csv', index_col=False)
denormalizedwarrantysales = pd.read_csv(r'C:\Users\tveva\PycharmProjects\CapstoneProject1\data sheets\warrantysalesdenormalized.csv', index_col=False)

print(denormalizedwarrantysales)
print(denormalizedproductsales)

#I commented out the below statements because I already ran them and added them to the database

#denormalizedproductsales.to_sql('denormalized_product_sales', enginefordenormalizeddata, schema='appdata3', if_exists='append', index=False)
#denormalizedwarrantysales.to_sql('denormalized_warranty_sales', enginefordenormalizeddata, schema='appdata3', if_exists='append', index=False)