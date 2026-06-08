Combo1 = 12.50 # Burger
Combo2 = 15.00 # Cheeseburger
Combo3 = 17.50 # X-Bacon

print(" Burger = 1 \n Cheeseburger = 2 \n X-Bacon = 3")

while True:
    lunch = str(input("Enter the snack number: "))

    if lunch == "1":
        print(f"Your Burger came to {Combo1}")
        break
    elif lunch == "2":
        print(f"Your Cheeseburger came to {Combo2}")
        break
    elif lunch == "3":
        print(f"Your X-Bacon came to {Combo3}")
        break
    else:
        print(f"Enter a valid number")