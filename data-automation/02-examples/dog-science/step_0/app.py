import pandas as pd
import collections

df = pd.read_csv('../data/20200306_hundehalter.csv')
#print(df.describe())
#print(df.loc[0:3, ['STADTKREIS', 'RASSE1']])

# Alter des Hundehalters
## Fragestellung wie ist die Altersdistribution der Hundehalter?

age_groups = df['ALTER'].value_counts()
#print(age_groups)

# Rasse
## Fragestellung: Lassen sich beliebte / seltene Rassen feststellen?
## Zusatzfrage: Wie ist die Datenqualität? Wo sind Limitationen zu finden

dog_breed = df['RASSE1'].value_counts()
#print(dog_breed)

# Geschlecht
##Fragestellung: Wie ist die Verteilung der Hundegeschlechter

dog_sex = df['GESCHLECHT'].value_counts()
#print(dog_sex)

# Farbe
## Fragestellung: Wie ist die Verteilung der Fellfarbe? Ist die Farbe relevant?

dog_color = df['HUNDEFARBE'].value_counts()
#print(dog_color)

# Alter des Hundes
## Fragestellung: Wie ist die Verteilung des Hundealters?

dog_age = df['GEBURTSJAHR_HUND'].value_counts() # Fehler 11 / 18 beachten
dog_age_dict = {}
current_year = 2021
for i, count in dog_age.items():
    if len(str(i)) > 3:
        dog_age_dict[current_year-i] = count

dog_age_dict = collections.OrderedDict(sorted(dog_age_dict.items(), key=lambda x: x[0])) # 1971 erklären
#print(dog_age_dict)


# Halter
## Fragestellung: Wer hat wievele Hunde? Gibt es besonders relevante Hundehalter?

dog_owner = df['HALTER_ID'].value_counts()
#print(dog_owner)
dog_owners_multiple_dogs = {}
count_single_dogs, count_multiple_dogs = 0, 0

for i, count in df['HALTER_ID'].value_counts().items():
    if count > 1:
        dog_owners_multiple_dogs[i] = count
        count_multiple_dogs += 1
    else:
        count_single_dogs += 1

#print(dog_owners_multiple_dogs)
#print(count_single_dogs)
#print(count_multiple_dogs)
#print(dog_owner.count())


# Wohnort
## Fragestellung: Gibt es besonders beliebte Gebiete für Hundehalter in Zürich? Welcher Kreis ist Favorit?

# Nach Kreis sortiert?
dog_owner_place = collections.OrderedDict(sorted(df['STADTKREIS'].value_counts().items(), key=lambda x: x[0]))
print(dog_owner_place)

# Nach Anz sortiert?
dog_owner_place_sorted = collections.OrderedDict(sorted(df['STADTKREIS'].value_counts().items(), key=lambda x: x[1], reverse=True))
print(dog_owner_place_sorted)