# String Questions:

# Q1
name = str(input('What is your name?'))
year = int(input("When are you born?(year): "))
age = 2025 - year
print(f"{name} is {age} years old.")

# Q2
txt = 'LMaasleitbtui'
print(txt[1:3] + txt[5] + txt[7] + txt[9] + txt[11])
print(txt[0] + txt[3] + txt[4] + txt[6] + txt[8] + txt[12])

# Q3
inpt12 = str(input("Enter a string:"))
print(len(inpt12))
upperCase = inpt12.upper()
lowerCase = inpt12.lower()
print(upperCase)
print(lowerCase)

# Q4
print(inpt12 == inpt12[::-1])

# Q5
string1 = "bsaiekcGWekKlJeud"
vowels = 'eiouaOIEAU'
count = sum(string1.count(vowel) for vowel in vowels)
print(count)
print(len(string1) - count)

# Q6
print('eu' in string1)

# Q7
sentence = str(input("Enter sentence: "))
replace = str(input("Enter word which you want replace: "))
newWord = str(input("Enter word which you want replace with: "))
print(sentence.replace(replace, newWord))

# Q8
print(inpt12[0])
print(inpt12[-1])

# Q9
print(inpt12[::-1])

# Q10
print(len(sentence.split()))

# Q11
print(any(char.isdigit() for char in inpt12))

# Q12
words = ["apple", "banana", "cherry"]
separator = "-"
print(separator.join(words))

# Q13
print(inpt12.replace(" ", ""))

# Q14
string11 = input()
string12 = input()
print(string11 == string12)

# Q15
print("".join(word[0].upper() for word in sentence.split()))

# Q16
input14 = str(input("Enter a string: "))
character11 = str(input("Enter a character to remove: "))
print(input14.replace(character11, ""))

# Q17
print("".join("*" if char in vowels else char for char in input14))

# Q18
inpt18 = input("Enter a sentence: ")
begin = input("Enter the beginning word of the sentence: ")
end = input("Enter the ending word of the sentence: ")
if inpt18.startswith(begin) and inpt18.endswith(end):
    print("True")
else:
    print("False")