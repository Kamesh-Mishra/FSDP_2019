#Ride Cost Calculator

distance_cover= float(input("travel km per day is:"))

cost_of_fuel= float(input("cost of fuel is:"))

vehicle_avg= float(input("your vehicles average is:"))



daily_travel_cost= (distance_cover/vehicle_avg)*(cost_of_fuel)

print("cost of driving per day to office is:",daily_travel_cost,"INR")
