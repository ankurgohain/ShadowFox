# BMI
usr_h = float(input("Enter your height in m: "))
usr_w = int(input("Enter your weight in kg: "))
bmi = usr_w / (usr_h ** 2)
if bmi < 18.5:
    print("You are underweight.\n", bmi)  
elif 18.5 <= bmi < 24.9:
    print("You are normal weight. ", bmi)
elif 25 <= bmi < 29.9:
    print("You are overweight." , bmi)
elif 30 <= bmi < 34.9:
    print("You are obese (Class 1).", bmi)

# cities
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]

city = input("Enter a city: ")
if city in Australia:  
    print(city, "is in Australia.")
elif city in UAE:
    print(city, "is in UAE.")
elif city in India:
    print(city, "is in India.")

city2 = input("Enter another city: ")
if city in Australia and city2 in Australia:  
    print("Both cities are in Australia.")
elif city in UAE and city2 in UAE:
    print("Both cities are in UAE.")
elif city in India and city2 in India:
    print("Both cities are in India.")
else:
    print("They don't belong to the same country")