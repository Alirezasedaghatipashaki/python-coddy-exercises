# ==========================================
# Day 7: User Input & Real-World Logic
# Platform: Coddy Practice
# ==========================================

# --- Exercise 1: Driving Eligibility Check (User Input) ---
# Taking inputs: Converting age to integer and checking boolean flags
age = int(input("Enter age: "))
has_license = input("Has license (true/false): ") == "true"
has_insurance = input("Has insurance (true/false): ") == "true"

# User is eligible only if ALL conditions are met
result = age >= 18 and has_insurance and has_license
print("Eligible to drive:", result)


# --- Exercise 2: Outdoor Activity Planner Logic ---
is_sunny = True
temperature = 25
wind_speed = 10
water_temperature = 22

# Condition checks
can_go_hiking = is_sunny == True and temperature > 15 and wind_speed < 20
can_go_swimming = is_sunny == True and temperature > 20 and water_temperature > 18
cannot_go_outside = is_sunny == False and temperature < 10 or wind_speed > 30

print("Can go hiking:", can_go_hiking)
print("Can go swimming:", can_go_swimming)
print("Cannot go outside:", cannot_go_outside)


# --- Exercise 3: Pet Shop Licensing Logic ---
has_license = True
has_space = True
has_experience = False

# Evaluating complex business requirements
can_sell_regular_pet = (has_license == True or has_experience == True) and has_space == True
can_sell_exotic_pet = (has_license == True and has_experience == True) and has_space == True
cannot_sell_any_pet = (has_license == False and has_experience == False) or has_space == False

print("Can sell regular pet:", can_sell_regular_pet)
print("Can sell exotic pet:", can_sell_exotic_pet)
print("Cannot sell any pet:", cannot_sell_any_pet)
