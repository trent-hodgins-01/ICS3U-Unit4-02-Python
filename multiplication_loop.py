# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/29/2021
# This is the Multiplication Loop program
# The user enters in a positive integer
# The program tells the user the product the numbers from 1 to the number typed in

import math


def main():
    # this function uses a while loop and calculates the product
    loop_counter = 0
    answer = 1

    # input
    number_as_string = input("Enter in a positive integer: ")
    print("")

    # process and output
    try:
        number_as_integer = int(number_as_string)
        while loop_counter < number_as_integer:
            loop_counter = loop_counter + 1
            answer = answer * loop_counter
        print(
            "The product of all the positive numbers from 1 to {0} is {1}".format(
                number_as_string, answer
            )
        )

    except Exception:
        print("You didn’t enter in a positive integer.")

    print("\nDone")


if __name__ == "__main__":
    main()
