import random as rd
"""random is a module in python, 
module is a file containing set of functions that we want to include in our application"""

rand_int=rd.randint(0,1)
if rand_int==0:
    print("Heads")
else:
    print("Tails")
print(rand_int)