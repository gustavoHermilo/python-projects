# Filter even numbers using list comprehension


def filter_even_numbers(numbers):
    """
    Returns a list with only even numbers from the input list
    """
    return [n for n in numbers if n % 2 == 0]


def main():
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [int(n) for n in user_input.split()]

        even_numbers = filter_even_numbers(numbers)

        print("Even numbers:", even_numbers)

    except ValueError:
        print("Invalid input. Please enter only integers.")


if __name__ == "__main__":
    main()
