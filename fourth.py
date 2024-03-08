#DICTIONARY

# info={
#     "key": "value",
#     "name" :"manas",
#     "learning": ["python","java","c++","js"],
#     "topics": ("dict","set"),
#     "age":23,
#     "is_adult":True,
#     "marks": 76.89
# }
# null_dict={}
# print(info["is_adult"])
# info["name"]="purbasa"
# info["surname "]="cahakrabortty"
# print(info)
# student={
#     "name":"manas chakrabortty",
#     "sub":{
#         "physics":98,
#         "math":99,
#     }
# }
# print(student)

# print(student["sub"]["physics"])

# student={
#     "name":"manas chakrabortty",
#     "sub":{
#         "physics":98,
#         "math":99,
#     }
# }
# new_dict={"name": "purbasa chakrabortty","age":19}
# student.update(new_dict)
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student["name3"])# if wrogn rhrough error
# print(student.get("name4"))# if wrogn no error= None


#SET
# colection={1,2,3,4,"hello","wow","wow"}
# print(colection)
# print(type(colection))
# print(len(colection))# length ignore duplicate value
# m={}# syntax same dict and set this is dict
# m=set()#empty set

# c=set()
# c.add(1)
# c.add(2)
# c.add(2)
# c.add("manas")
# c.clear()
# c.pop()
# c.remove(2)

# print(c)

# m={1,2,3,4}
# p={3,4,5,6,7}
# print(m.union(p))#return combine collection
# print(set(m))# original value
# print(m.intersection(p))



#HOME WORK
#1) WAP STORE FOLLOWING WORD MEANINGS IN APYTHON DICTIONARY:
# table :"a piece of furniture","list of facts &figures"
#cat:"a small animal"
# dictionary= {
#     "cat": "a small animal",
#     "table": ["a piece of furniture", "list of facts &figure"]# list form
# }
# print(dictionary)


#2) YOU ARE GIVENA LIST OF SUBJECTS FOR STUDENTS .ASSUME ONE CLASSROOM IS REQUIRED FOR 1 SUBJECT. HOW MANY CLASSSROOM ARE NEEDED BY ALL STUDENTS?
#"python","java","c++","python","javascript","java","python","java","c++","c"
# subject={
#     "python","java","c++","python","javascript","java","python","java","c++","c"
# }

# print(len(subject))

#3) WAP TO ENTER MARKS OF 3 SUBJECTS FROM THE USER AND STORE THEM IN A DICTIONARY. START WITH AN EMPTY DICTIONARY &ADD ONE BY ONE . USE SUBJECT NAME AS KEY & MARKS AS VALUE.
# marks={}
# x=int(input("enter phy: "))
# marks.update({"phy" :x})
# x=int(input("enter math: "))
# marks.update({"math" :x})
# x=int(input("enter chem: "))
# marks.update({"chem" :x})
# print(marks)

#4) FIGURE OUT A WAY TO STORE 9 &9.0 AS SEPARATE VALUES IN THE SET. HELP BUILT IN DATATYPES
# v={9,9.0}
# print(v)#python treat 9 and 9.0 as a same
# m={9,'9.0'}#9,0 as a string
# p={
#     ("float",9.0),
#     ("int",9)
# }
# print(p)