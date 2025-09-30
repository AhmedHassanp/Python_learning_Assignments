#Assignment 3.2
score = input("Enter Score:")

try:
    scr = float(score)
except:
    print("Enter correct score.")
    quit()

if scr > 1.0:
    print("Out of range.")
else:    
    if scr >= 0.9:
        grade = "A"
    elif scr >= 0.8:
        grade = "B"
    elif scr >= 0.7:
        grade = "C"
    elif scr >= 0.6:
        grade = "D"
    else:
        grade = "F"
    
    print (grade)