# numbers=[1,2,3,4,5]
# ne_list=[n+1 for n in numbers ]
# print(ne_list) #--  [2,3,4,5,6]

# name="Ganesh"
# ne_list=[n for n in name ]
# print(ne_list) # --  ['G','a','n','e','s','h']

# range_list=[item*2 for item in range(1,5)]
# print(range_list) # -- [2, 4, 6, 8]

#conditional list comprehension
# names=['Alex','Beth','Caroline','Dave','Elanor','Freddie','Ganesh']
# long_name=[name.upper() for name in names if len(name)>5]
# print(long_name) # -- ['CAROLINE', 'ELANOR', 'FREDDIE', 'GANESH']


#apply list comprehension to us-states game -25 day

#Dictionary comprehension
# import random
# namess=['Alex','Beth','Caroline','Ganesh']
# student_score={name:random.randint(0,100) for name in namess}
# print(student_score)
#
# passed_student = {key:value for (key,value) in student_score.items() if value>=60}
# print(passed_student)


#loop through a dataframe
# import pandas
# student_dict={"student":['Angela','James','Liy'],"score":[56,76,98]}
# student_data_frame=pandas.DataFrame(student_dict)
# for (key,value) in student_data_frame.items():
#     print(value)

# for (index,row) in student_data_frame.iterrows():  #-- loop through each row
#     print(row)