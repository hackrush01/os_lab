num = input("Enter a number: ")
nod = len(num)
num = int(num)
temp = num
res = 0

while temp > 0:
    res = res + (temp % 10) ** nod
    temp = int(temp / 10)

if res == num:
    print("{0:d} is an Armstrong number".format(num))
else:
    print("{0:d} is not an Armstrong number".format(num))
