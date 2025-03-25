# a=5.5
# a=int(a)
# print(a)

# n=int(input())
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# m=int(input("no. of rows"))
# p=int(input("no. of columns"))
# o=input('Enter the symbol')
# for i in range(m):
#     for j in range(p):
#         print(o,end="")
#     print()


# n=5
# for i in range(n):
#     for j in range(1,i+2):
#         print(j,end=" ")
#     print()


# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(j,end=" ")
#     print()


# print((789)<str(6541))
# if 3!=4:
#     print("True")
# print("false")

# '''Write a program to print the following pattern :
#     *
#    ***
#   *****
#  *******
# ********* '''

# n = 5
# for i in range(1, n+1):
#     print(' ' * (n - i) + '*' * (2 * i - 1))




# n=int(input())
# temp=n
# while temp>0:
#     dig=temp%10
#     print(dig)
#     temp=temp//10



# doubles=[]
# for i in range(1,11):
#     doubles.append(i*2)
# print(doubles)

# or

# doubles=[x*2 for x in range(1,11)]
# print(doubles)
# triples=[y*3 for y in range(1,11)]
# print(triples)
# sq=[z**2 for z in range(1,11)]
# print(sq)
# f=["apple","banana","orange","guava"]
# f=[fruits.upper() for fruits in f]
# fruit_char=[fruit[0] for fruit in f]
# print(fruit_char)
# print(f)
# numbers=[1,2,-3,4,-5,6-7]
# p=[num for num in numbers if num>=0]
# n=[num for num in numbers if num<0]
# e=[num for num in numbers if num%2==0]
# o=[num for num in numbers if num%2!=0]
# grades=[45,98,96,100,56]
# marks=[grade for grade in grades if grade>50]
# print(marks)
# print(p)
# print(n)
# print(e)
# print(o)



# #MATCH CASE[alt to use many if elif cases]
# #THIS IS NORAML WAy
# def week(day):
#     if day==1:
#         print("sunday")
#     elif day==2:
#         print("monday")
#     elif day==3:
#         print("tuesday")
#     elif day==4:
#         print("wednesday")
#     elif day==5:
#         print("thursday")
#     elif day==6:
#         print("friday")
#     elif day==7:
#         print("saturday")
#     else:
#         print("Invalid day")
# week(5)

#MATCH CASE
# def week(day):
#     match day:
#         case 1:
#             return "sunday"
#         case 2:
#             return "monday"
#         case 3:
#             return "tuesday"
#         case 4:
#             return "wednesaday"
#         case 5:
#             return "thursday"
#         case 6:
#             return "friday"
#         case 7:
#             return "saturday"
#         case _:
#             return "invalid day"
# print(week(1))

#OTHER USE
# def week(day):
#     match day:
#         case "saturday" | "sunday":
#             return True
#         case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
#             return False
#         case _:
#             return False
# print(week("saturday"))



# #MODULES
# import math           |
# from math inport ()   |ways to inmport a module 
# import math as ()     |

# import ex #imported all the contents from ex.py file
# # result=ex.pie
# result=ex.sq(3)
# # result=ex.cu(3)
# print(result)
# # print(result)
# # print(result)



#HOLLOW DIAMOND
#         *         
#       *   *       
#     *       *     
#   *           *   
# *               * 
#   *           *   
#     *       *     
#       *   *       
#         *        
# n=int(input())
# for i in range(1,2*n):
#     for j in range(1,2*n):
#         if i+j==n+1 or j-i==n-1 or i-j==n-1 or i+j==(3*n)-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



#A
#   * * *   
# *       * 
# * * * * * 
# *       * 
# *       * 

# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if ((j==0 or j==n-1) and i!=0) or (i==n//2 or i==0) and (j>0 and j<n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# n,m=map(int,input().split())
# s=0
# ml=1
# s2=0
# ml2=1
# while n>0:
#     d=n%10
#     s=s+d
#     ml=ml*d
#     n=n//10
#     d=0
# while m>0:
#     f=m%10
#     s2=s2+f
#     ml2=ml2*f
#     m=m//10
#     f=0
# if s==s2 and ml==ml2:
#     print("Anagram")
# else:
#     print("Not")



# n=int(input())
# for i in range(1,2*n):
#     for j in range(1,2*n):
#         if j==1 or j==2*n-1 or i==j or i+j==2*n or i==(2*n)//2 or ((j==2 or j==2*n-2) and (i>1 and i<2*n-1)) or ((j==3 or j==2*n-3) and (i>2 and i<2*n-2)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



