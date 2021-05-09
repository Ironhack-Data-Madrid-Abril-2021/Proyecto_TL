# TL Project

  

## Introduction

On this project, we are going to focus on the transformation and load of an specific dataframe. After that, we will be able to analyze data and get insights about shark attacks around the world in past years.

You can find 3 main archives in my repo:

 - The TL Project_final.py Python file. Were you can find the clean code.
 - De Playground.ipyb, a Jupyter notebook where you can see how data was cleaned and the checks where made in the process.
 - The .sql docs where you can see the queries I used to upload the clean set to SQL in order to get the insights.

  

## Instructions for the analyst - how data was modified

At first the database was a bit messy and full of nulls. These are the principal changes were made during the transformation and data cleaning process:

 - All the rows that had all their values at null, were deleted.
 - After that Df was reduced by deleting every row with les than 3 no-null values.
 - No columns were deleted during this aproach.
 - You can find null values in the columns with the value 'Unknown', with 3 exceptions: pdf column ('no pdf') and both href columns ('no link')



## Insights

 - Most of the attacks happen in summer, and there are less in winter time.
 - Attacks where registered mainly in USA and Australia
 - Shark attacks where mostly unprovoked, non fatal and affected to male. 
