marks=input("What are the marks of the students?\n-->").split()
max=0
for element in marks:
    element = int(element)
    if element >= max:
        max=element
print(f"The maximum marks is {max}.")