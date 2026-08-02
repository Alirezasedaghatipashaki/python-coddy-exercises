# ==========================================
# Day 5: Comparison & Logical Operators
# Platform: Coddy Practice
# ==========================================

# --- Exercise 1: Basic Multiplication & Variable Assignment ---
a = 8
b = 3
c = b * a
print(f'c = {c}')


# --- Exercise 2: Greater Than Comparison (>) ---
n1 = 8
n2 = 9
n3 = n1 > n2  # Evaluates to False because 8 is not greater than 9

print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}")


# --- Exercise 3: Logical AND Operator (and) ---
age = 20
has_license = True

# Both conditions must be True for result to be True
result = age >= 18 and has_license

print("Eligible to drive:", result)


# --- Exercise 4: Less Than or Equal To Comparison (<=) ---
x = 15
y = 10
z = x <= y  # Evaluates to False because 15 is not less than or equal to 10

print(f"x = {x}, y = {y}, z = {z}")
