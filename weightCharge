# get input from the user
weight = float(input("enter the weight of the delivery in kg: "))
volume = float(input("enter the volume of the delivery in cm3: "))

# constants for charges
BASIC_CHARGE = 5
WEIGHT_CHARGE_RATE = 0.50
WEIGHT_THRESHOLD = 1
VOLUME_CHARGE_RATE = 0.50
VOLUME_THRESHOLD = 10000
VOLUME_EXTRA = 200

# calculate weight charge
weight_charge = 0
if weight > WEIGHT_THRESHOLD:
    extra_weight = weight - WEIGHT_THRESHOLD
    weight_charge = WEIGHT_CHARGE_RATE * (extra_weight / 0.1)

# calculate volume charge
volume_charge = 0
if volume > VOLUME_THRESHOLD:
    extra_volume = volume - VOLUME_THRESHOLD
    volume_charge = VOLUME_CHARGE_RATE * (extra_volume / VOLUME_EXTRA)

# calculate total cost and print the result
total_cost = BASIC_CHARGE + weight_charge + volume_charge
print("total cost of delivery: £" + str(total_cost))
