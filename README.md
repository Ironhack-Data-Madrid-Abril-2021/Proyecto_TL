![alt text](https://www.ngenespanol.com/wp-content/uploads/2018/08/%C2%BFPor-qu%C3%A9-disminuy%C3%B3-el-riesgo-de-ataques-de-tibur%C3%B3n.jpg)



Proyecto de Limpieza de datos de Sharks- Vicente Díaz Pliego


El proyecto consistía en dejar la base de datos lo más limpia posible. El requisito más complicado era hacerlo sin poder eliminar ninguna de las columnas.

El procedimiento ha sido muy tedioso, ya que he tenido que ir limpiado columna a columna todos los valores de la base de datos.

Es mi primera limpieza de datos, estoy seguro que muchos de los comandos utilizados podrían haber sido optimizados. Por desgracia, el tiempo para hacer el trabajo es limitado. Aún así, estoy bastante satisfecho con el resultado.


Una vez limpiado todos los valores NaN de las columnas y homogeneizar los tipos de datos, he creado un nuevo archivo .csv con la nueva base de datos optimizada.

En SQL Workbench, he exportado los datos generando una tabla única con la nueva base de datos shark_clean.csv 

Por desgracia, no he conseguido que se visualicen los datos de las filas. No me genera ningún error, simplemente no se visualizan las filas. Sin embargo, las columnas si.


Una vez acabado con este proceso, he realizado un estudio con dos hipotesis:

1 Hipotesis : ¿Qué franja horaria es más probable que se produzca un ataque de tiburón?

Resultado de la hipótesis: el número de ataques que se produce por la tarde, es ligeramente superior a los de por la mañana.

Los ataques de tiburones nocturnos no son espeacialmente numerosos.

2 Hipótesis : ¿De cada ataque que se produce, cuántos ataques son fatales?

Resultado de la hipótesis: El gráfico nos muestra que, afortunadamente, los ataques que se producen de tiburones a seres humanos son en su mayoría no letales.


Siendo realistas, aún me queda mucho que aprender en la analítica de datos. Esto es solo el comienzo.