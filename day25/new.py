import csv
import pandas as pd

with open('day25/weather_data.csv') as file:
    data = file.readlines()

print(data)

with open('day25/weather_data.csv') as file:
    data = csv.reader(file)
    temp = []
    for row in data:
        if row[1] != 'temp':
            row[1] = int(row[1])
        temp.append(row)
print(temp)

data = pd.read_csv('day25/weather_data.csv')
print(data)
print(data['temp'])
print(type(data))
print(type(data['temp']))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

ave_temp =sum(temp_list)/len(temp_list)
print(ave_temp)

print(data['temp'].mean())
print(data['temp'].max())

print(data['condition'])
print(data.condition)

print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
temp_max = monday.temp 
temp_max_f = temp_max * 9/5 + 32
print(temp_max_f)

dict_data = {'Name' : ['John', 'Jack', 'Jill'],
             'Age' : [23, 34, 45]}

data = pd.DataFrame(dict_data)
print(data)

data.to_csv('day25/new_data.csv')