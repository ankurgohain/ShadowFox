justice_league = ["Superman" , "Batman" , "Wonder Woman" , " Flash" , "Aquaman" , "Green Lantern"] 
print("Number of members:",len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Updated Justice League:", justice_league)

justice_league[4], justice_league[5] = justice_league[5], justice_league[4]
print("After swapping: ", justice_league)

justice_league.clear()
print("After disbanding :",justice_league)

justice_league= ["Superman", "Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]

print("New league :",justice_league)

justice_league.sort()
print("New leader:", justice_league[0])