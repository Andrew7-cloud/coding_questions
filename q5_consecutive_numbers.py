""" The purpose of this file is to asses a list of numbers to determine if values are in sequence"""

# Requirements:Write a function to check to see if all numbers in list are consecutive numbers.
#   For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#   The return should be boolean Type. def is_consecutive(a_list): "


def is_consecutive(a_list):
    # inital value represents initial "step off point"
    x = a_list[0]
    Consecutive_test = True

    for item in a_list:
        current_item = item

# if true, then inital value is being evaluated (1 in example), pass 1 to prior item and reiterate
        if current_item == x:
            prior_item = current_item
            pass

# scenario: inital value not being evaluated

        else:
            if current_item != prior_item + 1:
                a_list = False
                return a_list

            else:
                prior_item = current_item
                pass

    return a_list


# data input
selected_list = [1, 2, 3, 4, 5]

# function call
is_consecutive(selected_list)

# I beleieve the existing code logic is complete and correct.

# How do I properly check and print the return?
