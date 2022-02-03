import random as rd
print("\nWelcomce to Hangman\n")
print("\nRules: \nYou need to guess the word letter by letter\nbefore the HANGMAN completes!\n")
names=["shyam", "ram", "shaurya", "yash", "pankaj", "purohit"]
a = list(rd.choice(names).upper())
#print(a)
#print(len(a))
right=[]
wrong=[]
while len(wrong) in range(0,7):
    guess=input("Enter the letter\n--> ").upper()
    if guess in a:
        right.append(guess)
        print(f"{guess} is RIGHT\n")
        if len(right) == len(a):
            print("\nYou WON HANGMAN\n")
            break
        else:
            pass
    else:
        wrong.append(guess)
        print(f"{guess} is WRONG")
else:
    print("\nHANGMAN DEAD\n")
#print(right)
#print(wrong)