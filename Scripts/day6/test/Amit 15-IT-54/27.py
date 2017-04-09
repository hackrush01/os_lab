string = input("Enter a string: ")
rev = string[::-1]

if rev == string:
	print("The string is palindromic")
else:
	print("The string is not palindromic")
