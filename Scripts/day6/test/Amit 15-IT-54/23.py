def HCF(x,y):

	while(y > 0):
		x, y = y, x % y

	return x

num1 = int(input("Enter first number:  "))
num2 = int(input("Enter second number: "))
hcf=0

if num1 > num2:
	hcf=HCF(num1, num2)
else:
	hcf=HCF(num2, num1)

lcm = (num1 * num2) / hcf

print("LCM is: ", int(lcm))
