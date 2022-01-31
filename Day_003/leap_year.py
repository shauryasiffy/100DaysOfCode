year=int(input("Enter the year\n-->"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("LEAP1")
        else:
            print("NOT LEAP1")
    else:
        print("LEAP2")
else:
    print("NOT LEAP2")