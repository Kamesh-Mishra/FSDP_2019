#Target Heart Rate Calculator

age = int(input("Enter the present age:"))



maximum_heart_rate= int(220-age)
print("your maximum heart rate is:",maximum_heart_rate,"Beats per Minute")

lower_target_heart_rate=70*maximum_heart_rate//100
higher_target_heart_rate=85*maximum_heart_rate//100

print("your lower Target Heart Rate Range is:",lower_target_heart_rate,"Beats per minute")
print("your Higher Target Heart Rate Range is:",higher_target_heart_rate,"Beats per minute")
