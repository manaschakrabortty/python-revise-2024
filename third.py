#LIST AND TUPLES
# marks=[12,19,21,18]#list
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[2])
# students=["manas",21,"kolkata"]
# print(students)
#strings are immutable and list are mutable with an example
# students="manas,12,19"
# print(students[0])# it is possible in str
#students[0]="purbasa"#this is not possible in str
# students=["manas",12,19]
# print(students[0])
# students[0]="purbasa"
# print(students)

#LIST SLICING
# m=[34,65,32,98,67]
# print(m[1:4])
# print(m[:4])
# print(m[1:])
# print(m[-3:-1])
#LIST METHODS
# list=[1,2,3,4,5]
# # list.append(9)#add 9 in last
# # list.sort()#small to big. SORTING 1) ACCENDING{ SMALL TO BIG 1.2.3} 2) DISCENDING {BIG TO SMALL 3.2.1}
# # list.sort(reverse=True)#sort in decending order [3.2.1]
# # list.reverse()
# # list.insert(0,7)
# list.remove(3)#remove first ocurrence of element.
# list.pop(4)#removes element at idx.
# print(list)

#TUPLES
#are immutable like strings

# tup=(2,1,4,7,8,9,7,)
# # print(tup[0])
# # print(tup[3])
# # tup[0]=3# this is not allowed in tuple immutable.
# # tup1=(1,)#we create a comma either else it loks like int,either floar or some thing 
# print(tup[1:3])
# print(type(tup))
#METHODS
# tup8=(2,5,7,1,9,1,)
# print(tup8.index(1))
# print(tup8.count(1))



#HOME WORK
# 1) WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVOURITES MOVES & STORE THEM IN ALIST?
# a=input("ENTER YOUR FIRST MOVEY:- ")
# b=input("ENTER YOUR SECOND MOVEY :- ")
# c=input("ENTER YOUR THIRD MOVEY:= ")
# d=[a,b,c]
# print(d)
# print(type(d))

# movies=[]
# a=input("ENTER YOUR FIRST MOVEY:- ")
# b=input("ENTER YOUR SECOND MOVEY :- ")
# c=input("ENTER YOUR THIRD MOVEY:= ")
# movies.append(a)
# movies.append(b)
# movies.append(c)
# print(movies)


#2)WAP TO CHECK IF ALIST CONTAINS A PALINDROME OF ELEMENTS .(USE copy()method)

# # list1=["m","a","a","m"]
# copy_list1 = list1.copy()
# copy_list1.reverse()
# if(copy_list1==list1):
#     print("PALINDROME")
# else:
#     print("not palindrome")



#3) WAP TO COUNT THE NUMBER OF ASRUDENTS WITH THE "A " GRADE IN THE FOLLOEING tuple
# ["C","D","A","A","B","C","A","B","A"]
#NEXT QUESTION 
# STORE THE ABOVE VALUES IN A LIST & SORT THEM "A" TO "D". [ ACENDING ORDER]
#1.
# grade= ("C","D","A","A","B","C","A","B","A")
# print(grade.count("A")
#. anas
grade=["C","D","A","A","B","C","A","B","A"]
grade.sort()
print(grade)












