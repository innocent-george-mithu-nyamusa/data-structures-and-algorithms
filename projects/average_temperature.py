#from array import *
# To Calculate the Average temperature
# First get number of days to calcute for
# Second get the number the value for each day
# Store that value in a place
# Calcute the average
# calculate the days above average

number_of_days = abs(int(input("Enter the number of days we want to calculate: ")))
total = 0
assert abs(number_of_days) > 0, "Number of days must be positive"

for day in range(number_of_days):
    day_temp = int(input(f"Day {day+1} high temp is: "))
    total += day_temp

avg = total/number_of_days
print("Average temperature is= ", avg)
