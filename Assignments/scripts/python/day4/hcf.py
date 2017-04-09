def hcf(x,y):

	while(y > 0):
		x, y = y, x % y

	print("HCF is: ",x)

num1 = int(input("Enter first number:  "))
num2 = int(input("Enter second number: "))

if num1 > num2:
	hcf(num1, num2)
else:
	hcf(num2, num1)
