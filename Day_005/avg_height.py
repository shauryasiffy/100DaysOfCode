heights=input("What are the heights of the students in centimeters?\n-->").split()
#print(type(heights))
sum=0
for item in heights:
    item = int(item)
    #print(type(item))
    sum = sum+item
avg=sum/len(heights)
print(f"The average height of the class is {avg}cm.")