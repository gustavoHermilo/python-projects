from decimal import Decimal, getcontext

MAX_DIGITS = 150

def compute_e(n):
    #Set precision slightly higher to ensure correct rounding
    getcontext().prec=n+2

    e=Decimal(1)
    factorial=Decimal(1)
    k=1

    while k<n*3:
        factorial*=k
        e += Decimal(1)/ factorial
        k+= 1
    return e

def main():
    try:
        n= int(input("Enter number of decimal places:"))

        if n<0:
            print("Number must be non-negative")
            return
        if n> MAX_DIGITS:
            print(f"Maximum allowed digits is {MAX_DIGITS}")
            return

        e_value= compute_e(n)

        print(f"e to {n} decimal places:")
        print(round(e_value,n))
    except ValueError:
        print("Invalied input .Please enter an integer .")

if __name__=="__main__":
    main()
