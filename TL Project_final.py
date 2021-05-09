import pandas as pd

df = pd.read_csv("/Users/mikel/Documents/week2/Proyecto_TL/attacks.csv", encoding="ISO-8859-1")
# Delete all the full null rows.
df = df.dropna(how='all', axis=0)
# Update: I will reduce de DF deleting every row with les than 3 no-null values
df = df.dropna(0, thresh=3)
# Column names change
df = df.rename(columns={'Unnamed: 22': 'unnamed22', 'Unnamed: 23': 'unnamed23', 'Fatal (Y/N)': 'Fatal',
                        'original order': 'original_order', 'Species': 'sharks', 'Case Number': 'Case_number',
                        'Investigator or Source': 'Investigator', 'href formula': 'href_formula',
                        'Case Number.1': 'Case_n1', 'Case Number.2': 'Case_n2', 'Sex ': 'Sex', 'Species ': 'Species',
                        'Fatal(Y/N)': 'Fatal'})

##Date Column

# Store the values in a new column as a backup
df['_original_date'] = df.Date
# Basic cleaning
df['_original_date_pre_treated'] = \
    df._original_date \
        .apply(
                lambda x :
                    str(x)
                        .replace('Reported ', '')
                        .replace('Early ',    '')
                        .replace('Late ',     '')
                        .replace('--',        '-')
            )
# Using the pandas to_datetime formula and de coerce will make the changes
df.Date = pd.to_datetime(df._original_date_pre_treated, errors='coerce')

# Decades
df.decade = df.Date.apply(lambda x : x.year - x.year % 10)

# Delete unnecessary columns and fill the nulls
df=df.drop('_original_date_pre_treated', axis=1)
df=df.drop('_original_date', axis=1)
df['Date'] = df['Date'].fillna('Unknown')


##Year Column

df.Year=df.Year.apply(lambda x: 'Unknown' if x <1000 else x)
df['Year'] = df['Year'].fillna('unknown')
df.Year=df.Year.astype(dtype='str')
df['Year'] = df['Year'].str.rstrip('.0')

##Type Column

df['Type'] = df['Type'].fillna('Unknown')
df.Type=df.Type.replace(to_replace =("Boatomg"), value ="Boat")

##Country Column

df['Country'] = df['Country'].str.capitalize()
df['Country'] = df['Country'].str.rstrip('?')
df['Country'] = df['Country'].fillna('Unknown')

##Area Column

df['Area'] = df['Area'].fillna('Unknown')

##Location Column

df['Location'] = df['Location'].fillna('Unknown')
df.Location=df.Location.astype(dtype='str')

##Activity Column

df['Activity'] = df['Activity'].fillna('Unknown')
df.loc[df['Activity'].str.contains('\wwimming', regex=True, case=False), 'Activity'] = 'Swimming'
df.loc[df['Activity'].str.contains('\wurf', regex=True, case=False), 'Activity'] = 'Surfing'
df.loc[df['Activity'].str.contains('\wiv', regex=True, case=False), 'Activity'] = 'Diving'
df.loc[df['Activity'].str.contains('\wish', regex=True, case=False), 'Activity'] = 'Fishing'

# Mark the rest as unknown
activity_lst = ['Swimming','Surfing', 'Diving', 'Fishing']
df.Activity=df.Activity.apply(lambda x: 'Unknown' if x not in activity_lst else x)

##Name Column

df.Name=df.Name.replace(to_replace =["male", "female"], value ="Unknown")
df['Name'] = df['Name'].fillna('Unknown')

##Sex Column

df['Sex'] = df['Sex'].fillna('Unknown')
df.Sex=df.Sex.replace(to_replace =("M "), value ="M")
df.Sex=df.Sex.replace(to_replace =("N"), value ="M")
df.Sex=df.Sex.replace(to_replace =("lli"), value ="M")
df.Sex=df.Sex.replace(to_replace =("."), value ="Unknown")

##Age Column

df['Age'] = df['Age'].fillna('Unknown')

for i in df.Age:
    if i.endswith('s'):
        df['Age'] = df['Age'].str.rstrip('.s')
    else:
        pass

df.loc[df['Age'].str.contains('\[a-z]+', regex=True, case=False), 'Age'] = 'Unknown'

##Injury Column

