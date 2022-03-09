1. 
Tools that I used in this project are:
Excel with Power Query for dashboards, data normalizations, and analysis
MySQL for database storage and creating OLAP tables using queries
Python (using PyCharm) for web development and database batching in a virtual environment
Jupyter notebook for quality testing the database and showing joins
Conda terminal to access jupyter notebook

Sources I used were:
 I was struggling to remember how to divide two lists by each other, and I couldn't find how to in my notes, so I used this source: https://www.geeksforgeeks.org/python-dividing-two-lists/ to help solve this problem, this was in the jupyer notebook section
I also used link: https://dev.mysql.com/doc/connectors/en/connector-odbc-configuration-dsn-windows-5-2.html to learn how to connect excel with MySQL using OBDC

2.
Python libraries used for -

PyCharm:
flask
os
flask-sqlalchemy
pymysql
cryptography
flask-wtf
wtforms
flask-Migrate
pandas
numpy
openpyxl 

Jupyter Notebook:
sqlalchemy
pandas
pymysql

3.
The first day the capstone was released I spent an hour getting familiar with the raw
data set to determine how I wanted to structure everything. I then spent roughly
three hours getting everything into how I wanted it ordered on the 
"capstonemasterspreadsheet.xlsx" file and then individually switched every table
into a CSV file (for batching). My experience in econometrics always tells me to 
spend a lot of time on the front end (data manipulation and formatting) to produce
a high quality end result. I also created a logo for the website.

The next day I began by using some aspects of my old website (from Flask assignment)
as a skeleton template, it got me started quickly and I was still able to make
customizable changes and tailor the website as to how I wanted it. By the end
of the first day I had the main structure of the website done and I was able
to upload the data to the data base. I also made great functionality and logical
additions to the database (delete entry functionality, new validator types, and
more).

Monday, I began the process of creating an OLAP database and their respective tables
to separate the scope of the data structure. Three OLAP tables were created using 
MySQL queries found in the data sheets folder. The other two were done using Excel
and PowerQuery data wrangling techniques. I also began on making excel dashboards
and linking tables to MySQL in excel (this is found in the data sheets folder titled
"capstonemasterspreadsheet"). 

The next two days I finalized the dashboards and created a quality analysis Jupyter 
Notebook (titled "Diagnostic Notebook.ipynb"). I also have done additional analysis
(some used pivot tables in the excel dashboard and some used calculations found in
the excel spreadsheet titled "Additional Analysis Sheets"

4.
I briefly wanted to touch base on folder structure to make sure everything is clear.
There are two main folders that are necessary ("appfolder" and "data sheets")
for this project

Appfolder: contains the main file (titled "mainfortractortek.py") that should be ran 
to execute the website. The file "batchingdata.py" was used to batch OLTP
and OLAP tables into the database. The file "formssetup.py" was used to create form
fields and proper data validations for forms. The subfolder inside of the appfolder
titled "Templates" contains all the design templates used in the website.

Data sheets:
contains:
the MySQL script used "capstoneMySQLscript"
The Jupyter notebook file for quality analysis and joins "Diagnostic Notebook.ipynb"
The Excel Dashboard "capstonemasterspreadsheet"
Additional spreadsheet used for analysis "Additional Analysis Sheets"
The rest of the files were CSVs used for batching and loading tables into the 
MySQL database from Python. 