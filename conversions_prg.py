# Python program to convert a string to a list of characters.
def string_to_char_list():
    s = input("Enter a string: ")
    char_list = list(s)
    print("List of characters:", char_list)

# Python program to convert a list of characters to a string.
def char_list_to_string():
    chars = input("Enter characters separated by space: ").split()
    s = ''.join(chars)
    print("String:", s)

# Python program to convert a decimal number to binary, octal, and hexadecimal.
def decimal_to_bin_oct_hex():
    num = int(input("Enter a decimal number: "))
    print(f"Binary: {bin(num)[2:]}")
    print(f"Octal: {oct(num)[2:]}")
    print(f"Hexadecimal: {hex(num)[2:]}")

# Python program to convert temperature from Fahrenheit to Celsius.
def fahrenheit_to_celsius():
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"Temperature in Celsius: {c}")

# Python program to convert distance from kilometers to miles and vice versa.
def km_miles_conversion():
    choice = input("1. km to miles \n2. miles to km \n Enter your choice: ").strip()
    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} km = {miles} miles")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        km = miles / 0.621371
        print(f"{miles} miles = {km} km")
    else:
        print("Invalid choice.")

# Python program to convert a string to a dictionary where each character is a key and its frequency is the value.
def string_to_char_frequency_dict():
    s = input("Enter a string: ")
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    print("Character frequency dictionary:", freq)

# Python program to convert a list of tuples to a dictionary.
def list_of_tuples_to_dict():
    tuples_list = eval(input("Enter a list of tuples: ")) #format : (e.g. [('a',1),('b',2)])
    d = dict(tuples_list)
    print("Dictionary:", d)

# Python program to convert a dictionary to a list of tuples.
def dict_to_list_of_tuples():
    d = eval(input("Enter a dictionary: ")) #format:  (e.g. {'a':1,'b':2})
    tuples_list = list(d.items())
    print("List of tuples:", tuples_list)

# Python program to convert a binary number to decimal.
def binary_to_decimal():
    binary = input("Enter a binary number: ")
    try:
        decimal = int(binary, 2)
        print(f"Decimal: {decimal}")
    except ValueError:
        print("Invalid binary number.")

# Python program to convert a list of integers to a string representation of the binary numbers.
def list_of_integers_to_binary_string():
    nums = list(map(int, input("Enter integers separated by space: ").split()))
    binary_list = [bin(num)[2:] for num in nums]
    print("Binary strings:", binary_list)

if __name__ == "__main__":
    programs = {
        "1": ("String -> List of characters", string_to_char_list),
        "2": ("List of characters -> String", char_list_to_string),
        "3": ("Decimal -> Binary, Octal, Hexadecimal", decimal_to_bin_oct_hex),
        "4": ("Fahrenheit -> Celsius", fahrenheit_to_celsius),
        "5": ("Kilometers <- -> Miles conversion", km_miles_conversion),
        "6": ("String -> Character frequency dictionary", string_to_char_frequency_dict),
        "7": ("List of tuples -> Dictionary", list_of_tuples_to_dict),
        "8": ("Dictionary -> List of tuples", dict_to_list_of_tuples),
        "9": ("Binary -> Decimal", binary_to_decimal),
        "10": ("List of integers -> Binary strings", list_of_integers_to_binary_string),
    }

    print("\nSelect a program to run:")
    for key, (desc, _) in programs.items():
        print(f"{key}. {desc}")

    choice = input("\nEnter your choice (1-10): ").strip()
    if choice in programs:
        programs[choice][1]()  # Call the chosen function
    else:
        print("Invalid choice.")