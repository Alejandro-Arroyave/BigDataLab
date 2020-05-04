# 2. MapReduce

## Wordcount local 
      
Ejecutar el archivo [wordcount-local.py](https://github.com/jscaicedom/BigDataLab/blob/master/bigdata/02-mapreduce/wordcount-local.py)

```
$ cd bigdata/02-mapreduce/
$ python wordcount-local.py ../datasets/gutenberg-small/*.txt > ../../MapReduce/outlocal.txt
```
 
[Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outlocal.txt)

## Wordcount con MRjob

Ejecutar el archivo [wordcount-mr.py](https://github.com/jscaicedom/BigDataLab/blob/master/bigdata/02-mapreduce/wordcount-mr.py)

```
$ cd bigdata/02-mapreduce/
$ python wordcount-mr.py -r local ../datasets/gutenberg-small/*.txt > ../../MapReduce/outmrjob.txt
```

[Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outmrjob.txt)

## Ejercicio escogido (Primer ejercicio)

Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

### El salario promedio por Sector Económico (SE)
      
  ```
  $ cd MapReduce/
  $ python Punto1-Salario.py ../bigdata/datasets/otros/dataempleados.csv > outpunto1.txt 
  ```    
  
[Código](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/Punto1-Salario.py)
    
[Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outpunto1.txt)

### El salario promedio por Empleado
      
  ```
  $ cd MapReduce/
  $ python Punto2-Salario.py ../bigdata/datasets/otros/dataempleados.csv > outpunto2.txt 
  ```    
  
[Código](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/Punto2-Salario.py)
    
[Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outpunto2.txt)
     
### Número de SE por Empleado que ha tenido a lo largo de la estadística
      
  ```
  $ cd MapReduce/
  $ python Punto3-Salario.py ../bigdata/datasets/otros/dataempleados.csv > outpunto3.txt 
  ```    
  
[Código](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/Punto3-Salario.py)
    
[Salida](https://github.com/jscaicedom/BigDataLab/blob/master/MapReduce/outpunto3.txt)
     
# EVIDENCIA

[PDF](https://github.com/jscaicedom/BigDataLab/blob/master/bitacoras/Lab2%20-%20MapReduce.pdf)

[LINK OneNote](https://eafit.sharepoint.com/sites/Section_ST0263-031/_layouts/15/Doc.aspx?sourcedoc={4fb201e7-5fdd-47d7-94b6-35d07c449fe7}&action=view&wd=target%28Johanna%20Sarai%20Caicedo%20Mejia%2FBig%20Bata.one%7C05843a6d-7fe5-4e7a-9600-9b969322777c%2FMapReduce%7C307fa2f4-c419-465a-88ec-8f275860919b%2F%29)

## [Volver](https://github.com/jscaicedom/BigDataLab)
