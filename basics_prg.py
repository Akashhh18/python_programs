# Python program to find the minimum among five numbers.
def find_minimum_of_five():
    numbers = [float(input(f"Enter number {i+1}: ")) for i in range(5)]
    print("Minimum is:", min(numbers))

#Python program to check if a given number is prime or not.
def check_prime():
    num = int(input("Enter the number: "))
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

#Python program to calculate the area of a triangle given its three sides.
def triangle_area():
    a = int(input("Enter side 1: "))
    b = int(input("Enter side 2: "))
    c = int(input("Enter side 3: "))
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("Area of the triangle is:", area)

#Python program to swap two numbers without using a temporary variable.
def swap_two_numbers():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    x, y = y, x
    print(f"After swapping: x={x}, y={y}")

#Python program to find the sum of natural numbers up to a given number.
def sum_of_natural_numbers():
    n = int(input("Enter a positive number: "))
    print("Sum is:", n * (n + 1) // 2)

#Python program to check if a number is even or odd.
def even_or_odd():
    n = int(input("Enter a number: "))
    print("Even" if n % 2 == 0 else "Odd")

#Python program to calculate the square root of a number.

def square_root():
    n = int(input("Enter a number: "))
    print("Square root is:", n ** 0.5)

#Python program to calculate the average of three numbers.
def average_of_three():
    p = int(input("Enter number 1: "))
    q = int(input("Enter number 2: "))
    r = int(input("Enter number 3: "))
    print("Average is:", (p + q + r) / 3)

#Python program to check if a given year is a leap year or not.
def check_leap_year():
    year = int(input("Enter the year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


if __name__ == "__main__":
    programs = {
        "1": ("Find minimum of 5 numbers", find_minimum_of_five),
        "2": ("Check prime", check_prime),
        "3": ("Triangle area", triangle_area),
        "4": ("Swap 2 numbers", swap_two_numbers),
        "5": ("Sum of natural numbers", sum_of_natural_numbers),
        "6": ("Even or odd", even_or_odd),
        "7": ("Square root", square_root),
        "8": ("Average of 3 numbers", average_of_three),
        "9": ("Check leap year", check_leap_year),
    }

    print("\nSelect a program to run:")
    for key, (desc, _) in programs.items():
        print(f"{key}. {desc}")

    choice = input("\nEnter your choice (1-9): ").strip()
    if choice in programs:
        programs[choice][1]()  # Call the chosen function
    else:
        print("Invalid choice.")
