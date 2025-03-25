# def create_name(first_name,last_name):
#     first_name=first_name.capitalize()
#     last_name=last_name.capitalize()
#     return first_name +" "+ last_name
# first_name=input()
# last_name=input()
# print(create_name(first_name,last_name))


# LIST COMPREHENSION
double=[]
for i in range(1,11):
    double.append(i)
print(double)

# OR
double=[i for i in range(1,11)]
print(double)