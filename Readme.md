1.	Limpiar nombre de columnas con métodos de string (lstrip.lower.rstrip,replace) y cambiar algunos nombres que SQL los tenía guardado como palabras reservadas.
2.	Eliminar filas 100% duplicadas
3.	Eliminar filas que tenían mas de 60% de los valores vacíos.
4.	Eliminar registros más antiguos que 1970.
5.	Columna Casenumber, comprobar que no haya registros duplicados. Había 9 duplicados, tras revisar 1 y ver que efectivamente era un duplicado he tomado la decisión de eliminar los duplicados.
6.	Columna year, cambiado el formato a year e incluido la fecha de dos registros que no lo tenían usando los datos de la columna date.
7.	Columna date, primero cambiado la columna a str, he limpiado los datos con métodos de string y al final convertido las fechas a mesas, al final todas las fechas se han convertido en meses.  (ESTA COLUMNA ES LA QUE MAS PROBLEMAS ME HA DADO)
8.	Type con métodos de string los he clasificado en 5 categorías.
9.	Counrty los he convertido por continentes y océanos con métodos de string y una función (SE QUE hay una librería de países, pero no he sido capaz de usarlo)
10.	Sexo he unificado los valores en femenino, masculino y desconocido.
11.	Edad, he convertido la columna en str, atreves de métodos de string y función he categorizado las edades en 5 rangos.
12.	Fatal, categorizado en 3 variantes mediante str
13.	Time, convertido en str y con una función categorizado en mañana, mediodía, tarde, noche.
14.	Species con str.contains he categorizado los que me ha dado tiempo, pero se puede mejorar bastante.
15.	Resto he reemplazado los valores NAN por unknown , 0, notapply dependiendo de cada caso.
16.	Después he hecho CSV.
17.	He creado base de datos en SQL
18.	He definido los valores de la tabla, pero al importar el CSV me daba error.
19.	No he podido detectar el error y lo he tenido que importar como una tabla nueva.

