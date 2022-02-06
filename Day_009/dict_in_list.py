travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
print(f"\nThe current travel log is \n{travel_log}\n")
print("\nNow you can add to your travel log\n")

country=input("Enter the Country\n-->")
visits=int(input("How many times did you visited?\n-->"))
cities=input("Whcih cities did you visited?\n-->").split()

def add(country,visits,cities):
  
  new_log={}
  new_log["country"]=country
  new_log["visits"]=visits
  new_log["cities"]=cities

  travel_log.append(new_log)
  print(travel_log)

add(country, visits, cities)

