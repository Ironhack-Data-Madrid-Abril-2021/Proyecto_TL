load data local infile '/Users/mikel/Documents/week2/Proyecto_TL/attacks.csv' 
into table sharks 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
