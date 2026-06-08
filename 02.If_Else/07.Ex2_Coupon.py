# requesting the customer's data
purchase_value = input("Enter the value of the purchase made: ")
coupon = input("Enter the discount coupon: ")

# performing the logical test with the coupon in uppercase
if coupon.upper() == "BIRTH10":
    # calculation of 10% discount
    final_value = float(purchase_value) * 0.9
else:
    final_value = float(purchase_value)
    print("INVALID COUPON")

# displaying the final purchase value
print("The final purchase value is {}".format(final_value))