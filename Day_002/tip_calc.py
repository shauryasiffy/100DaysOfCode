print("welcome to the Tip Calculator")
bill = float(input("What was the total bill? \n$"))
split = int(input("how many people to split the bill? \n"))
tip = int(input("What percentage do you want to tip? \n10%\n12%\n15%\n"))
to_pay = round((bill/split) + ((bill/split)*tip)/100)

print(f"Each person should pay: ${to_pay}")
