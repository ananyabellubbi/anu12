num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print("Addition", addition)
print("Subtraction", subtraction)
print("Multiplication", multiplication)

if num2 != 0:
    division = num1 / num2
    print("Division", division)
else:
    print("Division is not possible")
    
