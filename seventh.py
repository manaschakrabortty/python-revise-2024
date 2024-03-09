#FILE I/O
# TEXT FILE- .txt, .docx, .log
#Binary file- .mp4, .mov,.png,
# f=open("file_name","r/w")r=read,w=write.

# f=open("open.txt","r")
# # data= f.read()
# # data2= f.read(5)# it will print first of 5 char.
# # # print(data)
# # print(data2)
# line1=f.readline()#it wll printline 1 
# print(line1)
# f.close()
#C:\Users\manas\OneDrive\Desktop\PYTHON REVISE 2024\open.txt
#['r','w','x','a','b','t','+']mode 
# f=open("open.txt","w")
# f.write("i want to master in python from now 1234")
# f.close()

# f=open("open.txt","a")
# f.write("\n i want to master in js from now 1234")
# f.close()
# f=open("sample.txt","w")
# f.close()
#r+ =read + overwrite(pointer start)-NO TRUNCELT
#w+ = read + overwrite(pointer start)-TRUNCELT
#a+ = read+ append (pointer end)- no truncate

#WITH SYNTAX
# with open("demo.txt","r")as f:
#     data= f.read()
#     print(data)

#DELETING A FILE
# import os
# os.remove("file name")


#PRACTICE QUESTION
#1) CREATE A FILE "PRACTICE.TXT"USING PYTHON . ADD THE FOLLOWING DATA IN IT
# HI EVERYONE
# WE ARE LEARNING FILE I/O
# USING PYTHON
# I LIK3 PROGRAMMING IN PYTHON
# with open("practice.txt","w") as f:
#     f.write("HI EVERYONE\nWE ARE LEARNING FILE I/O\nUSING PYTHON\nI LIK3 PROGRAMMING IN PYTHON")
#) WAF THAT REPLACE ALL OCCURRENCES OF"Java"with"Python" in above file
# with open("practice.txt","r") as f:
#     data = f.read()
# new_data  = data.replace("python","java")
# print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)


#SEARCH IF THE WORD "learning" exists in the file or not?
# word="LEARNING"
# with open("practice.txt","r") as f:
#     data= f.read()
#     if (data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")
#USING FUNCTION
# def check_find():
#     word="LEARNING"
#     with open("practice.txt","r") as f:
#         data= f.read()
#         if (data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")
# check_find()

#WAF TO FIND IN WHICH LINE OF THE FILE DOES THE WORD "LEARNING" OCCUR FIRST
#PRINT -1 IF WORD NOT FOUND
# def check_find():
#     word="LEARNING"
#     with open("practice.txt","r") as f:
#         data= f.read()
#         if (data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")
# check_find()
# def check_found():
#     word="LEARNING"
#     data= True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1
# check_found()

#FROM A FILE CONTAINING NUMBERS SEPARATED BY COMMA, PRINT THE COUNT OF EVEN NUMBERS
count=0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)#1st individual number get 2nd parse/casting to int because it is string format

    nums=data.split(",")
    for val in nums:
        if(int(val)%2 ==0):
            count+=1
print(count)
