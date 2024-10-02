# Prompting the user to give me their numeric grade
grade = int(input("What is your numeric grade in the class?\nNumeric grade: "))

# Using grade scale to find letter grade
if grade >= 0: # Checking if the number is more than or equal to 0
    if grade <= 100: # Checking if the number is less than or equal to 100
        if grade >= 90: # Printing an "A" letter grade if grade is between 90-100 
            print("You got an A")
        elif grade >= 80: # Printing a "B" letter grade if grade is between 80-89
            print("You got a B")
        elif grade >= 70: # Printing a "C" letter grade if grade is between 70-79
            print("You got a C")
        elif grade >= 60: # Printing a "D" letter grade if grade is between 60-69
            print("You got a D")
        else:
            print("You got an F") # Printing an "F" letter grade if grade is betwee 0-59
    else:
        print("How much extra credit did you do?") # Printing if somehow they got more than 100
else:
    print("How can you get a negative grade?") # Printing if somehow they got less than 0           