x = input("Input a numer between 100-999 :")
try:
    val1 = int(x)
    if val1 <100 or val1 > 999:
        raise IndexError("Number is out of range!")
    y = x[::-1]
    print(f"The reverse is {y}.")
except ValueError:
    print("That's not a Number!")
except IndexError as indexerror:
    print(indexerror.args[0])