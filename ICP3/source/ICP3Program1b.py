# Function to count vowel
def vowel_count(input_string):
    count = 0

    # Creating a set of vowels
    vowel = set("aeiouAEIOU")

    for alphabet in input_string:
        if alphabet in vowel:
            count = count + 1

    print("No. of vowels :", count)


# Input string
string1 = input("enter a string:")
# Calling a function
vowel_count(string1)