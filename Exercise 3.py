x = input("Inter your number 1 :")
y = input("Inter your number 2 :")
try:
    val1 = int(x)
    val2 = int(y)
    if val1 * val2 <= 1000:
        print("The result is", val1 * val2)
    else:
        print("The result is", val1 + val2)
except ValueError:
    print("That's not a Number!")