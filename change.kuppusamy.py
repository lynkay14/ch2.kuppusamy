# change.kuppuamy.py
# This program calculates the total value of coins in USD
# includes the defined variable of rare half-dollar

def main():
    print("Quick Change Counter")
    print()
    print("Enter the number of each coin type.")
    halfdollar=eval(input("Half-Dollars"))
    quarters=eval(input("Quarters"))
    dimes=eval(input("Dimes:"))
    nickels=eval(input("Nickels:"))
    pennies=eval(input("Pennies:"))
    total=halfdollar * .5 + quarters * .25  + dimes * .10 + nickels * .05 + pennies * .01
    print()
    print("The total value of your coins is", total)

main()