# for i in range(4):
#     for j in range (i+1):
#         print(i,end="")
#     print()

# ## WHILE LOOP
# name=input("ENter your name: ")
# while name=="":
#     print("You did not enter your name:")
#     name=input("ENter your name: ")        #if we do not use this we will be stuck in an infinite loop
# print(f"Hello {name}")


# food=input("Enter a food you like (q to quit): ")
# while food != "q":
#     print(f"You like: {food}")
#     food=input("Enter a food you like (q to quit): ")
# print("BYE")


# num=int(input("Enter a number betwwn 1-10: "))
# while num<1 or num>10:
#     print(f"Your number is not valid")
#     num=int(input("Enter a number betwwn 1-10: "))
# print(f"Your number is valid ")

# #CI CALCULATOR

# principle=0
# rate=0
# time=0
# while principle<=0:
#     principle=float(input("Enter the principle value: "))
#     if principle<=0:
#         print("principle can't be negative or zero")

# while rate<=0:
#     rate=float(input("Enter the intrest rate: "))
#     if rate<=0:
#         print("intrest rate can't be negative or zero")

# while time<=0:
#     time=int(input("Enter the time in yars: "))
#     if time<=0:
#         print("time can't be negative or zero")

# total=principle*pow((1+rate/100),time)
# print(f"Total balancs after {time} years : ${total:.2f}")

#SHOPPPING CART

# items=[]
# prices=[]
# total=0
# while True:
#     item=input("Enter the items to buy (q to quit)")
#     if item.lower()=="q":
#         break
#     else:
#         price=float(input("Enter the price : $"))
#         items.append(item)
#         prices.append(price)
# print("-----YOUR CART-----")
# for item in items:
#     print(items)
# for price in prices:
#     total+=price
# print(f"Your total price is: ${total}")


#2-D lists

# a=["we","me","us"]
# b=[1,2,3,4]
# c=['hello','asf','wreg']
# d=[a,b,c]
# print(d)
# print(d[0][1])

# #num pad

# num_pad=((1,2,3),
#          (4,5,6),
#          (7,8,9),
#          ("*",0,"#"))
# for i in num_pad:
#     for j in i:
#         print(j,end=" ")
#     print()

#QUIZ
questions=("How many elements in periodic table?:",
           "How many bones in human body?:",
           "Which animal lays the largest eggs?:",
           "What is the most abundant gas  in earth's atmosphere?:",
           "Which is the hottest planet in our solar system")
options=(("A. 34","B. 4325","C. 118","D. 235"),
         ("A.1235","B. 2135","C.223 ","D.206"),
         ("A. Whale","B. Crocodile","C. Ostrich","D. Elephant"),
         ("A. Oxygen","B. Hydrogen","C. Nitrogen","D. Helium"),
         ("A. Mercury","B. Venus","C. Earth","D. Mars"))
answers=("C","D","C","C","B")
guesses=[]
score=0
question_num=0
for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("A,B,C,D: ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("WRONG!!!")
        print(f"{answers[question_num]}: is the correct answer")
    question_num+=1

print("---------")
print("  RESULT ")
print("---------")

print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
    
print()
print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score=int((score/len(questions))*100)
print(f"Your score is: {score}%")


