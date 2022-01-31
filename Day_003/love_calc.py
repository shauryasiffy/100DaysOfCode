n1=list(input("What is your name?").upper())
n2=list(input("What is her name?").upper())

true=["T","R","U","E"]
love=["L","O","V","E"]

a=[]
b=[]

for letter in true:
    if letter in n1:
        a.extend(letter)
    if letter in n2:
        a.extend(letter)
    
for letter2 in love:
    if letter2 in n1:
        b.extend(letter2)
    if letter2 in n2:
        b.extend(letter2)

print(a)
print(b)


