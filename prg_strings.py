import string as str_module

# Python program to check if a given string is a palindrome or not (ignoring spaces and case).
def palindrome_check():
    s = input("Enter a string: ").replace(" ", "").lower()
    print("Is palindrome?", s == s[::-1])

# Python program to reverse words in a given string.
def reverse_words():
    s = input("Enter a string: ")
    words = s.split()
    reversed_s = ' '.join(words[::-1])
    print("Reversed words:", reversed_s)

# Python program to check if two strings are anagrams of each other.
def check_anagram():
    s1 = input("Enter first string: ").replace(" ", "").lower()
    s2 = input("Enter second string: ").replace(" ", "").lower()
    print("Are anagrams?", sorted(s1) == sorted(s2))

# Python program to find the longest word in a given string.
def longest_word():
    s = input("Enter a string: ")
    words = s.split()
    longest = max(words, key=len)
    print("Longest word:", longest)

# Python program to count the number of vowels and consonants in a string.
def count_vowels_consonants():
    s = input("Enter a string: ").lower()
    vowels = "aeiou"
    v_count = sum(1 for c in s if c in vowels)
    c_count = sum(1 for c in s if c.isalpha() and c not in vowels)
    print("Vowels:", v_count, "Consonants:", c_count)

# Python program to check if a given string is a pangram or not.
def pangram_check():
    s = input("Enter a string: ").lower()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    print("Is pangram?", alphabet <= set(s))

# Python program to capitalize the first letter of each word in a sentence.
def capitalize_words():
    s = input("Enter a sentence: ")
    capitalized = ' '.join(word.capitalize() for word in s.split())
    print("Capitalized sentence:", capitalized)

# Python program to find the frequency of each word in a string.
def word_frequency():
    s = input("Enter a string: ").lower()
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    print("Word frequency:", freq)

# Python program to check if a given string is a valid palindrome or not.
def valid_palindrome():
    s = ''.join(c.lower() for c in input("Enter a string: ") if c.isalnum())
    print("Is valid palindrome?", s == s[::-1])

# Python program to remove all punctuations from a given string.
def remove_punctuations():
    s = input("Enter a string: ")
    cleaned = ''.join(c for c in s if c not in str_module.punctuation)
    print("String without punctuations:", cleaned)

if __name__ == "__main__":
    programs = {
        "1": ("Check palindrome (ignore spaces & case)", palindrome_check),
        "2": ("Reverse words in string", reverse_words),
        "3": ("Check if two strings are anagrams", check_anagram),
        "4": ("Find longest word in string", longest_word),
        "5": ("Count vowels and consonants", count_vowels_consonants),
        "6": ("Check if string is pangram", pangram_check),
        "7": ("Capitalize first letter of each word", capitalize_words),
        "8": ("Word frequency in string", word_frequency),
        "9": ("Check valid palindrome (ignore non-alphanumeric)", valid_palindrome),
        "10": ("Remove all punctuations from string", remove_punctuations),
    }

    print("\nSelect a program to run:")
    for key, (desc, _) in programs.items():
        print(f"{key}. {desc}")

    choice = input("\nEnter your choice (1-10): ").strip()
    if choice in programs:
        programs[choice][1]()  # Call the chosen function
    else:
        print("Invalid choice.")