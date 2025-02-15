# Number Data Type Questions:
# Q1
userInput = float(input("Enter float number:"))
roundedNumber = round(userInput, 2)
print(roundedNumber)

# Q2
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

print ("Largest number is:", max(num1, num2, num3))
print ("Smallest number is:", min(num1, num2, num3))

# Q3
km = float(input("Enter distance (in km):"))
m = km * 1000
cm = km * 100000
print(f"{m} meter")
print(f"{cm} centimeter")

# Q4
dividend = int(input("Enter dividend:"))
divisor = int(input("Enter divisor:"))
print(f"Quotient is {dividend // divisor}, remainder is {dividend % divisor}")

# Q5
celci = float(input("Enter temperature in celcius:"))
fahrenheit = (celci * 9/5) + 32
print("Temperature in fahrenheit is:", fahrenheit)

# Q6
number1 = int(input("Enter a number:"))
print(number1 % 10)

# Q7
userInput1= int(input("Enter a number:"))
condition = userInput1 % 2
if condition == 0:
    print("Number is even")
else:
    print("Number is not even")