power = int(input("Enter the power to print upto: "))
for x in range(1, power + 1):
    print("2 raised to the power", x, "is", (lambda x: int(2 ** x))(x))
