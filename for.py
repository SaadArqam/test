# #FOR LOOPS

# for i in range(1,11):
#     print(i)

# for j in range(1,11,2):
#     print(j)

#     #CONTINUE AND BREAK

# for x in range(1,31):
#     if x==15:
#         continue
#     else:
#         print(x)

# for y in range(1,31):
#     if y==15:
#         break
#     else:
#         print(y)

# #NESTED LOOP
# for z in range(3):
#     for a in range(1,11):
#         print(a,end="")
#     print()

# #TO MAKE A RECTANGLE USING SYMBOLS

# rows=int(input("Enter the no of rows: "))
# colunms=int(input("Enter the no of columns: "))
# symbol=input("Enter the symbol to be used: ")
# for p in range(rows):
#     for q in range(colunms):
#         print(symbol,end="")
#     print()

#TIMER 

# import time
# t=int(input("Enter the time: "))
# for w in reversed(range(0,t)):      #REVERSED FUN REVERSE THE RANGE OR WE CAN USE (t,0,-1)
#     print(w)
#     time.sleep(1)
# print("BOOM")

# DIGITAK CLOCK

# import time
# t=int(input("Enter the time in seconds: "))
# for w in reversed(range(0,t)):      #REVERSED FUN REVERSE THE RANGE OR WE CAN USE (t,0,-1)
#     sec=w%60
#     min=int((x/60)%60)
#     hr=int(x/3600)
#     print(f"{hr:02}:{min:02}:{sec:02}")
#     time.sleep(1)
# print("BOOM")

# def Surface_Area(l,b,h):
#     s_area=2 * (l * b + b * h + h * l)   
#     return s_area
    
# def Volume(l,b,h):
#     vol=l*b*h
#     return vol

