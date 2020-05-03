# Laboratorio de Big Data

## 1. HDFS
Para más información ver la bitácora [aquí](https://eafit.sharepoint.com/sites/Section_ST0263-031/_layouts/15/Doc.aspx?sourcedoc={4fb201e7-5fdd-47d7-94b6-35d07c449fe7}&action=view&wd=target%28Johanna%20Sarai%20Caicedo%20Mejia%2FBig%20Bata.one%7C05843a6d-7fe5-4e7a-9600-9b969322777c%2FHDFS%7C5c86107a-6758-4820-b09a-467497c53ac0%2F%29)

## 2. MapReduce

- Wordcount local 
      Ejecutar el archivo [wordcount-local.py](https://github.com/jscaicedom/BigDataLab/blob/master/bigdata/02-mapreduce/wordcount-local.py)

```
$ cd bigdata/02-mapreduce/
$ python wordcount-local.py ../datasets/gutenberg-small/*.txt > ../../MapReduce/outlocal.txt
```
 
   [Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outlocal.txt)

- Wordcount con MRjob

```
$ cd bigdata/02-mapreduce/
$ python wordcount-mr.py -r local ../datasets/gutenberg-small/*.txt > ../../MapReduce/outmrjob.txt
```

   [Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outmrjob.txt)

- Ejercicio escogido (Primer ejercicio)

  Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

   - El salario promedio por Sector Económico (SE)
      
  ```
  $ cd MapReduce/
  $ python Punto1-Salario.py ../bigdata/datasets/otros/dataempleados.csv > outpunto1.txt 
  ```    
  
     [Código](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/Punto1-Salario.py)
    
     [Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outpunto1.txt)

   - El salario promedio por Empleado
      
  ```
  $ cd MapReduce/
  $ python Punto2-Salario.py ../bigdata/datasets/otros/dataempleados.csv > outpunto2.txt 
  ```    
  
     [Código](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/Punto2-Salario.py)
    
     [Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outpunto2.txt)
     
   - Número de SE por Empleado que ha tenido a lo largo de la estadística
      
  ```
  $ cd MapReduce/
  $ python Punto3-Salario.py ../bigdata/datasets/otros/dataempleados.csv > outpunto3.txt 
  ```    
  
     [Código](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/Punto3-Salario.py)
    
     [Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outpunto3.txt)
     

Para ver la evidencia ir a la bitácora [aquí](https://eafit.sharepoint.com/sites/Section_ST0263-031/_layouts/15/Doc.aspx?sourcedoc={4fb201e7-5fdd-47d7-94b6-35d07c449fe7}&action=view&wd=target%28Johanna%20Sarai%20Caicedo%20Mejia%2FBig%20Bata.one%7C05843a6d-7fe5-4e7a-9600-9b969322777c%2FMapReduce%7C307fa2f4-c419-465a-88ec-8f275860919b%2F%29)

## 3. Hive y Sqoop (Parte 1)
Para más información ver la bitácora [aquí](https://eafit.sharepoint.com/sites/Section_ST0263-031/_layouts/15/Doc.aspx?sourcedoc={4fb201e7-5fdd-47d7-94b6-35d07c449fe7}&action=view&wd=target%28Johanna%20Sarai%20Caicedo%20Mejia%2FBig%20Bata.one%7C05843a6d-7fe5-4e7a-9600-9b969322777c%2FHive%C2%A0%28Parte%201%5C%29%7C014c2eb7-3185-43c7-98b3-8a0eea075bfb%2F%29)

## 3. Hive Caso de estudio Retail (Parte2)
Para más información ver la bitácora [aquí](https://eafit.sharepoint.com/sites/Section_ST0263-031/_layouts/15/Doc.aspx?sourcedoc={4fb201e7-5fdd-47d7-94b6-35d07c449fe7}&action=view&wd=target%28Johanna%20Sarai%20Caicedo%20Mejia%2FBig%20Bata.one%7C05843a6d-7fe5-4e7a-9600-9b969322777c%2FHive%20caso%20de%20estudio%20%28Parte%202%5C%29%7Caed9fbfe-7f98-40be-85dd-756074581ef7%2F%29)

## 4. Spark
Para más información ver la bitácora [aquí](https://eafit.sharepoint.com/sites/Section_ST0263-031/_layouts/15/Doc.aspx?sourcedoc={4fb201e7-5fdd-47d7-94b6-35d07c449fe7}&action=view&wd=target%28Johanna%20Sarai%20Caicedo%20Mejia%2FBig%20Bata.one%7C05843a6d-7fe5-4e7a-9600-9b969322777c%2FSpark%7Cd99a385e-4b98-4985-9e1d-e7e0d97a1856%2F%29)
