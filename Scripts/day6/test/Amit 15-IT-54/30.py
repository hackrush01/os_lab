string = input("Enter a string: ")
count = 0

for char in string:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print("Number of vowels are:", count)
