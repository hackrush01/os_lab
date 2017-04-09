import string

String = input("Enter the String: ").translate(
    str.maketrans('', '', string.punctuation))
print ("The new string is:", String)