df['Injury'] = df['Injury'].fillna('Unknown')
df.loc[df['Injury'].str.contains('\wo injury', regex=True, case=False), 'Injury'] = 'No injury'
df.Injury=df.Injury.apply(lambda x: 'FATAL' if x.startswith(('Death', 'Dead')) else x)
df.loc[df['Injury'].str.contains('\wrm', regex=True, case=False), 'Injury'] = 'Arm injury'
df.loc[df['Injury'].str.contains('\woot', regex=True, case=False), 'Injury'] = 'Leg injury'
df.loc[df['Injury'].str.contains('\weg', regex=True, case=False), 'Injury'] = 'Leg injury'
df.loc[df['Injury'].str.contains('\wand', regex=True, case=False), 'Injury'] = 'Arm injury'
df.loc[df['Injury'].str.contains('\watal', regex=True, case=False), 'Injury'] = 'FATAL'
df.loc[df['Injury'].str.contains('\wit', regex=True, case=False), 'Injury'] = 'Bitten'
df.loc[df['Injury'].str.contains('\wuncture', regex=True, case=False), 'Injury'] = 'Puncture'
df.loc[df['Injury'].str.contains('\waceration', regex=True, case=False), 'Injury'] = 'Laceration'
df.loc[df['Injury'].str.contains('\winor', regex=True, case=False), 'Injury'] = 'Minor Injuries'

# Mark the rest as Unknown
injury_lst = ['Unknown', 'Arm injury', 'No injury', 'Leg injury', 'Laceration', 'Minor Injuries', 'Puncture', 'Bitten', 'FATAL']
df.Injury=df.Injury.apply(lambda x: 'Unknown' if x not in injury_lst else x)

##Fatal Column

df['Fatal'] = df['Fatal'].fillna('Unknown')

df.Fatal=df.Fatal.replace(to_replace =(" N"), value ="N")
df.Fatal=df.Fatal.replace(to_replace =("N "), value ="N")
df.Fatal=df.Fatal.replace(to_replace =("y"), value ="Y")
df.Fatal=df.Fatal.replace(to_replace =("UNKNOWN"), value ="Unknown")
df.Fatal=df.Fatal.replace(to_replace =("M"), value ="Unknown")
df.Fatal=df.Fatal.replace(to_replace =("2017"), value ="Unknown")

##Time Column

df['Time'] = df['Time'].fillna('Unknown')

# Group all the values by Morning, Afternoon, Evening and Night
df.Time=df.Time.apply(lambda x: 'Morning' if x.startswith('06') else x)
df.Time=df.Time.apply(lambda x: 'Morning' if x.startswith('07') else x)
df.Time=df.Time.apply(lambda x: 'Morning' if x.startswith('08') else x)
df.Time=df.Time.apply(lambda x: 'Morning' if x.startswith('8') else x)
df.Time=df.Time.apply(lambda x: 'Morning' if x.startswith('09') else x)
df.Time=df.Time.apply(lambda x: 'Morning' if x.startswith('10') else x)
df.Time=df.Time.apply(lambda x: 'Morning' if x.startswith('11') else x)
df.Time=df.Time.apply(lambda x: 'Morning' if x.startswith('12') else x)
df.Time=df.Time.apply(lambda x: 'Afternoon' if x.startswith('13') else x)
df.Time=df.Time.apply(lambda x: 'Afternoon' if x.startswith('14') else x)
df.Time=df.Time.apply(lambda x: 'Afternoon' if x.startswith('15') else x)
df.Time=df.Time.apply(lambda x: 'Afternoon' if x.startswith('16') else x)
df.Time=df.Time.apply(lambda x: 'Afternoon' if x.startswith('17') else x)
df.Time=df.Time.apply(lambda x: 'Evening' if x.startswith('18') else x)
df.Time=df.Time.apply(lambda x: 'Evening' if x.startswith('19') else x)
df.Time=df.Time.apply(lambda x: 'Evening' if x.startswith('20') else x)
df.Time=df.Time.apply(lambda x: 'Evening' if x.startswith('21') else x)
df.Time=df.Time.apply(lambda x: 'Night' if x.startswith('22') else x)
df.Time=df.Time.apply(lambda x: 'Night' if x.startswith('23') else x)
df.Time=df.Time.apply(lambda x: 'Night' if x.startswith('0') else x)

