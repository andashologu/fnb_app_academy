num1 = int(input("Enter the first number: ")) # ask for user input
num2 = int(input("Enter second number: ")) # ask for user input

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("both number are equal")