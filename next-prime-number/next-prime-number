#Next Prime Number
#The program keeps generating prime numbers
#until the user decides to stop

def is_prime(n):
    if n<2:
        return False
    for i in  range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    current = 1

    while True:
        user_input= input("Press Enter for next prime or type 'q' to quit:")

        if user_input.lower()=='q':
            print("Program stopped.")
            break

        current +=1
        while not is_prime(current):
            current+=1

        print(f"Next prime:{current}")

if __name__=="__main__":
    main()
