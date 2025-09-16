# Python program to find the length of a dictionary.
def dict_length():
    d = eval(input("Enter a dictionary: "))
    print("Length of dictionary:", len(d))

# Python program to check if a given key exists in a dictionary.
def check_key_exists():
    d = eval(input("Enter a dictionary: "))
    key = input("Enter the key to check: ")
    print(f"Key '{key}' exists?" , key in d)

# Python program to count the occurrences of each word in a string and store them in a dictionary.
def word_count_to_dict():
    text = input("Enter a string: ")
    words = text.split()
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1
    print("Word count dictionary:", count_dict)

# Python program to merge two dictionaries.
def merge_dictionaries():
    d1 = eval(input("Enter first dictionary: "))
    d2 = eval(input("Enter second dictionary: "))
    merged = {**d1, **d2}
    print("Merged dictionary:", merged)

# Python program to multiply all values in a dictionary by a certain number.
def multiply_values():
    d = eval(input("Enter a dictionary with numeric values: "))
    factor = float(input("Enter a multiplication factor: "))
    multiplied = {k: v*factor for k, v in d.items()}
    print("Dictionary after multiplication:", multiplied)

# Python program to sort a dictionary by its values.
def sort_dict_by_values():
    d = eval(input("Enter a dictionary with numeric values: "))
    sorted_items = sorted(d.items(), key=lambda x: x[1])
    print("Sorted dictionary by values:", dict(sorted_items))

# Python program to find the keys corresponding to the maximum and minimum values in a dictionary.
def max_min_keys():
    d = eval(input("Enter a dictionary with numeric values: "))
    max_key = max(d, key=d.get)
    min_key = min(d, key=d.get)
    print(f"Key with maximum value: {max_key}")
    print(f"Key with minimum value: {min_key}")

# Python program to remove a specific key-value pair from a dictionary.
def remove_key():
    d = eval(input("Enter a dictionary: "))
    key = input("Enter key to remove: ")
    removed = d.pop(key, None)
    if removed is not None:
        print(f"Key '{key}' removed. Updated dictionary: {d}")
    else:
        print(f"Key '{key}' not found. Dictionary unchanged: {d}")

# Python program to find the sum of all values in a dictionary.
def sum_of_values():
    d = eval(input("Enter a dictionary with numeric values: "))
    total = sum(d.values())
    print("Sum of all values:", total)

# Python program to check if two dictionaries have the same keys.
def same_keys_check():
    d1 = eval(input("Enter first dictionary: "))
    d2 = eval(input("Enter second dictionary: "))
    print("Do both dictionaries have the same keys?", d1.keys() == d2.keys())

if __name__ == "__main__":
    programs = {
        "1": ("Length of a dictionary", dict_length),
        "2": ("Check if a key exists in dictionary", check_key_exists),
        "3": ("Count occurrences of words in string", word_count_to_dict),
        "4": ("Merge two dictionaries", merge_dictionaries),
        "5": ("Multiply all values in a dictionary", multiply_values),
        "6": ("Sort a dictionary by values", sort_dict_by_values),
        "7": ("Find keys of max and min values", max_min_keys),
        "8": ("Remove a specific key-value pair", remove_key),
        "9": ("Sum of all values in dictionary", sum_of_values),
        "10": ("Check if two dictionaries have the same keys", same_keys_check),
    }

    print("\nSelect a program to run:")
    for key, (desc, _) in programs.items():
        print(f"{key}. {desc}")

    choice = input("\nEnter your choice (1-10): ").strip()
    if choice in programs:
        programs[choice][1]()  # Call the chosen function
    else:
        print("Invalid choice.")