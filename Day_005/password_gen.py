import random as rd
let=int(input("How many letter?"))
sym=int(input("How many symbols?"))
num=int(input("How many numbers?"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

pas=""

for element in range(0, let):
    pas=pas+ rd.choice(letters)
for element in range(0, sym):
    pas=pas+ rd.choice(symbols)
for element in range(0, num):
    pas=pas+ rd.choice(numbers)
print(pas)
