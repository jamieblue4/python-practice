import random as rnd

upper_range = input("Type a number: ")

if upper_range.isdigit():
    upper_range = int(upper_range)

    if upper_range <= 0:
        print("Please type a number larger than 0.")
        quit()

else:
    print("Please type in a number.")
    quit()

random_number = rnd.random.randrange(0, 101)
print(upper_range)