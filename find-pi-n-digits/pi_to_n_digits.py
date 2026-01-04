from decimal import Decimal, getcontext
MAX_DIGITS= 150     #safety limit

def compute_pi(n):
    getcontext().prec= n+2     #extra precision for rounding
    pi=Decimal(0)
    k=0

    while k<n*5:
        pi += (Decimal(1)/(16**k)) * (
                Decimal(4)/(8*k+1)-
                Decimal(2)/(8*k+4)-
                Decimal(1)/(8*k+5)-
                Decimal(1)/(8*k+6)
        )
        k+=1

    return pi
def main():
    try:
        n= int(input("Enter number of decimal places="))

        if n<0:
            print("Number must be non-negative.")
            return
        if n>MAX_DIGITS:
            print(f"Maximun allowed digits is {MAX_DIGITS}.")
            return

        pi_value= compute_pi(n)
        print (f"PI to {n} decimal places:")
        print(round (pi_value,n))

    except ValueError:
        print("Invalid input.Please enter an integer")

if __name__=="__main__":
    main()
