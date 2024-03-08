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