# The try to group the rest non numeric values
df.loc[df['Time'].str.contains('\wrning', regex=True, case=False), 'Time'] = 'Morning'
df.loc[df['Time'].str.contains('\wfternoon', regex=True, case=False), 'Time'] = 'Afternoon'
df.loc[df['Time'].str.contains('\wvening', regex=True, case=False), 'Time'] = 'Evening'
df.loc[df['Time'].str.contains('\wight', regex=True, case=False), 'Time'] = 'Night'
df.loc[df['Time'].str.contains('\woon', regex=True, case=False), 'Time'] = 'Afternoon'
df.Time=df.Time.apply(lambda x: 'Morning' if x.startswith('Early morning') else x)
df.Time=df.Time.apply(lambda x: 'Afternoon' if x.startswith('Early afternoon') else x)

# Mark the rest as unknown
day_lst = ['Morning', 'Afternoon', 'Evening', 'Night', 'Unknown']
df.Time=df.Time.apply(lambda x: 'Afternoon' if x.startswith('Early afternoon') else x)
df.Time=df.Time.apply(lambda x: 'Unknown' if x not in day_lst else x)

##Species Column
df['Species'] = df['Species'].fillna('Unknown')

# First of all separate for principal shark races
df.loc[df['Species'].str.contains('\white', regex=True, case=False), 'Species'] = 'White shark'
df.loc[df['Species'].str.contains('\wull', regex=True, case=False), 'Species'] = 'Bull shark'
df.loc[df['Species'].str.contains('\witer', regex=True, case=False), 'Species'] = 'Tiger shark'
df.loc[df['Species'].str.contains('\rey', regex=True, case=False), 'Species'] = 'Grey shark'
df.loc[df['Species'].str.contains('\wurse', regex=True, case=False), 'Species'] = 'Nurse shark'

# Then for size
df.loc[df['Species'].str.contains('\warge', regex=True, case=False), 'Species'] = 'Undifined Large shark'
df.loc[df['Species'].str.contains('\wmall', regex=True, case=False), 'Species'] = 'Undifined Small shark'

# Mark the rest as unknown
shark_lst= ['White shark', 'Bull shark', 'Tiger shark', 'Grey shark', 'Nurse shark', 'Undifined Large shark', 'Undifined Small shark']
df.Species=df.Species.apply(lambda x: 'Unknown' if x not in shark_lst else x)

##Investigator Column
df['Investigator'] = df['Investigator'].fillna('Unknown')

##PDF and Href Columns
df['pdf'] = df['pdf'].fillna('No pdf')
df['href_formula'] = df['href_formula'].fillna('No link')
df['href'] = df['href'].fillna('No link')

##Case1 and Case 2 columns

for i in df.Case_n1:
    if i.endswith('a'):
        df['Case_n1'] = df['Case_n1'].str.rstrip('.a')
    elif i.endswith('b'):
        df['Case_n1'] = df['Case_n1'].str.rstrip('.b')
    elif i.endswith('c'):
        df['Case_n1'] = df['Case_n1'].str.rstrip('.c')
    elif i.endswith('d'):
        df['Case_n1'] = df['Case_n1'].str.rstrip('.d')
    elif i.endswith('R'):
        df['Case_n1'] = df['Case_n1'].str.rstrip('.R')
    else:
        pass
for i in df.Case_n1:
    if i.endswith('a'):
        df['Case_n2'] = df['Case_n2'].str.rstrip('.a')
    elif i.endswith('b'):
        df['Case_n2'] = df['Case_n2'].str.rstrip('.b')
    elif i.endswith('c'):
        df['Case_n2'] = df['Case_n2'].str.rstrip('.c')
    elif i.endswith('d'):
        df['Case_n2'] = df['Case_n2'].str.rstrip('.d')
    elif i.endswith('R'):
        df['Case_n2'] = df['Case_n2'].str.rstrip('.R')
    else:
        pass

##Unnamed and case number Columns
df['unnamed22'] = df['unnamed22'].fillna('unknown')
df['unnamed23'] = df['unnamed23'].fillna('unknown')
df['Case_number'] = df['Case_number'].fillna('unknown')


# Export comma-separated variable file
df = df.to_csv('/Users/mikel/Documents/week2/Proyecto_TL/attacks.csv', index=False)






