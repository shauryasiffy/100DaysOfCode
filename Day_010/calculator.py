
print("\nWelcome to the calculator\n")

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

operation = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

def calculator():
    num1=float(input("Enter the first number\n--> "))
    cont=True

    while cont:
        num2=float(input("Enter the next number\n--> "))
            
        for symbol in operation:
            print(symbol)
        
        op=input("Enter the operation\n--> ")

        calculation=operation[op]
        answer=calculation(num1,num2)
        print("The answer of {} {} {} is {}\n".format(num1,op,num2,answer))
    
        if input("Do you want to continue?\n type YES or NO\n--> ").upper()=="YES":
            num1=answer
        else:
            cont=False
            print("The final answer is {}\nTHANKYOU!\n".format(answer))
calculator()