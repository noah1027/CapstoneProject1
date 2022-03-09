USE appdata2;


#I created this temporary table to make a total product revenue per employee per year table
CREATE temporary table totalquantity_peremp_peryear
select prod_code, employee_id, year_id, SUM(quantity_prodsold) AS totalquantity from productsales
group by prod_code, employee_id, year_id;

select * from totalquantity_peremp_peryear;

drop temporary table totalquantity_peremp_peryear;

#creates a total revenue from product sold per employee per year 
create table total_product_revenue_per_emp_per_year
as select product.prod_name, sales_team_lead, workyear.year, (totalquantity*prod_price) as totalsalesrevenue from totalquantity_peremp_peryear
inner join productprice on totalquantity_peremp_peryear.prod_code = productprice.prod_code and totalquantity_peremp_peryear.year_id = productprice.year_id
left join product on product.prod_code = totalquantity_peremp_peryear.prod_code
left join employee on employee.employee_id = totalquantity_peremp_peryear.employee_id
left join workyear on workyear.year_id = totalquantity_peremp_peryear.year_id
group by productprice.year_id, totalquantity_peremp_peryear.prod_code, totalquantity_peremp_peryear.employee_id;



#this moves the database from the OLTP schema (appdata2) to the OLAP schema (appdata3)
alter table appdata2.total_product_revenue_per_emp_per_year rename appdata3.total_product_revenue_per_emp_per_year;


#creates an aggregate quantity for warranty sold per employee per year, used for creating a total revenue table
create temporary table totalwarrantyquantity_peremp_peryear
select esp_code, employee_id, year_id, sum(quantity_espsold) as total_esp_quantity from warrantysales
group by esp_code, employee_id, year_id;


select * from totalwarrantyquantity_peremp_peryear;
drop temporary table totalwarrantyquantity_peremp_peryear;


#creates an aggregate total revenue from warrantys sold per employee per year 
create table total_warranty_revenue_per_emp_per_year
as select prod_name, totalwarrantyquantity_peremp_peryear.esp_code, sales_team_lead, workyear.year , (total_esp_quantity*warranty_price) as totalwarrantysalesrevenue from totalwarrantyquantity_peremp_peryear
inner join warrantyprice on totalwarrantyquantity_peremp_peryear.esp_code = warrantyprice.esp_code
left join employee on employee.employee_id = totalwarrantyquantity_peremp_peryear.employee_id
left join product on warrantyprice.prod_code = product.prod_code
left join workyear on workyear.year_id = totalwarrantyquantity_peremp_peryear.year_id
group by year, totalwarrantyquantity_peremp_peryear.esp_code, totalwarrantyquantity_peremp_peryear.employee_id;


#this moves the database from the OLTP schema (appdata2) to the OLAP schema (appdata3)
alter table appdata2.total_warranty_revenue_per_emp_per_year rename appdata3.total_warranty_revenue_per_emp_per_year;

use appdata3;

#This creates a table in the OLAP schema (appdata3) that measures the warranty conversion rate (total warranty sold/ total product sold) for each product by employee and by year
create table warranty_conversion_rate
as select denormalized_product_sales.product_name, denormalized_product_sales.year, denormalized_product_sales.employee_name as sales_team_lead,(denormalized_warranty_sales.yearly_totals/denormalized_product_sales.yearly_totals) as warranty_conversion_rate from denormalized_product_sales
inner join denormalized_warranty_sales on denormalized_warranty_sales.prod_code = denormalized_product_sales.prod_code and denormalized_warranty_sales.year_id = denormalized_product_sales.year_id and denormalized_warranty_sales.employee_id = denormalized_product_sales.employee_id
group by denormalized_product_sales.prod_code, denormalized_product_sales.year_id, denormalized_product_sales.employee_id;




