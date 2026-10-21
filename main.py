def check_number():
    """1. If the entered number is greater than 7, print 'Hello'."""
    try:
        num = float(input("Enter a number: "))
        if num > 7:
            print("Hello")
    except ValueError:
        print("Error: Please enter a valid number.")


def check_name():
    """2. If the entered name matches 'John', print 'Hello, John', otherwise print 'There is no such name'."""
    name = input("Enter a name: ").strip()
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")


def check_array_multiples_of_three():
    """3. Given a numeric array, output the elements that are multiples of 3."""
    user_input = input("Enter array numbers separated by spaces: ").strip()
    if not user_input:
        print("The array is empty.")
        return

    try:
        array = [int(x) for x in user_input.split()]
        multiples_of_three = [num for num in array if num % 3 == 0]
        print("Elements that are multiples of 3:", multiples_of_three)
    except ValueError:
        print("Error: Array elements must be integers.")


def main():
    print("=== TASK 1: Number Check ===")
    check_number()
    print("\n=== TASK 2: Name Check ===")
    check_name()
    print("\n=== TASK 3: Array Filtering ===")
    check_array_multiples_of_three()


if __name__ == "__main__":
    main()
