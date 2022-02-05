int_num=int(input("Enter the number\n"))
def Prime(num):
    is_prime= True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
    if is_prime:
        print("The Number is Prime")
    else:
        print("The number is NOT Prime")

Prime(int_num)
