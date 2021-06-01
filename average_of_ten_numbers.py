#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: June 2021
# This program finds the average of ten random numbers

import random


def main():
    # this function finds the average

    # list declaration
    numbers = []

    # process -- generate numbers
    for loop_counter in range(0, 9 + 1):
        single_number = random.randint(1, 100)
        numbers.append(single_number)
    print("The numbers are {0}".format(numbers))  # output

    # process -- find average
    total = 0
    for loop_counter in range(len(numbers)):
        total += numbers[loop_counter]
    average = total / len(numbers)
    print("\nThe average is {0}\nDone.".format(average))  # output


if __name__ == "__main__":
    main()
