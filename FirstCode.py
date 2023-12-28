print("EPAL wood pallet cost calculator")
print("For pallet made from pine maritime wood")

print("0,17 m3 of maritime pine wood is needed")
Maritime_pine_wood_min_price = 10.0
Maritime_pine_wood_max_price = 70.0

while True :
    try:
        Maritime_pine_wood_price = float(input("Please enter the current market price of 1 m3 maritime pine wood"))
        if Maritime_pine_wood_min_price <= Maritime_pine_wood_price <= Maritime_pine_wood_max_price:
            break # Exit the loop if the input is within the valid range
        else :
            print(f"The price must be between {Maritime_pine_wood_min_price} and {Maritime_pine_wood_max_price} Please try again. ")
    except ValueError:
        print("Please enter a valid number.")

Pallet_wood_volume = 0.17

Total_wood_price = Maritime_pine_wood_price * Pallet_wood_volume
print(f"Total wood price is {Total_wood_price} Euros by unit")

print("42 pieces of M5_5x90 threaded nails") 
M5_5x90_threaded_nails_price = float(input("please enter the price with all taxes included : "))

print("18 pieces of M5_5x38 threaded nails")
M5_5x38_threaded_nails_price = float(input("Please enter the price with all taxes included : "))

#total cost of raw material : 
Raw_material_total_cost = M5_5x38_threaded_nails_price + M5_5x90_threaded_nails_price + Total_wood_price
print(f"Total cost of raw material is {Raw_material_total_cost} Euros")

#let's calculate the electricity cost hourly :
print("Electricity cost")
Electricity_cost = float(input("Please enter the amount of your bill with all taxes included : "))

print("Total business activity hours for the billing period ")
Total_business_activity_hours = float(input("please enter the amount of business hours of activity : "))

Cost_by_hour = Electricity_cost/Total_business_activity_hours
print("Hourly electricity cost is {Cost_by_hour} Euros")

#Hours conversion in minute :
Cost_by_minute = Cost_by_hour / 60
print(f"Cost of electricity by minute : {Cost_by_minute} Euros")

#lets calculate the electricity cost by pallet : 
print("Electricity cost by pallet : ")
Time_needed_to_build_a_pallet = float(input("please enter the amount of minutes needed to build a pallet : "))

Total_electricity_cost_by_pallet = Cost_by_minute * Time_needed_to_build_a_pallet
print(f"Total electricity cost by pallet is {Total_electricity_cost_by_pallet} Euros")

Total_of_electricity_and_raw_material_cost_by_pallet = Total_electricity_cost_by_pallet + Raw_material_total_cost
print(f"Total electricity cost and raw material cost by pallet {Total_of_electricity_and_raw_material_cost_by_pallet} Euros ")

#Now let's calculate the labour cost :

