# ==========================================
# Day 4: Modulo Operator (%) & Assignment Operators
# Platform: Coddy Practice
# ==========================================

# --- Exercise 1: Modulo Operator Basics (%) ---
a = 9
b = 2
c = 11

d = a % 2   # 9 divided by 2 has remainder 1
e = b % 3   # 2 divided by 3 has remainder 2
f = c % 10  # 11 divided by 10 has remainder 1

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")
print(f"e = {e}")
print(f"f = {f}")


# --- Exercise 2: Advanced Modulo Operations ---
x = 15
y = 4
z = 23

w = x % y   # 15 % 4 = 3
v = z % x   # 23 % 15 = 8
u = z % y   # 23 % 4 = 3

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"w = {w}")
print(f"v = {v}")
print(f"u = {u}")


# --- Exercise 3: Augmented Assignment Operators (+=, *=, -=) ---
count = 0
count += 4  # Equivalent to: count = count + 4 -> 4
count *= 2  # Equivalent to: count = count * 2 -> 8
count -= 1  # Equivalent to: count = count - 1 -> 7

print(f"count = {count}")


# --- Exercise 4: Division Assignment Operator (/=) ---
score = 100
score /= 2  # Equivalent to: score = score / 2 -> 50.0 (Floats result)
score += 10 # score = 60.0
score *= 3  # score = 180.0

print(f"score = {score}")
