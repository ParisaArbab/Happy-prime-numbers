# Happy-prime-numbers
classifies numbers into one of four categories: Happy Prime, Sad Prime, Happy Non-Prime, or Sad Non-Prime, based on their primality and happiness status.
This Python program classifies numbers into one of four categories: Happy Prime, Sad Prime, Happy Non-Prime, or Sad Non-Prime, based on their primality and happiness status.

Primality Check: The is_prime function determines if a number is prime. Numbers less than 2 are not prime. The function efficiently checks divisibility for numbers greater than 3, ruling out non-prime numbers early.

Happiness Check: The is_happy function checks if a number is a happy number. A number is happy if the sum of the squares of its digits repeatedly leads to 1. The function uses a set to track visited numbers to detect loops.

Classification: The classify_number function uses is_prime and is_happy to classify a number into one of four categories: Happy Prime (a prime number that is also happy), Sad Prime (a prime number that is not happy), Happy Non-Prime (a non-prime number that is happy), or Sad Non-Prime (a non-prime number that is not happy).

User Interaction: The program prompts the user to enter a positive integer and uses the classify_number function to classify it, printing the result. The loop continues until the user enters '0' to exit. It handles invalid inputs gracefully, prompting the user to enter a positive integer in case of a ValueError.

This code combines mathematical concepts of primality and happiness of numbers with interactive input to provide an educational tool that explores number theory properties.
