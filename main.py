string = "Hello, World!"
vowels = "aeiou"
count = 0
for char in string.lower():
    if char in vowels:
        count += 1
print("Количество гласных букв:", count)
