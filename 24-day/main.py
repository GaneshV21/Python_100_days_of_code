#open and close and read
with open("data.txt",mode='r') as data:
    new_data = data.read()
    print(new_data)
# output -- hello world

#write
with open("data.txt", mode='w') as data:
    data.write("Hi Ganesh")

# output --Hi Ganesh


#relative and absolute path

#relative --  ../talk.ppt

#absolute -- /work/project/talk.ppt

#access the file using this paths

#absolute path:

with open("C:/Users/zcsu028/Desktop/api's.txt",mode='r') as data:
    new_data = data.read()
    print(new_data)

#relative path:
with open("../../../api's.txt",mode='r') as data:
    new_data = data.read()
    print(new_data)

