# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 15, 2022
# Description: Takes string and counts how many of each letter are in the string

def count_letters(string):
    result = {}

    for x in string.upper():
        if (x>="A" and x<='Z'):

            if not result.get(x):

                result[x]=1
            else:
                result[x] += 1

    return result

"""function takes string and returns number of each letter in string"""