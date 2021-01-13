"""  The purpose of this file is to determine the maximimum value in a list """

# Requirements: "Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):"


def max_num_in_list(a_list):
    maximum_var = max(a_list)
    print(maximum_var)
    return maximum_var


l_provided = [1, 200, 500, 300, 700, 20]

# call function
max_num_in_list(l_provided)
