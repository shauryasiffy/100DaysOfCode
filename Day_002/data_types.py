num = input("Enter the number \n-->")
a = list((num))
b = []
for element in a:
    element = int(element)
    b.append(element)
    sum = 0
    for x in b:
        sum = sum + x
print(f"The sum of the digits of {num} is \n -->{sum}")