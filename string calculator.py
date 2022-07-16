import re
def string_Calculator(string_numbers):
    if string_numbers == '':
        return 0
    else:
        string_numbers = map(int, re.findall(r"-?\d+", string_numbers))
        string_numbers = list(filter(lambda x: x < 1000, string_numbers))
        negative_numbers = list(filter(lambda x: x < 0, string_numbers))
        if negative_numbers: raise Exception('negatives not allowed ' + str(negative_numbers))
        return sum(string_numbers)