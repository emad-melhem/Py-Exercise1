x = input("Inter your number :")
try:
    val = int(x)
    if val % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
    print("That's not a Number!")