weight = float(input("Please enter the weight(in lb): "))

ground_shipping = 20.00
ground_shipping_premium = 125.00
drone_shipping = 0

#Ground Shipping
if weight <= 2:
    ground_shipping += 1.50 * weight

elif 2 <= weight <= 6:
    ground_shipping += 3.00 * weight

elif 6 <= weight <= 10:
    ground_shipping += 4.00 * weight

elif weight > 10:
    ground_shipping += 4.75 * weight

#Drone Shipping
if weight <= 2:
    drone_shipping = 4.50 * weight

elif 2 <= weight <= 6:
    drone_shipping = 9.00 * weight

elif 6 <= weight <= 10:
    drone_shipping = 12.00 * weight

elif weight > 10:
    drone_shipping = 14.25 * weight

# Decideing the cheapest method
if drone_shipping >= ground_shipping <= ground_shipping_premium:
    cost = ground_shipping
    method = "Ground Shipping"

elif ground_shipping >= ground_shipping_premium <= drone_shipping:
    cost = ground_shipping_premium
    method = "Ground Shipping Premium"

else:
    cost = drone_shipping
    method = "Drine Shipping"

print(f"Weight : {weight}")
print(f"Cheapest Shipping Method: {method}")
print(f"Shipping cost: {cost}")