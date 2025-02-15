# Boolean Data Type Questions:

# Q1
username = input("Enter username:")
password = input("Enter password:")
if password and username:
    print("welcome")
else:
    print("please enter both username and password")

# Q2
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
print(a == b)

# Q3
print(0 < a)
print(a % 2 == 0)

# Q4
c = int(input("Enter number for c:"))
print(a != b and b != c and a != c)

# Q5
string1 = input("Enter a string:")
string2 = input("Enter another string:")
length1 = len(string1)
length2 = len(string2)
print(length1 == length2)

# Q6
print(a % 3 == 0 and a % 5 == 0)

# Q7
print(a + b > 50.8)
print(10 <= a <= 20)