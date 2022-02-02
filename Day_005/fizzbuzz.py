num=int(input("enter the number"))
for i in range(1, num+1):
    if i%3==0 and i%5==0:
        print("<<FIZZ-BUZZ>>")
    elif i%3==0:
        print("FIZZ")
    elif i%5==0:
        print("--BUZZ--")
    else:
        print(i)