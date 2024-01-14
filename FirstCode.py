print("Welcome to the EPAL wood pallet cost calculator")
print("For pallet made from pine maritime wood")

print("0,17 m3 of maritime pine wood is needed")
maritime_pine_wood_min_price = 10.0
maritime_pine_wood_max_price = 70.0

while True :
    try:
        maritime_pine_wood_price = float(input("Please enter the current market price of 1 m3 maritime pine wood"))
        if maritime_pine_wood_min_price <= maritime_pine_wood_price <= maritime_pine_wood_max_price:
            break # Exit the loop if the input is within the valid range
        else :
            print(f"The price must be between {maritime_pine_wood_min_price} and {maritime_pine_wood_max_price} Please try again. ")
    except ValueError:
        print("Please enter a valid number.")

pallet_wood_volume = 0.17

total_wood_price = maritime_pine_wood_price * pallet_wood_volume
print(f"Total wood price is {total_wood_price} Euros by unit")

print("42 pieces of M5_5x90 threaded nails") 
M5_5x90_threaded_nails_price = float(input("please enter the price with all taxes included : "))

print("18 pieces of M5_5x38 threaded nails")
M5_5x38_threaded_nails_price = float(input("Please enter the price with all taxes included : "))

# total cost of raw material : 
raw_material_total_cost = M5_5x38_threaded_nails_price + M5_5x90_threaded_nails_price + total_wood_price
print(f"Total cost of raw material is {raw_material_total_cost} Euros")

# let's calculate the electricity cost hourly :
print("Electricity cost")
electricity_cost = float(input("Please enter the amount of your bill with all taxes included : "))

print("Total business activity hours for the billing period ")
total_business_activity_hours = float(input("please enter the amount of business hours of activity : "))

cost_by_hour = electricity_cost/total_business_activity_hours
print("Hourly electricity cost is {cost_by_hour} Euros")

# Hours conversion in minute :
cost_by_minute = cost_by_hour / 60
print(f"Cost of electricity by minute : {cost_by_minute} Euros")

# lets calculate the electricity cost by pallet : 
print("Electricity cost by pallet : ")
time_needed_to_build_a_pallet = float(input("please enter the amount of minutes needed to build a pallet : "))

total_electricity_cost_by_pallet = cost_by_minute * time_needed_to_build_a_pallet
print(f"Total electricity cost by pallet is {total_electricity_cost_by_pallet} Euros")

total_of_electricity_and_raw_material_cost_by_pallet = total_electricity_cost_by_pallet + raw_material_total_cost
print(f"Total electricity cost and raw material cost by pallet {total_of_electricity_and_raw_material_cost_by_pallet} Euros ")

# Now let's calculate the labour cost on the EPAL production line.
# Let's separate permanent workers and temporary workers with two lists :sß
# Permanent workers :
permanent_workers = []

# Let's add workers to this list:
while True:
    worker_name = input("Please enter the name for each worker then 'exit' to quit: ")

    if worker_name.lower() == 'exit':
        break  # Exit the loop if the input is 'exit'

    permanent_workers.append({'name': worker_name})

# Print the list of permanent workers
print("\nPermanent Workers:")
for worker in permanent_workers:
    print(worker)

# Temporary workers :
temporary_workers = []

# Let's add workers to this list:
while True:
    worker_name = input("Please enter the name for each worker then 'exit' to quit: ")

    if worker_name.lower() == 'exit':
        break  # Exit the loop if the input is 'exit'

    temporary_workers.append({'name': worker_name})

# Print the list of temporary workers :
print("\nTemporary Workers: ")
for worker in temporary_workers :
    print(worker)

print("Please enter only gross values regarding salary and hourly rate")

# Permanent workers salary and working hours :
for worker in permanent_workers:
    # Request of hourly rate :
    hourly_rate = float(input(f"Please enter the hourly rate for {worker['name']}: "))
    worker['hourly_rate'] = hourly_rate  # Dictionnary
    
    # Request of worked hours amount :
    hours_worked = float(input(f"Please enter the worked hours amount for {worker['name']}: "))
    worker['hours_worked'] = hours_worked  # Dictionnary

# Temporary workers salary and working hours :
for worker in temporary_workers:
    # Request of hourly rate :
    hourly_rate = float(input(f"Please enter the hourly rate for {worker['name']}: "))
    worker['hourly_rate'] = hourly_rate  # Dictionnary
    
    # Request of hourly rate :
    hours_worked = float(input(f"Please enter the worked hours amount for {worker['name']}: "))
    worker['hours_worked'] = hours_worked  # Dictionnary

# Salary for permanent workers :

total_salary_permanent = 0
for worker in permanent_workers:
    salary = worker['hourly_rate'] * worker['hours_worked']
    print(f"Salary for {worker['name']}: {salary} Euros")
    total_salary_permanent += salary

# Salary for temporary workers :

total_salary_temporary = 0
for worker in temporary_workers:
    salary = worker['hourly_rate'] * worker['hours_worked']
    print(f"Salary for {worker['name']}: {salary} Euros")
    total_salary_temporary += salary

# Calculation of total gross salary cost :
total_salary = total_salary_permanent + total_salary_temporary
print(f"Total gross salary cost : {total_salary} Euros")

# Calculation of total labour cost :
social_taxes_percentage = 0.45 
social_taxes_cost = total_salary * social_taxes_percentage 
total_labour_cost = total_salary + social_taxes_cost 








