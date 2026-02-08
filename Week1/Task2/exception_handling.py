def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return None, None


def addition():
    num1, num2 = get_numbers()
    if num1 is not None:
        print("Result:", num1 + num2)


def subtract():
    num1, num2 = get_numbers()
    if num1 is not None:
        print("Result:", num1 - num2)


def product():
    num1, num2 = get_numbers()
    if num1 is not None:
        print("Result:", num1 * num2)


def division():
    num1, num2 = get_numbers()
    if num1 is not None:
        try:
            print("Result:", num1 / num2)
        except ZeroDivisionError:
            print("Cannot divide by zero!")


def main():
    while True:
        print("\n----- Select Operation -----")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addition()
        elif choice == "2":
            subtract()
        elif choice == "3":
            product()
        elif choice == "4":
            division()
        elif choice == "5":
            print("Program terminated successfully!")
            break
        else:
            print("Invalid choice. Try again.")


main()
