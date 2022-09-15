cal={'january':31,'february':28,'march':31,'april':30,'may':31,'june':30,'july':31,'august':31,'september':30,'october':31,'november':30,'december':31}

def leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            True
    else:
        False

y=int(input("Enter the year\n--> "))
m=input("Enter the month\n--> ").lower()

for month in cal:
    if leap(y)==True:
        cal.update({"february":29})
    if m==month:
        print("The month {} of the Year {} has {} number of days.\nTHANKSYOU!".format(m,y,cal[month]))





