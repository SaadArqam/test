# def max(a,b,c):
#     if a>b:
#         if a>c:
#             print(a)
#         else:
#             print(c)
#     if b>a:
#         if b>c:
#             print(b)
#         else:
#             print(c)
# a=int(input())
# b=int(input())
# c=int(input())
# max(a,b,c)


#PATTERN USING DEF AND RECURSIONS

#RIGHT ANGLE TRIANGLE
# def patern(n):
#     if n==5:
#         return
#     print("* "*n)
#     return(patern(n+1))
# patern(1)

# #INVERTED TRIANGLE
# def patern(n):
#     if n==0:
#         return
#     print("* "*n)
#     return(patern(n-1))
# patern(5)




# def knight(x,y):
#     if x==1 or x==8:
#         if y==1 or y==8:
#             return 2
#         elif y==1 or y==7:
#             return 3
#         else:
#             return 4
#     elif x==2 or x==7:
#         if y==1 or y==8:
#             return 3
#         elif y==2 or y==7:
#             return 4  
#         else:
#             return 6
#     else:
#         if y==1 or y==8:
#             return 4
#         elif y==2 or y==7:
#             return 6
#         else:
#             return 8
        

#CODE TO PRINT A HOLLOW TRIANGLE
n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n):
        if i==n or i+j==n+1 or j-i==n-1: 
            print("*",end="")
        else:
            print(end=" ")
    print()



        