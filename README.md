![alt text](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.lavozdegalicia.es%2Fnoticia%2Fsociedad%2F2020%2F08%2F16%2Fincreible-instantanea-salto-tiburon-blanco%2F00031597575314089587560.htm&psig=AOvVaw3jpNmvOtN9-YmMZ21dtp-o&ust=1620650688518000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLjRgbfQvPACFQAAAAAdAAAAABAD.jpg)



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