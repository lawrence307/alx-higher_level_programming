#!/usr/bin/python3
# Check Examples

# python 3.7.1

thousands = ["MMM", "MM", "M"]
hundreds = ["CM", "DCCC", "DCC", "DC", "D",
            "CD", "CCC", "CC", "C"]
tens = ["XC", "LXXX", "LXX", "LX", "L",
        "XL", "XXX", "XX", "X"]
digits = ["IX", "VIII", "VII", "VI", "V",
          "IV", "III", "II", "I"]


def check_digit(string, nums):
    for i in nums:
        if i in string:
            return list(reversed(nums)).index(i) + 1
    return -1
