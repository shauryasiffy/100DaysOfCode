max=int(input("enter the maximum number\n-->"))
even_list=[]
sum=0
for num in range(0,max+1):
    if num%2==0:
        even_list.append(num)
for num in even_list:
        sum = sum+num

print(f"The sum is \n{sum}")
