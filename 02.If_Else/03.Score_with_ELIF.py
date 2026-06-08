score = int(input("Enter the customer's score: "))

if score >= 1000:
    print("The customer is entitled to receive 3GB more on their internet allowance!")
elif score >= 500:
    print("The customer is entitled to receive 1.5GB more on their internet allowance!")
elif score >= 200:
    print("The customer is entitled to receive 500MB more on their internet allowance!")
else:
    print("The customer will not receive a bonus.")