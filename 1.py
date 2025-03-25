n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(i+1,n):
        print(" ",end=" ")
    for j in range((n-i)):
        print(" ",end=" ")
    if i==0:
        print("*",end=" ")
    else:
        for j in range(i):
            print("*",end=" ")
    print()

for i in range(1,n+1):
    for j in range(n-i):
        print("*",end=" ")
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()