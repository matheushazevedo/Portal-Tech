vehicleWeight = float(input("What is the vehicle's weight? "))
vehicleWheels = int(input("How many wheels does the vehicle have? "))
peopleOnVehicle = int(input("How many people are inside the car? "))

if vehicleWheels == 2 or vehicleWheels == 3:
    vehicleLicense = "A"
elif vehicleWheels == 4 and peopleOnVehicle <= 8 and vehicleWeight <= 3500:
    vehicleLicense = "B"
elif vehicleWheels >= 4:
    if vehicleWeight >= 3500 and vehicleWeight <= 6000:
        vehicleLicense = "C"
    elif peopleOnVehicle > 8:
        vehicleLicense = "D"
    elif vehicleWeight > 6000:
        vehicleLicense = "E"

print(f"The best category of license for the vehicle informed is {vehicleLicense}")