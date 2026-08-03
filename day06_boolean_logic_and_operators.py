# ==========================================
# Day 6: Advanced Boolean Logic (and, or, not)
# Platform: Coddy Practice
# ==========================================

# --- Exercise 1: Logical AND with Booleans ---
x1 = True
x2 = False
x3 = x1 and x2  # Evaluates to False because one side is False

print(f"x3 = {x3}")


# --- Exercise 2: Combining Math and Comparison Operators ---
b1 = 5
b2 = 10

# Checks if product (50) is greater than sum (15) -> True
b3 = (b1 * b2) > (b1 + b2)

print(f"b3 = {b3}")


# --- Exercise 3: Complex Logic with 'or' and 'not' ---
a = True
b = False
c = False

# (True or False) -> True
# not False -> True
# True and True -> True
result = (a or b) and not c

print(f"result = {result}")


# --- Exercise 4: Chaining Logical Operators ---
b1 = True
b2 = True
b3 = False

# True and True and True -> True
b4 = b1 and b2 and (not b3)

print(f"b4 = {b4}")
