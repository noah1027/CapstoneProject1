from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, number_range

class AddWeeklyProductEntry(FlaskForm):
    prod_code = SelectField("Product Code:", choices=[('PROD001'),('PROD002'),('PROD003'),('PROD004'),('PROD005'),('PROD006'),('PROD007'),('PROD008')], validators=[DataRequired()])
    employee_id = SelectField("Sale team's lead employee ID:", choices=[('EMP244'),('EMP256'),('EMP234'),('EMP267'),('EMP290')], validators=[DataRequired()])
    year_id = IntegerField("Year ID (Please verify through Year's table):", validators=[DataRequired()])
    week = IntegerField("Week (Please verify through the week table):", validators=[DataRequired(),number_range(min=0, max=51, message='Please enter a valid week number.')])
    quantity_prodsold = IntegerField('Quantity of product sold:', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddWeeklyWarrantyEntry(FlaskForm):
    esp_code = SelectField("ESP Code:", choices=[('ESP001'), ('ESP002'), ('ESP003'), ('ESP004'), ('ESP005'), ('ESP006'), ('ESP007'), ('ESP008')], validators=[DataRequired()])
    employee_id = SelectField("Sale team's lead employee ID:", choices=[('EMP244'),('EMP256'),('EMP234'),('EMP267'),('EMP290')], validators=[DataRequired()])
    year_id = IntegerField("Year ID (Please verify through Year's table):", validators=[DataRequired()])
    week = IntegerField("Week (Please verify through the week table):", validators=[DataRequired(),number_range(min=0, max=51, message='Please enter a valid week number.')])
    quantity_espsold = IntegerField('Quantity of the ESP sold:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteWeeklyProductEntry(FlaskForm):
    index = IntegerField('Please enter the index number of the entry you wish to delete', validators=[DataRequired()])
    confirmation = SelectField('Please review the above entry, are you sure you wish to delete this entry?', choices=[('NO'), ('YES')], validators=[DataRequired()])
    submit = SubmitField('Delete Entry')

class DeleteWeeklyESPEntry(FlaskForm):
    index = IntegerField('Please enter the index number of the entry you wish to delete', validators=[DataRequired()])
    confirmation = SelectField('Please review the above entry, are you sure you wish to delete this entry?', choices=[('NO'), ('YES')], validators=[DataRequired()])
    submit = SubmitField('Delete Entry')
