#futval.hw.kuppusamy.py
# a program to compute the value of an investment
# carried n years into the future

def main():
    print("This program calculates the future value")
    print("of an investment over an input number of years.")

    n = eval(input("How many years to calculate?"))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(n):
        principal = principal * (1 + apr)
    print("The value in", n, "years is", principal)

main()

