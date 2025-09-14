# Python program to find the intersection of two sets.
def set_intersection():
    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())
    print("Intersection:", set1 & set2)

# Python program to find the union of two sets.
def set_union():
    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())
    print("Union:", set1 | set2)

# Python program to find the difference between two sets.
def set_difference():
    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())
    print("Difference (set1 - set2):", set1 - set2)

# Python program to check if a set is a subset of another set.
def is_subset():
    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())
    print("Is set1 a subset of set2?", set1 <= set2)

# Python program to remove duplicates from a list and convert it to a set.
def remove_duplicates_to_set():
    lst = input("Enter elements of list separated by space: ").split()
    s = set(lst)
    print("Set after removing duplicates:", s)

# Python program to find the symmetric difference between two sets.
def symmetric_difference():
    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())
    print("Symmetric difference:", set1 ^ set2)

# Python program to check if two sets are disjoint.
def are_disjoint():
    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())
    print("Are sets disjoint?", set1.isdisjoint(set2))

# Python program to find the Cartesian product of two sets.
def cartesian_product():
    set1 = input("Enter elements of first set separated by space: ").split()
    set2 = input("Enter elements of second set separated by space: ").split()
    product = [(a, b) for a in set1 for b in set2]
    print("Cartesian product:", product)

# Python program to perform set operations (union, intersection, difference) using set methods.
def set_operations_methods():
    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())
    print("Union:", set1.union(set2))
    print("Intersection:", set1.intersection(set2))
    print("Difference (set1 - set2):", set1.difference(set2))

# Python program to check if a set is a proper subset of another set.
def is_proper_subset():
    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())
    print("Is set1 a proper subset of set2?", set1 < set2)

if __name__ == "__main__":
    programs = {
        "1": ("Intersection of two sets", set_intersection),
        "2": ("Union of two sets", set_union),
        "3": ("Difference between two sets", set_difference),
        "4": ("Check if a set is subset of another", is_subset),
        "5": ("Remove duplicates from list → set", remove_duplicates_to_set),
        "6": ("Symmetric difference between two sets", symmetric_difference),
        "7": ("Check if two sets are disjoint", are_disjoint),
        "8": ("Cartesian product of two sets", cartesian_product),
        "9": ("Set operations using methods", set_operations_methods),
        "10": ("Check if a set is a proper subset", is_proper_subset),
    }

    print("\nSelect a program to run:")
    for key, (desc, _) in programs.items():
        print(f"{key}. {desc}")

    choice = input("\nEnter your choice (1-10): ").strip()
    if choice in programs:
        programs[choice][1]()  # Call the chosen function
    else:
        print("Invalid choice.")