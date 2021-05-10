En esta progrmación limpiaremos los datos de la tabla estraida como dataframe de pandas.

Adecuamos los nombres de las columnas para poder manipularlas con facilidad

Cambiamos las casillas vacías por na para facilitar el tratamiento

Borramos todas las filas con mas de 3 fallos

Usando set(df.Type) vemos en que columnas podemos cambiar na por unknown
Rellenamos por Unknown

Normalizamos la variable Sex

Normalizamos la variable Age

Normalizamos la variable Year

Normalizamos la variable Unnamed22 y 23

+Los rellenamos con 0 con los na

Normalizamos la variable Date
+Limpiamos la columna de typos
+Normalizamos la fecha
+Rellenamos na's con fillna con los métodos "bfill y ffill"

Rehacemos la variable Year con los datos de Date

Limpiamos la variable Country

Limpiamos las variables Country, Location, Area, Activity, Name e Injury

Limpiamos y normalizamos los datos de la columna Fatal
+Correjimos con replace las variables mal escritas
+Habiendo leido todas las palbras clave que prueban muerte en set(df.Injury[ind]), 
  las utilizamos para completar la columna fatal con información de Injury
+Cambiamos valores restantes con strings por False(asumimos que sobrevivieron)(son pocos datos)

Normalizamos la variable Time

Hacemos una lista de especies sacadas de la columna, y hacemos una columna nueva" shark_scpecies" 
con las especies limpias

Reacemos la columna Case_Number con un índice especial(hay una copia en Case_Number.2)

Hemos acabado con los na!













