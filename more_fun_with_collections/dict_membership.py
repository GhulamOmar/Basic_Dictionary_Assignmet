""""
Program: dict_membership.py
Author: Ghulam Omar
Last date modified: 10/12/2019
This program is an example of function.That accepts a  Dictionary and return a boolean value.
"""


def in_dict(value, **key):
    """" accepts a  Dictionary and return a boolean"""
    for key in value:
        return 54 in (key, value['C'])  # return the true or false.


if __name__ == '__main__':
    print(in_dict({'A': 1, 'B': 11, 'C': 54}))
    """" calling the function"""
