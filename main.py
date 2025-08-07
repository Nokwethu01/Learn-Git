def greet_user(name):
    """Greets the user by name."""
    return f"Hello, {name}! Welcome to the project."

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def main():
    user_name = input("Enter your name: ")
    print(greet_user(user_name))

    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = add_numbers(x, y)
        print(f"The sum of {x} and {y} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")
        


main()

