#Assignment 3.1
hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter Rate per hour:")
r = float(rph)
if h > 40:
    g = h - 40
    pay = (40 * r) + (g * r * 1.5)
else:
    pay = (h * r)

print(pay)