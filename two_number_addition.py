#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program calculates the sum of two numbers


def main():
    # this function calculates the sum of two numbers

    # Input
    number_1 = int(input("Enter the first number to add (integer): "))
    number_2 = int(input("Enter the second number to add (integer): "))

    # Process
    the_sum = number_1 + number_2

    # Output
    print("")
    print("{0} + {1} = {2}".format(number_1, number_2, the_sum))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
