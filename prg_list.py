# Python program to find the second largest number in a list.
def second_largest():
    lst = list(map(int, input('Enter list elements separated by space: ').split()))
    if len(lst) < 2:
        print("List must have at least 2 elements.")
        return
    unique_lst = list(set(lst))
    unique_lst.sort(reverse=True)
    print("Second largest element:", unique_lst[1])

# Python program to merge two sorted lists into a single sorted list.
def merge_sorted_lists():
    l1 = list(map(int, input("Enter first sorted list separated by space: ").split()))
    l2 = list(map(int, input("Enter second sorted list separated by space: ").split()))
    merged = sorted(l1 + l2)
    print("Merged sorted list:", merged)

# Python program to find the intersection of two lists.
def intersection_of_lists():
    l1 = list(map(int, input("Enter first list separated by space: ").split()))
    l2 = list(map(int, input("Enter second list separated by space: ").split()))
    intersection = list(set(l1) & set(l2))
    print("Intersection:", intersection)

# Python program to check if a list is sorted in ascending order.
def is_sorted():
    lst = list(map(int, input("Enter list of elements separated by space: ").split()))
    sorted_check = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    print("Is the list sorted in ascending order?", sorted_check)

# Python program to find the frequency of elements in a list.
def frequency_of_elements_list():
    lst = list(map(int, input("Enter elements separated by space: ").split()))
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    print("Frequency of elements:", freq)

# Python program to find the largest and smallest elements in a list.
def largest_and_smallest():
    lst = list(map(int, input("Enter list of the elements separated by space: ").split()))
    print("Largest element:", max(lst))
    print("Smallest element:", min(lst))

# Python program to remove the nth index element from a list.
def remove_nth_index():
    lst = list(map(int, input("Enter list elements separated by space: ").split()))
    n = int(input("Enter index to remove: "))
    if 0 <= n < len(lst):
        removed = lst.pop(n)
        print(f"Removed element {removed}. Updated list:", lst)
    else:
        print("Invalid index.")

# Python program to find the sum of elements in a list using recursion.
def sum_using_recursion():
    lst = list(map(int, input("Enter list elements separated by space: ").split()))
    def recursive_sum(arr):
        if not arr:
            return 0
        return arr[0] + recursive_sum(arr[1:])
    print("Sum of elements:", recursive_sum(lst))

# Python program to sort a list of strings based on the length of each string.
def sort_strings_by_length():
    lst = input("Enter strings separated by space: ").split()
    sorted_lst = sorted(lst, key=len)
    print("Strings sorted by length:", sorted_lst)

# Python program to reverse a list in groups of a given size.
def reverse_in_groups():
    lst = input("Enter list elements separated by space: ").split()
    k = int(input("Enter group size: "))
    result = []
    for i in range(0, len(lst), k):
        result.extend(lst[i:i+k][::-1])
    print("List reversed in groups:", result)

if __name__ == "__main__":
    programs = {
        "1": ("Second largest in list", second_largest),
        "2": ("Merge two sorted lists", merge_sorted_lists),
        "3": ("Intersection of two lists", intersection_of_lists),
        "4": ("Check if list is sorted", is_sorted),
        "5": ("Frequency of elements in list", frequency_of_elements_list),
        "6": ("Largest and smallest in list", largest_and_smallest),
        "7": ("Remove nth index element", remove_nth_index),
        "8": ("Sum of elements using recursion", sum_using_recursion),
        "9": ("Sort strings by length", sort_strings_by_length),
        "10": ("Reverse list in groups", reverse_in_groups),
    }

    print("\nSelect a program to run:")
    for key, (desc, _) in programs.items():
        print(f"{key}. {desc}")

    choice = input("\nEnter your choice (1-10): ").strip()
    if choice in programs:
        programs[choice][1]()  # Call the chosen function
    else:
        print("Invalid choice.")