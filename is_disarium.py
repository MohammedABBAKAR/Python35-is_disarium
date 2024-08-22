# Disarium Number
# A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

# Create a function that determines whether a number is a Disarium or not.

# Examples
# is_disarium(75) ➞ False
# # 7^1 + 5^2 = 7 + 25 = 32

# is_disarium(135) ➞ True
# # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

# is_disarium(544) ➞ False

# is_disarium(518) ➞ True

# is_disarium(466) ➞ False

# is_disarium(8) ➞ True
# Notes
# Position of the digit is 1-indexed.
# A recursive version of this challenge can be found via this link.



def is_disarium(number):
    digits = str(number)
    sum_of_powers = sum(int(digit) ** (index + 1) for index, digit in enumerate(digits))
    return sum_of_powers == number

# Test cases
print(is_disarium(75))  # Output: False
print(is_disarium(135))  # Output: True
print(is_disarium(544))  # Output: False
print(is_disarium(518))  # Output: True
print(is_disarium(466))  # Output: False
print(is_disarium(8))    # Output: True
