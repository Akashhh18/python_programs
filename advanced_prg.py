#Python program to find the LCM (Least Common Multiple) of two numbers.
def find_lcm():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    g = gcd(a, b)
    lcm = (a * b) // g
    print(f"LCM of {a} and {b} is: {lcm}")

#Python program to find the GCD (Greatest Common Divisor) of two numbers.
def find_gcd():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    while b != 0:
        a, b = b, a % b
    print("GCD is:", a)

#Python program to generate Fibonacci series up to n terms.
def fibonacci_series():
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b
    print()

#Python program to sort a list of integers using the bubble sort algorithm.
def bubble_sort():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print("Sorted list:", nums)

#Python program to implement linear search in a list.
def linear_search():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter number to search: "))
    found = False
    for i in range(len(nums)):
        if nums[i] == target:
            print(f"{target} found at index {i}")
            found = True
            break
    if not found:
        print(f"{target} not found in list")


if __name__ == "__main__":
    programs = {
        "1": ("Find LCM of two numbers", find_lcm),
        "2": ("Find GCD of two numbers", find_gcd),
        "3": ("Generate Fibonacci series", fibonacci_series),
        "4": ("Sort numbers using Bubble Sort", bubble_sort),
        "5": ("Linear search in list", linear_search),
    }

    print("\nSelect a program to run:")
    for key, (desc, _) in programs.items():
        print(f"{key}. {desc}")

    choice = input("\nEnter your choice (1-5): ")
    if choice in programs:
        programs[choice][1]()  # Call the chosen function
    else:
        print("Invalid choice.")
