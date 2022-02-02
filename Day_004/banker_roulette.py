import random as rd
names=input("Enter the names of people \n-->").split(" ")
a=len(names)
choice=rd.randint(0,a-1)
print(f"{names[choice]} has to pay the bill!")
