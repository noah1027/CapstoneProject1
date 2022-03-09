from flask import Flask, render_template, url_for, redirect, session
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
import cryptography
from formssetup import AddWeeklyProductEntry, AddWeeklyWarrantyEntry, DeleteWeeklyProductEntry, DeleteWeeklyESPEntry

#Main configurations
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password1!@localhost/Appdata2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'
db = SQLAlchemy(app)
Migrate(app, db)

#To create a class for the aggregate sales table for tractors, broken down by week,year, and employee
class ProductSales(db.Model):
    __tablename__ = 'productsales'
    index = db.Column(db.Integer,primary_key=True)
    prod_code = db.Column(db.Text)
    employee_id = db.Column(db.Text)
    year_id = db.Column(db.Integer)
    week = db.Column(db.Integer)
    quantity_prodsold = db.Column(db.Integer)

    def __init__(self, prod_code, employee_id, year_id, week, quantity_prodsold):
        self.prod_code = prod_code
        self.employee_id = employee_id
        self.year_id = year_id
        self.week = week
        self.quantity_prodsold = quantity_prodsold

    def __repr__(self):
        return f"Record number {self.index} shows employee {self.employee_id}'s team sold {self.quantity_prodsold} units of {self.prod_code} in {self.week} week of {self.year_id} ID"
#To create a class for the aggregate sales table for warranty (esp), broken down by week,year, and employee
class WarrantySales(db.Model):
    __tablename__ = 'warrantysales'
    index = db.Column(db.Integer, primary_key=True)
    esp_code = db.Column(db.Text)
    employee_id = db.Column(db.Text)
    year_id = db.Column(db.Integer)
    week = db.Column(db.Integer)
    quantity_espsold = db.Column(db.Integer)

    def __init__(self, esp_code, employee_id, year_id, week, quantity_espsold):
        self.esp_code = esp_code
        self.employee_id = employee_id
        self.year_id = year_id
        self.week = week
        self.quantity_espsold = quantity_espsold

    def __repr__(self):
        return f"Record number {self.index} shows employee {self.employee_id}'s team sold {self.quantity_espsold} units of {self.esp_code} in {self.week} week of {self.year_id} ID"

 #Creates a class for the work week table
class WorkWeek(db.Model):
    __tablename__ = 'workweek'
    week = db.Column(db.Integer, primary_key=True)
    quarter = db.Column(db.Integer)
    year_id = db.Column(db.Integer, primary_key=True)
    date_start_corresponding = db.Column(db.String)

    def __init__(self, week, quarter, year_id, date_start_corresponding):
        self.week = week
        self.quarter = quarter
        self.year_id = year_id
        self.date_start_corresponding = date_start_corresponding

    def __repr__(self):
        return f"For {self.week} week in the {self.year_id} year, corresponds with {self.date_start_corresponding} and quarter {self.quarter}."

#Creates a class for the work year table
class WorkYear(db.Model):
    __tablename__ = 'workyear'
    year_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)

    def __init__(self, year_id, year):
        self.year_id = year_id
        self.year = year

    def __repr__(self):
        return f"For {self.year_id}, the corresponding year is {self.year}."

#home page route
@app.route('/')
def index():
    return render_template('caphome.html')

#Displays list of weekly product sales entries
@app.route('/productsaleslist')
def weekly_product_sales_list():
    ProductSalesList = ProductSales.query.all()
    return render_template('weeklyproductsaleslist.html', ProductSalesList=ProductSalesList)

#Displays list of weekly ESP sales entries
@app.route('/espsaleslist')
def weekly_esp_sales_list():
    ESPSalesList = WarrantySales.query.all()
    return render_template('weeklyespsaleslist.html', ESPSalesList=ESPSalesList)

#Displays list of year to year ID conversions
@app.route('/yeartable')
def year_table():
    YearConversionList = WorkYear.query.all()
    return render_template('yeartablelist.html', YearConversionList=YearConversionList)

#Displays list of work week conversions
@app.route('/weektable')
def week_table():
    WeekConversionList = WorkWeek.query.all()
    return render_template('weektablelist.html', WeekConversionList=WeekConversionList)

#add a route to weekly product sales entry
@app.route('/productsalesentry', methods=['GET','POST'])
def add_weekly_product_sales_entry():
    form = AddWeeklyProductEntry()

    if form.validate_on_submit():
        prod_code = form.prod_code.data
        employee_id = form.employee_id.data
        year_id = form.year_id.data
        week = form.week.data
        quantity_prodsold =form.quantity_prodsold.data

        new_weekly_product_report = ProductSales(prod_code, employee_id, year_id, week, quantity_prodsold)
        db.session.add(new_weekly_product_report)
        db.session.commit()

        return redirect(url_for('weekly_product_sales_list'))

    return render_template('addweeklyproductsales.html', form=form)

#Adds a route to weekly ESP sales entry
@app.route('/espsalesentry', methods=['GET','POST'])
def add_weekly_esp_sales_entry():
    form = AddWeeklyWarrantyEntry()

    if form.validate_on_submit():
        esp_code = form.esp_code.data
        employee_id = form.employee_id.data
        year_id = form.year_id.data
        week = form.week.data
        quantity_espsold =form.quantity_espsold.data

        new_weekly_esp_report = WarrantySales(esp_code, employee_id, year_id, week, quantity_espsold)
        db.session.add(new_weekly_esp_report)
        db.session.commit()

        return redirect(url_for('weekly_esp_sales_list'))

    return render_template('addweeklyespsales.html', form=form)

#Adds a route on site to delete a weekly product entry
@app.route('/deleteproductentry', methods=['GET', 'POST'])
def delete_weekly_product_sales_entry():
    form = DeleteWeeklyProductEntry()

    if form.validate_on_submit():
        if form.confirmation.data == 'YES':
            index = form.index.data
            entry = ProductSales.query.get(index)
            db.session.delete(entry)
            db.session.commit()
        else:
            return redirect(url_for('delete_weekly_product_sales_entry'))
        return redirect(url_for('weekly_product_sales_list'))
    return render_template('deleteweeklyproductsales.html', form=form)

#adds a route to delete a weekly ESP entry
@app.route('/deleteespentry', methods=['GET', 'POST'])
def delete_weekly_esp_sales_entry():
    form = DeleteWeeklyESPEntry()

    if form.validate_on_submit():
        if form.confirmation.data == 'YES':
            index = form.index.data
            entry = WarrantySales.query.get(index)
            db.session.delete(entry)
            db.session.commit()
        else:
            return redirect(url_for('delete_weekly_esp_sales_entry'))
        return redirect(url_for('weekly_esp_sales_list'))
    return render_template('deleteweeklyespsales.html', form=form)













if __name__ == '__main__':
    app.run(debug=True)