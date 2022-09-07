
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""def add_two_numbers(input_one, input_two):
    number_one = int(input_one)
    number_two = int(input_two)
    return number_one + number_two

def main():
    print('This program adds the numbers')
    print(add_two_numbers(4,5))

main()"""

"""" Start in-class excercise here """
"""Part 1"""
def main():
    number_one=  int(input("Enter a number. "))
    number_two= int(input("Enter another number. "))
    sum = number_one + number_two
    difference =  number_one - number_two
    product =  number_one * number_two
    quotient =  number_one / number_two
    print("Sum: ", sum, "difference: ", difference, "product: ", product, "quotient: ", quotient)

main()

"""Part 2"""

def add(your_number_one, your_number_two):
    addition_result = your_number_one + your_number_two
    return addition_result

def subtract(your_number_one, your_number_two):
    subtraction_result = your_number_one - your_number_two
    return subtraction_result

def multiply(your_number_one, your_number_two):
    multiplication_result = your_number_one * your_number_two
    return multiplication_result

def divide(your_number_one, your_number_two):
    division_result = your_number_one / your_number_two
    return division_result

"""FIND OUT WHAT IS GOING WRONG HERE """

five_character_word = str(input("Enter a five-character word: "))
single_character = str(input("Enter a single character: "))
print("Searching for", single_character, "in", five_character_word)
