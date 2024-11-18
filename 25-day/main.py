# with open('./weather_data.csv') as weather:
#     data=weather.readlines()
#     print(data)

# import csv
# with open('./weather_data.csv') as weather:
#     data=csv.reader(weather)
#     temperature=[]
#     for row in data:
#         if row[1]!='temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
# data=pandas.read_csv("./weather_data.csv")
# print(data)
# print(type(data)) # -- pandas.core.frame.DataFrame
# print(data['temp'])
# print(type(data['temp'])) # -- pandas.core.series.Series

# read about Dataframe and series in Pandas Documentation

# data_dict=data.to_dict() #-- dataframe
# print(data_dict)
#
# temp_list=data['temp'].to_list() #--Series
# print(temp_list)

# using series functionality
# find average temperature
# average_temp=(sum(temp_list)/len(temp_list))
# print(average_temp)
# print(data['temp'].mean()) # -- for average

# print(data['temp'].max()) # -- max value form list

#Get data in columns
# print(data['temp'])
# print(data.temp)

#Get data in row
# print(data[data.day=='Monday'])
# print(data[data.temp==data['temp'].max()])

# monday=data[data.day=='Monday']
# print(monday.temp) #-- 12

#create a dataframe from scratch
# data_dict={
#     "students":["Amy","James","Ganesh"],
#     "scores":[76,56,90]
# }
# data=pandas.DataFrame(data_dict)
# print(data)

#convert dataframes to csv
# data.to_csv("new_data.csv") # -- new_data.csv file is created and updated


# data=pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels_count=len(data[data['Primary Fur Color']=='Gray'])
# red_squirrels_count=len(data[data['Primary Fur Color']=='Cinnamon'])
# black_squirrels_count=len(data[data['Primary Fur Color']=='Black'])
#
# data_dicts={
#     "Primary Fur Color":['Gray','Cinnamon','Black'],
#     "Count":[gray_squirrels_count,red_squirrels_count,black_squirrels_count]
# }
# df=pandas.DataFrame(data_dicts)
# print(df)
# df.to_csv('./squirrel_count.csv')




