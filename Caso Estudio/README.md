# Caso de estudio retail_db

Creación de base de datos con configuraciones en [retail_db-ddl.sql](https://github.com/jscaicedom/BigDataLab/blob/master/bigdata/rdbms/retail_db-ddl.sql) y [retail_db-data.sql](https://github.com/jscaicedom/BigDataLab/blob/master/bigdata/rdbms/retail_db-data.sql)

En la instancia Ec2 

```
$ sudo yum install git
$ git clone https://github.com/jscaicedom/BigDataLab.git
$ mysql -u admin -p -h database.cy5rftlokiyu.us-east-1.rds.amazonaws.com retail_db < BigDataLab/bigdata/rdbms/retail_db-data.sql
```

En el clúster para procesar ETL

```
$ hdfs dfs -chown -R admin:hdfs /user/admin/
```

Productos más vendidos 

```
SELECT p.product_name, count(order_item_quantity) as count
FROM order_items oi
inner join products p on oi.order_item_product_id = p.product_id
group by p.product_name
order by count desc
limit 10
```
 
| No | p.product_name |	count |
| ----- | -------------- | ------ |
| 1 |	Perfect Fitness Perfect Rip Deck |	24515 |
| 2 |	Nike Men\'s CJ Elite 2 TD Football Cleat |	22246 |
| 3 |	Nike Men\'s Dri-FIT Victory Golf Polo	| 21035 |
| 4	| O\'Brien Men\'s Neoprene Life Vest	| 19298 | 
| 5 |	Field & Stream Sportsman 16 Gun Fire Safe |	17325 |
| 6	| Pelican Sunstream 100 Kayak	| 15500 |
| 7	| Diamondback Women\'s Serene Classic Comfort Bi |	13729 |
| 8	| Nike Men\'s Free 5.0+ Running Shoe |	12169 |
| 9	| Under Armour Girls\' Toddler Spine Surge Runni |	10617 |
| 10	| Nike Men\'s Comfort 2 Slide	| 328 |


| p.product_name |	 ventas | visitas |
| ----- | -------------- | ------ |
|	Perfect Fitness Perfect Rip Deck |	24515 | 1926 |
|	Nike Men\'s CJ Elite 2 TD Football Cleat |	22246 | 1757 |
|	Nike Men\'s Dri-FIT Victory Golf Polo	| 21035 | 1780 |
| O\'Brien Men\'s Neoprene Life Vest	| 19298 | 1084 |
|	Field & Stream Sportsman 16 Gun Fire Safe |	17325 | 1028 |
| Pelican Sunstream 100 Kayak	| 15500 | 1104 |
| Diamondback Women\'s Serene Classic Comfort Bi |	13729 | 1059 |
| Nike Men\'s Free 5.0+ Running Shoe |	12169 | 1004 |
| Under Armour Girls\' Toddler Spine Surge Runni |	10617 | 939 |


Para más información ver la bitácora [aquí](https://eafit.sharepoint.com/sites/Section_ST0263-031/_layouts/15/Doc.aspx?sourcedoc={4fb201e7-5fdd-47d7-94b6-35d07c449fe7}&action=view&wd=target%28Johanna%20Sarai%20Caicedo%20Mejia%2FBig%20Bata.one%7C05843a6d-7fe5-4e7a-9600-9b969322777c%2FHive%20caso%20de%20estudio%20%28Parte%202%5C%29%7Caed9fbfe-7f98-40be-85dd-756074581ef7%2F%29)
