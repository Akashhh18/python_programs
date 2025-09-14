# Python program to find the maximum and minimum elements in a tuple.
def max_min_tuple():
    t = tuple(map(int, input("Enter elements of tuple separated by space: ").split()))
    print("Maximum:", max(t))
    print("Minimum:", min(t))

# Python program to concatenate two tuples.
def concatenate_tuples():
    t1 = tuple(input("Enter elements of first tuple separated by space: ").split())
    t2 = tuple(input("Enter elements of second tuple separated by space: ").split())
    concatenated = t1 + t2
    print("Concatenated tuple:", concatenated)

# Python program to find the index of a given item in a tuple.
def index_of_item():
    t = tuple(input("Enter elements of tuple separated by space: ").split())
    item = input("Enter item to find index of: ")
    try:
        index = t.index(item)
        print(f"Index of {item}: {index}")
    except ValueError:
        print(f"{item} not found in tuple.")

# Python program to count the occurrences of a specific element in a tuple.
def count_element_occurrences():
    t = tuple(input("Enter elements of tuple separated by space: ").split())
    element = input("Enter element to count: ")
    count = t.count(element)
    print(f"{element} occurs {count} times in the tuple.")

# Python program to find the product of elements in a tuple.
def product_of_elements():
    t = tuple(map(int, input("Enter integer elements of tuple separated by space: ").split()))
    product = 1
    for num in t:
        product *= num
    print("Product of elements:", product)

# Python program to find the length of the longest increasing subsequence in a tuple of integers.
def length_of_longest_increasing_subseq():
    t = tuple(map(int, input("Enter integer elements of tuple separated by space: ").split()))
    if not t:
        print("Tuple is empty.")
        return
    # Dynamic programming approach
    dp = [1] * len(t)
    for i in range(1, len(t)):
        for j in range(i):
            if t[i] > t[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print("Length of longest increasing subsequence:", max(dp))

# Python program to find the frequency of each element in a tuple.
def frequency_of_elements():
    t = tuple(input("Enter elements of tuple separated by space: ").split())
    freq = {}
    for item in t:
        freq[item] = freq.get(item, 0) + 1
    print("Frequency of each element:", freq)

# Python program to find the index of the first occurrence of a given element in a tuple.
def first_occurrence_index():
    t = tuple(input("Enter elements of tuple separated by space: ").split())
    element = input("Enter element to find first occurrence: ")
    try:
        index = t.index(element)
        print(f"First occurrence index of {element}: {index}")
    except ValueError:
        print(f"{element} not found in tuple.")

# Python program to check if two tuples have the same elements.
def check_same_elements():
    t1 = tuple(input("Enter elements of first tuple separated by space: ").split())
    t2 = tuple(input("Enter elements of second tuple separated by space: ").split())
    print("Tuples have same elements (order ignored)?", set(t1) == set(t2))

# Python program to find the median of elements in a tuple.
def median_of_tuple():
    t = sorted(map(float, input("Enter numeric elements of tuple separated by space: ").split()))
    n = len(t)
    if n == 0:
        print("Tuple is empty.")
    elif n % 2 == 1:
        print("Median:", t[n // 2])
    else:
        median = (t[n//2 - 1] + t[n//2]) / 2
        print("Median:", median)

if __name__ == "__main__":
    programs = {
        "1": ("Maximum and minimum in tuple", max_min_tuple),
        "2": ("Concatenate two tuples", concatenate_tuples),
        "3": ("Index of an item in tuple", index_of_item),
        "4": ("Count occurrences of element in tuple", count_element_occurrences),
        "5": ("Product of elements in tuple", product_of_elements),
        "6": ("Length of longest increasing subsequence", length_of_longest_increasing_subseq),
        "7": ("Frequency of elements in tuple", frequency_of_elements),
        "8": ("First occurrence index of element", first_occurrence_index),
        "9": ("Check if two tuples have same elements", check_same_elements),
        "10": ("Median of elements in tuple", median_of_tuple),
    }

    print("\nSelect a program to run:")
    for key, (desc, _) in programs.items():
        print(f"{key}. {desc}")

    choice = input("\nEnter your choice (1-10): ").strip()
    if choice in programs:
        programs[choice][1]()  # Call the chosen function
    else:
        print("Invalid choice.")