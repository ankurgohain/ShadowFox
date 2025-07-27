# import random
# def roll_dice():
#     return random.randint(1, 6)
# roll_6 = 0
# roll_1 = 0
# roll_66 = 0
# for i in range(20):
#     roll1 = roll_dice()
#     roll2 = roll_dice()
#     if roll1 == 6:
#         roll_6 += 1
#     if roll1 == 1:
#         roll_1 += 1
#     if roll1 == 6 and roll2 == 6:
#         roll_66 += 1
# print(f"Rolled a 6: {roll_6} times")
# print(f"Rolled a 1: {roll_1} times")
# print(f"Rolled two 6s in a row: {roll_66} times")

total = 100
set = 10
cur = 0
for i in range(set):
    for j in range(set):
        cur += 1
    print('Are you tired?')
    a1 = input('yes or no: ')
    if a1 == 'yes':
        a2 = input("Do you want to skip the rest? (yes or no): ")
        if a2 == 'yes':
            print(f"You completed a total of {cur*10} jumping jacks.")
            break
        else:
            print(f"You have {100 - cur*10} sets remaining.")
            print("Are you tired?")
            a3 = input('yes or no: ')
            if a3 == 'yes':
                print(f"You completed a total of {cur*10} jumping jacks.")
                break
            else: 
                continue
    else:
        print(f"You have {total - cur*10} sets remaining.")
        continue
print("Congratulations! You completed the workout")