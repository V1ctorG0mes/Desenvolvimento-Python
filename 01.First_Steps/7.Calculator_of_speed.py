print("This program calculates the average speed of a scooter")

# Asking for user input
distance = input("What was the distance in meters traveled by the scooter? ")
time = input("How many minutes did the scooter take to cover this distance? ")

# Calculation
average_speed = float(distance) / float(time)

# Displaying the result
print("The scooter reached a speed of {0:.2f} m/min".format(average_speed))