#LOOP 
#WHILE LOOP
# print("o hello")
# count=1
# while count <=5:
#     print("hello")
#     count+=1

# i=1
# while i<=5:
#     print("manas ",i)#i=iterator this is print the number
#     i+=1

#print 0-5 
# i=0
# while i<=10:
#     print(i)
#     i+=1

# #REVERSE
# i=9
# while i>=1:
#     print(i)
#     i-=1

#INFINITE LOOP
# i=5
# while i<6:
#     print(i)
#     i-=1


#PRACTICE IN WHILE LOOP
#1) PRINT NUMBERS FROM 1-100?
# i=1
# while i<=100:
#     print(i)
#     i+=1
#2) PRINTS NUMBERS FROM 100-1?
# i=100
# while i>=1:#THIS IS A STOPPING CONDITION
#     print(i)
#     i-=1

#3) PRINT THE MULTIPLICATION TABLE OF A NUMBER n
# i=1
# n=3#int(input("enter the number:> "))
# while i<=10:
#     print(n,i,n*i)#we can do (4*i)
#     i+=1

#3) PRINT THE ELEMENTS OF THE FOLLOWING LIST USING A LOOP?
#[1,4,9,16,25,36,49,64,81,100]
# num=[1,4,9,16,25,36,49,64,81,100]
# print(num[0])
# print(num[1])
# print(num[2])#...print(num[len(num-1)])#index
#op2
# idx= 0
# while idx < len(num):
#     # print(idx)
#     print(num[idx])#num[0],num[1],..
#     idx +=1
#q2
# heros=["ironman","batmAN", "THOR", "SUPERMAN", ]
# i=0
# while i <len(heros):
#     print(heros[i])#this is called travase mean its travel of an element
#     i+=1

#3) SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP?
#(1,4,9,16,25,36,49,64,81,100)
# num=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i<len(num):
#     if (num[i] == x):
#         print("FOUND AT INDEX ", i)
#     i+=1


#BREAK & CONTINUE
# i=1
# while i<=5:
#     print(i)
#     if(i== 3):#break in 3 number
#         break
#     i+=1

# i=0
# while i<=5:
#     if(i == 3):
#         i+=1
#         continue#skip
#     print(i)
#     i+=1
#ANOTHER
# i=0#ODD NUM PRINT
# while i<=10:
#     if(i%2==0 ):
#         i+=1
#         continue#skip
#     print(i)
#     i+=1
#EVEN NUM PRINT
# i=1
# while i<=10:
#     if(i%2!=0 ):
#         i+=1
#         continue#skip
#     print(i)
#     i+=1




#FOR LOOP 
# mans=[1,2,3,4,5,6,7]
# for i in mans:
#     print(i)

# mans=(1,2,3,4,5,6,7)
# for i in mans:
#     print(i)


#1) PRINT THE ELEMENT OF THE FOLLOWING LIST USING A LOOP
#[1,4,9,16,25,36,49,64,81,100]
# num=[1,4,9,16,25,36,49,64,81,100]
# for l in num:
#     print(l)


#3) SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP?
#(1,4,9,16,25,36,49,64,81,100,49)
# nums=(1,4,9,16,25,36,49,64,81,100,49)
# x=49
# i=0
# for  sd in  nums :
#     if (sd ==x):
#         print("number found ai idx ..", i)
#     i +=1
#RANGE 
#START,STOP, STEP
# for i in range(10):#range(stop)
#     print(i)
# for i in range(2,10):#range( start, stop)
#     print(i)
# for i in range(1,10,2):#range( start, stop , step)
#     print(i)


#printEVEN NUMBERS
# for i in range(2,100,2):
#     print(i)
#PRINT ODD NUMBERS
# for i in range(1,100,2):
#     print(i)

#print 100-1 for loop
# for i in range(100,0,-1):
#     print(i)

#print the multiplication table of n
# n =int(input("ENTER THE NUMBER? ::-- "))
# for i in range (1,11):
#     print(n*i)

#PASS STATEMENT
# for i in range (5):
#     #empty
# print("my manas")# through error

# solution
# for i in range (5):
#     pass
# print("my manas")

# if i>5:
#     pass

#q1
#1)WAP TO FIND THE SUM OF FIRST n NATURAL  NUMBERS. (USING WHILE)
# n=8
# sum=0
# for i in range(1,n+1):
#     sum += i
# print("number is " ,sum)
#while loop
# n=8
# sum=0
# i=1
# while i<=n:
#     sum += i
#     i += 1
# print("number is " ,sum)

#wap  to find the factorial of first n numbers.(using for)
# n=5
# fac=1
# for i in range(1,n+1):
#     fac *= i
# print("number is " ,fac)


#while
# n=3
# fac =1
# i=1
# while i<=n:
#     fac *= i
#     i+=1
# print("factorial= ", fac)



# for i in range(1,4,1):
#     for j in range()
#     print(i)    


# a=1
# for i in range(5):
#     print("*")
#     a=i+1
#     print(a)


# n=5
# for i in range(n):
#     for i in range(n-i-1):
#         print('',end='')
#     for k in range(2*i+1):
#         print("*",end='')
#     print()