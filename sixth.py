# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# cal_sum(12,12)
# cal_sum(12,19)
# cal_sum(18,19)
#we use function because to decrese redundansy of our code.

#FUNCTION DEFINITION
# def cal_sum(a,b):#a,b  ARE PARAMETERS
#     return a+b

# #FUNCTION CLL
# sum=cal_sum(1,4)#1,4 ARE FUNCTION ARUMENTS
# print(sum)

#AVERAGE OF 3 NUMBRS
# def avg_num(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# avg_num(12,32,45)

#DEFAULT PARAMETERS

# def cal_prod(a,b):
#     print(a*b)
#     return a*b
# cal_prod()

# def cal_prod(a,b=1):
#     print(a*b)
#     return a*b
# cal_prod(1)

#HW

#WAF  TO PRINT THE LENGTH OF A LIST (LIST IS A PARAMETER)
# cities=["kolkata","kgp","delli","beng"]
# herose=["virat","rohit","gill","siraj"]
# def print_len(list):
#     print(len(list))
# print(len(cities))
# print(len(herose))



#WAF TO PRINT THE ELEMENTS OF A LIST IN ASINGLE LINE(LIST IS THE PARAMETER)
# cities=["kolkata","kgp","delli","beng"]
# herose=["virat","rohit","gill","siraj"]
# def ele_he(list):
#     for item in list:
#         print(item,end=" ")
# ele_he(herose)

#WAF TO FIND THE FACTORIAL OF n.(nis the parameter)
#n!=1*..*n
#4!=1*2*3*4
#for loop
# n=5
# fact=1
# for i in range(1, n+1):
#     fact *=i
# print(fact)

# def cal_fact(n):
#     fact=1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# cal_fact(5)

#WAF TO CONVERT USD TO IND
# def price_ct(usd_val):
#     ind_val=usd_val*83
#     print(usd_val,"USD=", ind_val,"INR")
# price_ct(5)


#waf  to input a function ,if function is odd it returns a string "odd",if number is even it returns "even,"
# def ed_fun(n):
#     if(n*2==1):
#         print("ODD")
#     elif(n*2==0):
#         print("EVEN")
#     return ed_fun
# ed_fun(2)



#RECURSION
#this is called RECURSIVE Function.
# def show(n):
#     if(n==0):# this is a  condition it is called BASE CASE .
#         return
#     print(n)
#     show(n-1)
# show(5)

#CALL STACK:= FUNCTION CALL REPETELY

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n
# print(fact(5))

#WARECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS,
# def cal_sum(n):
#     if (n==0):
#         return 0
#     return cal_sum(n-1) +n
# sum= cal_sum(5)
# print(sum)


#WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST 
#HINT- USE LIST $INDEX AS PARAMETERS.
# def print_list(list,idx=0):
#     if (idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# heroes=["manas","Biswajit","manasi","rsghunath"]
# print_list(heroes)