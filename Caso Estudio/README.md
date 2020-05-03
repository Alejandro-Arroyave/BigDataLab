# Caso de estudio retail_db

Creación de base de datos con configuraciones en [retail_db-ddl.sql](https://github.com/jscaicedom/BigDataLab/blob/master/bigdata/rdbms/retail_db-ddl.sql) y [retail_db-data.sql](https://github.com/jscaicedom/BigDataLab/blob/master/bigdata/rdbms/retail_db-data.sql)

En la instancia Ec2 

```
$ sudo yum install git
$ git clone https://github.com/jscaicedom/BigDataLab.git
$ mysql -u admin -p -h database.cy5rftlokiyu.us-east-1.rds.amazonaws.com retail_db < BigDataLab/bigdata/rdbms/retail_db-data.sql
```