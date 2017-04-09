from math import sqrt
num = int(input("Enter Number: "))
chkRange = int(sqrt(num))
factors = 0

for i in range(2, chkRange + 1):
	if num % i == 0:
		factors += 1

if factors > 0:
	print ("{0:d} is not prime.".format(num))
else:
	print ("{0:d} is prime.".format(num))