import os
import json
# a= 5
# b=10
# j =(a+b)*2
# s= a*b

# c = True
# if c :
#     my_text = open("hello.text","a")
#     my_text.write(f"pi: {j}\n")
#     my_text.write(f"pi: {s}\n")
    
#     my_text = open("hello.text","r")
#     print(my_text.read())

# else:
#     print("a false")



new = 'new_file.txt'


ism = input("ismingiz ")
tyil = int(input("yoshiz"))
salary =input("maoshiz")



user =[]
# user.append(ism)
# user.append(tyil)
# user.append(salary)

user.append({
    
    "name":ism.title(),
    "age":int(tyil),
    "salary":int(salary)
})

with open(new,'a') as fayl:
    
    fayl.write(ism+"\n")
    fayl.write(str(tyil)+"\n")
    fayl.write(salary+"\n")
   

with open('new_file.txt') as f:
    a = f.read()
  

    
    