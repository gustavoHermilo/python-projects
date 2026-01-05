MAX_TERMS = 150    #safety limit

def generate_fibonacci(n):
    sequence = []
    a,b = 0,1

    for _ in range(n):
        sequence.append(a)
        a,b= b,a +b
    return sequence

def main():
    try:
        n= int(input ("Enter the number of Fibonacci terms:"))

        if n<0:
            print("Number must be non-negative.")
            return
        if n>MAX_TERMS :
            print(f"Maximum allowed term is {MAX_TERMS}." )
            return

        fib_sequence=generate_fibonacci(n)
        print("Fibonacci sequence")
        print(fib_sequence)

    except ValueError:
        print ("Invalid input.Please enter an integer.")

if __name__=="__main__":
    main()
