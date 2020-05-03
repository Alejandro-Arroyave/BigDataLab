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

Para más información ver la bitácora [aquí](https://eafit.sharepoint.com/sites/Section_ST0263-031/_layouts/15/Doc.aspx?sourcedoc={4fb201e7-5fdd-47d7-94b6-35d07c449fe7}&action=view&wd=target%28Johanna%20Sarai%20Caicedo%20Mejia%2FBig%20Bata.one%7C05843a6d-7fe5-4e7a-9600-9b969322777c%2FHive%20caso%20de%20estudio%20%28Parte%202%5C%29%7Caed9fbfe-7f98-40be-85dd-756074581ef7%2F%29)
