w=float(input("What is the weight in kilogram?\n-->"))
h=float(input("What is your height in meter\n-->"))
b=w/(h**2)
print(f"Your Body mass Index is {b}kg/msq")
if b<18.5:
    print("UnderWeight")
elif 18.5<=b<25:
    print("NORMAL")
elif 25<=b<30:
    print("OVERWEIGHT")
elif 30<=b<35:
    print("OBESE")
elif b>=35:
    print("CLINICALLY OBESE")