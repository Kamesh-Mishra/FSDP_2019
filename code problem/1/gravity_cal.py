#Gravity Calculator

position_distance_time = float(input("time after falling is:"))
acceleration = float(input("Acceleration:"))


position_distance = (acceleration*position_distance_time**2)/2
print("distance travelled by object after",position_distance_time," sec is:",position_distance)
