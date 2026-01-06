#Prime Factorization
#The program asks the user for a number
# and prints all of its prime factors

def prime_factors(n):
    factors=[]

    #Start dividing by the smallest prime number
    divisor=2

    while n>1:
        if n%divisor ==0:
            factors.append(divisor)
            n//= divisor #reduce n
        else :
            divisor += 1
    return factors

def main():
    try:
        number = int(input("Enter a number: "))

        if number <= 1:
            print("Please enter a numer greater than 1.")
            return
        factors=prime_factors(number)

        print (f"Prime factors of {number}:")
        print(factors)

    except ValueError:
        print("Invalid input.Please enter an integer.")

if __name__=="__main__":
    main()
