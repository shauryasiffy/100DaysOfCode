print("Welcome to treasure island. \nYour mission is to find treasure!!")
door1= input("Where do you wanna go? \nLEFT OR RIGHT?").upper()
"""door2= input("What do you wanna do? \nSWIM OR WAIT?").upper()
door3= input("Which color do you wanna choose? \nBLUE, RED, OR YELLOW?").upper()
"""
if door1 == "LEFT":
    door2=input("What do you wanna do? \nSWIM OR WAIT?").upper()
    if door2=="WAIT":
        door3= input("Which color do you wanna choose? \nBLUE, RED, OR YELLOW?").upper()
        if door3=="YELLOW":
            print("WON")
        else:
            print("LOSE")
    else:
        print("LOOSE")
else:
    print("LOOSE")