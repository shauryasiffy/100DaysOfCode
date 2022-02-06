database={}

finished=False
while finished==False:
    name=input("\nWhat is the bidder's name?\n--> ")
    bid=int(input("\nEnter their Bid value\n--> $"))
    database[name]=bid
    next_bid=input("Are there any other bidder?\nType 'YES' or 'NO'").upper()
    if next_bid=="NO":
        finished==True
        print(database)
        max=0
        winner=''
        for name,bid in database.items():
            if bid > max:
                winner=name
                max=bid
        print(f"\nThe Winner is {name} with the highest bid of ${max}\n")
        break
    else:
        finished=False