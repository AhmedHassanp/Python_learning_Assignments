#Assignment 4.6
def computepay(h,r):
    h = float(h)
    r = float(r)
    if h > 40:
        g = h - 40
        pay = (40 * r) + (g * r * 1.5)
        return pay
    else:
        pay = h * r
        return pay
    
hrs = input("Enter Hours:")
rph = input("Enter Rate")

p = computepay(hrs,rph)

print("Pay",p)