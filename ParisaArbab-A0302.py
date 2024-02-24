"""
Author: Parisa Arbab
Date: Jan 27 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”
YouTube Link:https://youtu.be/XDN-kimPlfk

Questions:
 How does your code know when to stop when operating on a sad number?
 Show how using the top-down method resulted in clean readable code.
"""


def is_prime(num):
    """
    Check if a given number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def is_happy(num):
    """
    Check if a number is a happy number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is happy, False otherwise.
    """
    visited = set()
    while num != 1 and num not in visited:
        visited.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1


def classify_number(num):
    """
    Classify a number as happy prime, sad prime, happy non-prime, or sad non-prime.

    Args:
        num (int): The number to classify.

    Returns:
        str: Classification result as a string.
    """
    if is_prime(num):
        if is_happy(num):
            return "Happy Prime"
        else:
            return "Sad Prime"
    else:
        if is_happy(num):
            return "Happy Non-Prime"
        else:
            return "Sad Non-Prime"


while True:
    try:
        user_input = int(input("Enter a positive integer (or '0' to exit): "))
        if user_input == 0:
            break
        result = classify_number(user_input)
        print(f"{user_input} is a {result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
