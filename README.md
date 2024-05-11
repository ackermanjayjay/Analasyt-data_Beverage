# Analasyt-data_Beverage CoffeShop(Starbucks)


## Objective
This project make ETL and analyst data beverage starbucks 
Objective this project to analyst healty drink **(please drink water only if you want healty or black coffe or tea dont use sugar)**


## Scope
* Search data and download from [kaggle](https://www.kaggle.com/datasets/henryshan/starbucks)
* Extract data and transformation to SQL load to SQL extension 
* Analyst with SQL (PostgresSQL)

## Result
<p>
With analyst data using SQL with this code:

<pre>
select "beverage", "sugars(g)" ,"calories" from menu_starbucks  as low_sugar_and_low_cal
order by "calories" asc, "sugars(g)" asc
limit 10
</pre>
|beverage|sugars(g)|calories|
|--------|---------|--------|
|Tazo® Tea|0|0|
|Tazo® Tea|0|0|
|Tazo® Tea|0|0|
|Tazo® Tea|0|0|
|Brewed Coffee|0|3|
|Brewed Coffee|0|4|
|Espresso|0|5|
|Brewed Coffee|0|5|
|Caffè Americano|0|5|
|Brewed Coffee|0|5|



## Conclusion
* This data have 243 records data
* Have 18 columns
* Before inserted to table database, Transformation columns before Capitalize to lowercase and before have whitespace to "_" 