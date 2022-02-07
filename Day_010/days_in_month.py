month= input("Enter the month\n-->").lower()
year=int(input("Enter the year\n-->"))

month_num=int()

chart={"january":1, "february":2, "march":3, "april":4, "may":5, "june":6,
 "july":7, "august":8, "september":9, "october":10, "november":11, "december":12}

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

for month_name, month_number in chart.items():
    if month == month_name:
        month_num=month_number

def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                #print("LEAP1")
                return True
            else:
                #print("NOT LEAP1")
                return False
        else:
            #print("LEAP2")
            return True
    else:
        #print("NOT LEAP2")
        return False
if leap_year(year)==True:
    month_days[1]=29
    print(f"The month of {month.upper()} of the year {year} which is a LEAP YEAR has\n{month_days[month_num-1]} days ")
elif leap_year(year)==False:
    print(f"The month of {month.upper()} of the year {year} which is a NOT a LEAP YEAR has\n{month_days[month_num-1]} days ")
