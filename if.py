# age=int(input("Enter the age: "))
# if age>=90:
#     print("You are an ancient fossil")
# elif age>=18:
#     print("You area an adult")
# elif age<18:
#     print("You are a monir")
# else:
#     print("Wait for some time")

# name=input("Enter our name (saad/else):")
# if name=="saad":
#     print(f"Hello: {name}")
# else:
#     print(f"Fuck off: {name}")

#  #CALCULATOR

# op=input("Enter the operators: (+ - * /)")
# num1=float(input("Enter the first number; "))
# num2=float(input("Enter the second number; "))
# if op=="+":
#     print(num1+num2)
# elif op=="-":
#     print(num1-num2)  
# elif op=="*":
#     print(num1*num2)
# elif op=="/":
#     print(num1/num2) 
# else:
#     print("Not a valid opertor")


# # WEIGHT CONVERTER
# weight=float(input("Enter the weight: "))
# unit=input("kilograms or pounds? (K/L): ")

# if unit=="K":
#     weight=weight*2.205
#     unit="Lbs."
#     print(f"Your weight is: {round(weight, 2)}{unit}")
# elif unit=="L":
#     weight=weight/2.205
#     unit="Kgs."
#     print(f"Your weight is: {round(weight, 2)}{unit}")
# else:
#     print(f"{unit} is not valid")

# # TEMPERATURE CONVERTER
# temp=input("Is the temperature in Celcius or Farenheit: (C/F) ")
# con=float(input("Enter the temperature: "))
# if temp=="C":
#     con=(9*con)/5 +32
#     temp="F"
#     print(f"The temperature in farenheit is: {con}")
# elif temp=="F":
#     con=((con-32)*5)/9
#     temp="C"
#     print(f"The temperature in celcius is: {con}")
# else:
#     print(f"Wrong temperature unit: {temp}")

# #LOGICAL OPERATORS
# and=checks more than 2 conditions if True
# or= least 1 condition is True
# not=true if condition is false and vice versa

# t= -100
# sunny=False

# if t >0 and t< 50:
#     print("Temperture is good")
# else:
#     print("Temperatuire is bad")

# if t<=0 or t>=50:
#     print("Temperture is bad")
# else:
#     print("Temperatuire is good")

# if not sunny:
#     print("It is sunny outside")
# else:
#     print("It is cloudy ooutside")


##CONDITIONAL STATEMENT 
## X if condition else Y

# n=8 
# p=5
# q=9
# r=1 
# print("Positive" if n>0 else "Negative")
# result="EVEN" if n%2==0 else "ODD"
# max=p if p>q else q
# min=p if p<q else q
# print( max)
# print(min)
# status="ADULT" if r>=18 else "MINOR"
# print(status) 

# w=input("Enter the full name: ")
# # result=len(w)
# result=w.capitalize()
# print(result)

##VALIDATE USER INPUT
# uname=input("Entter your username: ")
# if len(uname)>12:
#     print("Your username can't be greater than 12 characters")
# elif not uname.find(" ")==-1:
#     print("User name can't have spaces")
# elif not uname.isalpha:
#     print("Usename can't have numbers")
# else:
#     print(f"Welcome {uname}")

5
n=int(input("Enter the number: "))
for i in range(n):
    for j in range(1,i+1):
        print(j,sep=" ",end="")
    print()