import random as rd
from signal import pause
from tracemalloc import stop
your_choice=int(input("What do you choose? \n 0 for rock\n 1 for Scissor\n 2 for Paper\n"))
comp_choice=rd.randint(0,2)
#print(comp_choice)
print(f"You chose {your_choice}")
print(f"Computer chose {comp_choice}")

if your_choice == comp_choice:
    print("\n \tTIE")

elif your_choice == 0:
    if comp_choice==1:
        print("\n \tWIN")
    else:
        print("\n \tLOSS")

elif your_choice == 1:
    if comp_choice==2:
        print("\n \tWIN")
    else:
        print("\n \tLOSS")

elif your_choice == 2:
    if comp_choice==1:
        print("\n \tWIN")
    else:
        print("\n \tLOSS")
