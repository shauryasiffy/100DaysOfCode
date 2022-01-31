print("Welcome to pizza delivery system")
size=input("What size do you want? \nS, M, or L\n").upper()
pep=input("Do you want pepperoni? \nY or N\n").upper()
che=input("Do you want extra cheese? \nY or N\n").upper()

def pizza_calc(size, pep, che):
    bill=0
    if size == "S":
        bill = bill + 15
        if pep=="Y":
            bill = bill + 2
        if che == "Y":
            bill = bill + 1
    
    if size == "M":
        bill = bill + 20
        if pep=="Y":
            bill = bill + 3
        if che == "Y":
            bill = bill + 1
    if size == "L":
        bill = bill + 25
        if pep=="Y":
            bill = bill + 3
        if che == "Y":
            bill = bill + 1
    
    return bill
print(f"Your final bill is ${pizza_calc(size, pep, che)}")