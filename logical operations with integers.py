# Prompting user to enter two integer numbers.
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))


#running input number through these comparison operations and seeing if they are True or False.       
print("Both are greater than 5:", num1 > 5 and num2 > 5)

print("Both are less than 100:", num1 < 100 and num2 < 100)

print("Are either of them even numbers?", num1 % 2 == 0 or num2 % 2 ==0)

print("Are either of their square roots greater than 0?", num1 ** 0.5 > 0 or num2 ** 0.5 > 0)

print("Is num1 not equal to num2?", not num1 == num2)

print("num2 is not equal to the number 2?", not num2 == 2)
