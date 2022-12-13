select * from realstatesales.detroit
order by sale_date desc

SET SQL_SAFE_UPDATES = 0;

-- DATA CLEANING

-- Some same sales have low prices, ej 1 or 0 US, because are tranfers between family members or business to personal and viceversa
-- for the sake of the analisys we are going to delete this data because those are not actual sales.
select * from realstatesales.detroit 
where sale_price < 1000

DELETE FROM  realstatesales.detroit 
WHERE sale_price < 1000


-- object_id is redundant, doesnt apply any real data.

alter table realstatesales.detroit
drop column object_id

-- Those 4 houses are oversold, other houses in the street where sold at 10% of those prices.
delete from realstatesales.detroit
WHERE property_class in (401) AND sale_price > (1000000)

-- sale_date hr/minute/sec are redundant 



Alter Table realstatesales.detroit
add SaleDate date

Update realstatesales.detroit
set SaleDate = SUBSTRING(sale_date, 1 , LOCATE('+', sale_date)-1 )  

Alter Table realstatesales.detroit
drop column  sale_date 

select * from realstatesales.detroit
order by SaleDate desc

--QC AND QCD ARE THE SAME



Update realstatesales.detroit
SET sale_instrument =
 CASE WHEN sale_instrument ='QCD' then 'QC' 
	  ELSE sale_instrument 
END 


-- clean date from rent db--------------


Update realstatesales.rental
set date_status = SUBSTRING(date_status, 1 , LOCATE('+', date_status)-1 )  

Alter Table realstatesales.rental
modify date_status date

-- Drop objectID = index
Alter Table realstatesales.rental
drop column ObjectID

-- join street_num and street_name
Alter Table realstatesales.rental
add address varchar(256)

update realstatesales.rental
set address =concat(street_num  , ' ' ,street_name)

Alter Table realstatesales.rental
drop column street_num

Alter Table realstatesales.rental
drop column street_name

-- street dir is all null, drop

Alter Table realstatesales.rental
drop column street_dir








-- alter US AVRG PRICES DATE

Alter Table realstatesales.avrghousessoldus
modify DATE date

-- Changes to unemplywc table numbers have , instead of .

Update realstatesales.detroit
SET sale_instrument =
 CASE WHEN sale_instrument ='QCD' then 'QC' 
	  ELSE sale_instrument 
END 

update realstatesales.unemploywc
SET Unemployment Rate = REPLACE(Unemployment Rate ,',', '.')


-- change popdetroit table in population coulmn name and year data type
ALTER TABLE realstatesales.popdetriotmetro
RENAME COLUMN `Population (Population)` TO `population` ;

Alter Table realstatesales.popdetriotmetro
modify Year Year





-- Continue in python









