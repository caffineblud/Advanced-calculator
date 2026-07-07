import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base, exponent):
    return math.pow(base, exponent)


def nth_root(value, n):
    if n == 0:
        raise ValueError("Root order cannot be zero.")
    if value < 0 and n % 2 == 0:
        raise ValueError("Even root of a negative number is not supported in real numbers.")
    return value ** (1 / n)


def logarithm(value, base=10):
    if value <= 0:
        raise ValueError("Logarithm input must be greater than zero.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(value, base)


def factorial(n):
    if n < 0 or not float(n).is_integer():
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(int(n))


def percentage(part, whole):
    if whole == 0:
        raise ValueError("Whole value cannot be zero when calculating percentage.")
    return (part / whole) * 100


def degrees_to_radians(degrees):
    return math.radians(degrees)


def sine(degrees):
    return math.sin(degrees_to_radians(degrees))


def cosine(degrees):
    return math.cos(degrees_to_radians(degrees))


def tangent(degrees):
    return math.tan(degrees_to_radians(degrees))


def exponential(value):
    return math.exp(value)


def safe_eval(expression):
    allowed_names = {
        name: obj
        for name, obj in math.__dict__.items()
        if not name.startswith("__")
    }
    allowed_names.update(
        {
            "abs": abs,
            "round": round,
            "pow": pow,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
        }
    )
    return eval(expression, {"__builtins__": None}, allowed_names)


def get_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def get_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")


def print_menu():
    print("\nAdvanced Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Nth root")
    print("7. Factorial")
    print("8. Logarithm")
    print("9. Trigonometry (degrees)")
    print("10. Percentage")
    print("11. Exponential (e^x)")
    print("12. Evaluate custom expression")
    print("0. Exit")


def main():
    history = []

    while True:
        print_menu()
        choice = input("Choose an operation: ").strip()

        try:
            if choice == "0":
                print("Goodbye!")
                break

            elif choice == "1":
                a = get_float("Enter first number: ")
                b = get_float("Enter second number: ")
                result = add(a, b)
                print(f"Result: {result}")

            elif choice == "2":
                a = get_float("Enter first number: ")
                b = get_float("Enter second number: ")
                result = subtract(a, b)
                print(f"Result: {result}")

            elif choice == "3":
                a = get_float("Enter first number: ")
                b = get_float("Enter second number: ")
                result = multiply(a, b)
                print(f"Result: {result}")

            elif choice == "4":
                a = get_float("Enter dividend: ")
                b = get_float("Enter divisor: ")
                result = divide(a, b)
                print(f"Result: {result}")

            elif choice == "5":
                base = get_float("Enter base: ")
                exponent = get_float("Enter exponent: ")
                result = power(base, exponent)
                print(f"Result: {result}")

            elif choice == "6":
                value = get_float("Enter value: ")
                n = get_float("Enter root order: ")
                result = nth_root(value, n)
                print(f"Result: {result}")

            elif choice == "7":
                n = get_int("Enter a non-negative integer: ")
                result = factorial(n)
                print(f"Result: {result}")

            elif choice == "8":
                value = get_float("Enter value (> 0): ")
                base = get_float("Enter logarithm base (default 10): ")
                result = logarithm(value, base)
                print(f"Result: {result}")

            elif choice == "9":
                angle = get_float("Enter angle in degrees: ")
                print("a. sine")
                print("b. cosine")
                print("c. tangent")
                trig_choice = input("Choose a trig function: ").strip().lower()
                if trig_choice == "a":
                    result = sine(angle)
                elif trig_choice == "b":
                    result = cosine(angle)
                elif trig_choice == "c":
                    result = tangent(angle)
                else:
                    print("Unknown trigonometry option.")
                    continue
                print(f"Result: {result}")

            elif choice == "10":
                part = get_float("Enter the part value: ")
                whole = get_float("Enter the whole value: ")
                result = percentage(part, whole)
                print(f"Result: {result}%")

            elif choice == "11":
                value = get_float("Enter exponent value: ")
                result = exponential(value)
                print(f"Result: {result}")

            elif choice == "12":
                expression = input(
                    "Enter an expression using numbers and math functions (sin, cos, tan, sqrt, log, exp): "
                ).strip()
                result = safe_eval(expression)
                print(f"Result: {result}")

            else:
                print("Invalid choice. Please choose a valid operation.")
                continue

            history.append(result)
            print(f"History ({len(history)} results): {history}")

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
