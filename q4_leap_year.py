
# Requirements: Write a function to return if the given year is a leap year.
#  A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
#  The return should be boolean Type (true/false). def is_leap_year(a_year):"


def is_leap_year(a_year):

    if a_year % 4 == 0:
        x = True
    else:
        x = False

    if a_year % 100 != 0:
        x2 = True
    else:
        x2 = False

    if a_year % 400 == 0:
        x3 = True
    else:
        x3 = False
    
    if x == True and x2 == False and x3 == True:
        y= True
    else:
        y=False

    print(y)
    return y 


selected_year = 2020
is_leap_year(selected_year)
