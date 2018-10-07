


import pandas


event_path = "athlete_events.csv"
region_path = "noc_regions.csv"


event_data = pandas.read_csv(event_path)


### q1
event_data_1996 = event_data[event_data['Year'].isin([1996])]

# print(event_data.dtypes)

event_data_1996_m = event_data_1996[event_data_1996['Sex'].isin(['M', 'm'])]
event_data_1996_f = event_data_1996[event_data_1996['Sex'].isin(['F', 'f'])]

print("answer 1")
print(event_data_1996_m.sort_values(by='Age', ascending=True).head(1)['Age'])
print(event_data_1996_f.sort_values(by='Age', ascending=True).head(1)['Age'])


### q2
event_data_2000 = event_data[event_data['Year'].isin([2000])]

event_data_2000_m = event_data_2000[event_data_2000['Sex'].isin(['M', 'm'])]
event_data_2000_m_gymnasts = event_data_2000_m[event_data_2000_m['Sport'].isin(['Gymnastics'])]

print("answer 2")
print(len(set(event_data_2000_m_gymnasts['Name'].values)) / len(set(event_data_2000_m['Name'].values)))
# print(len(set(event_data_2000_m_gymnasts['Name'].values)))
# print(len(set(event_data_2000_m['Name'].values)))


### q3
event_data_2000 = event_data[event_data['Year'].isin([2000])]

event_data_2000_f = event_data_2000[event_data_2000['Sex'].isin(['F', 'f'])]
event_data_2000_f_bascketball = event_data_2000_f[event_data_2000_f['Sport'].isin(['Basketball'])]

print("answer 3")
print(event_data_2000_f_bascketball['Height'].describe())


### q4
event_data_2002 = event_data[event_data['Year'].isin([2002])]

print("answer 4")
# print(event_data_2002.sort_values(by='Weight', ascending=False).head(1))
print(event_data_2002.sort_values(by='Weight', ascending=False).head(1)['Sport'])


### q5
answer5 = event_data[event_data['Name'].isin(['Pawe Abratkiewicz'])]

print("answer 5")
print(list(set(answer5['Year'].values)))
print(len(set(answer5['Year'].values)))


### q6
event_data_2000 = event_data[event_data['Year'].isin([2000])]

event_data_2000_tennis = event_data_2000[event_data_2000['Sport'].isin(['Tennis'])]
event_data_2000_tennis_silver = event_data_2000_tennis[event_data_2000_tennis['Medal'].isin(['Silver'])]
# print(list(event_data_2000_tennis_silver.values))
event_data_2000_tennis_silver_australia = event_data_2000_tennis_silver[event_data_2000_tennis_silver['Team'].isin(['Australia'])]

print("answer 6")
print(len(list(event_data_2000_tennis_silver_australia.values)))


### q7
event_data_2016 = event_data[event_data['Year'].isin([2016])]

event_data_2016_Switzerland = event_data_2016[event_data_2016['Team'].isin(['Switzerland'])]
event_data_2016_Serbia = event_data_2016[event_data_2016['Team'].isin(['Serbia'])]

event_data_2016_Switzerland_medals = event_data_2016_Switzerland[event_data_2016_Switzerland['Medal'].isin(['Silver', 'Bronze', 'Gold'])]
event_data_2016_Serbia_medals = event_data_2016_Serbia[event_data_2016_Serbia['Medal'].isin(['Silver', 'Bronze', 'Gold'])]

print("answer 7")
#print(set(event_data_2016['Medal'].values))
print(len(list(event_data_2016_Switzerland_medals.values)))
# print((list(event_data_2016_Switzerland_medals.values)))
print(len(list(event_data_2016_Serbia_medals.values)))
# print((list(event_data_2016_Serbia_medals.values)))


### q8
event_data_2014 = event_data[event_data['Year'].isin([2014])]

age_15_25 = list(range(15, 24))
age_25_35 = list(range(25, 34))
age_35_45 = list(range(35, 44))
age_45_55 = list(range(45, 55))

event_data_2014_15_25 = event_data_2014[event_data_2014['Age'].isin(age_15_25)]
event_data_2014_25_35 = event_data_2014[event_data_2014['Age'].isin(age_25_35)]
event_data_2014_35_45 = event_data_2014[event_data_2014['Age'].isin(age_35_45)]
event_data_2014_45_55 = event_data_2014[event_data_2014['Age'].isin(age_45_55)]


print("answer 8")
print(len(set(event_data_2014_15_25['Name'].values)))
print(len(set(event_data_2014_25_35['Name'].values)))
print(len(set(event_data_2014_35_45['Name'].values)))
print(len(set(event_data_2014_45_55['Name'].values)))


### q9

event_data_summer = event_data[event_data.Season == 'Summer']
event_data_winter = event_data[event_data.Season == 'Winter']
print("answer 9")
print(len(list(event_data_summer[event_data_summer.City == 'Lake Placid'].values)) > 0)
print(len(list(event_data_winter[event_data_winter.City == 'Sankt Moritz'].values)) > 0)


### q10
event_data_2016 = event_data[event_data['Year'].isin([2016])]
event_data_1995 = event_data[event_data['Year'].isin([1995])]


event_data_2016_sports = set(event_data_2016['Sport'].values)
event_data_1995_sports = set(event_data_1995['Sport'].values)

print("answer 10")
# print(event_data_2016_sports)
# print(event_data_1995_sports)
print(len(event_data_2016_sports) - len(event_data_1995_sports))