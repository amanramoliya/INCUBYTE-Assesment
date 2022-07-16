import re
def string_Calculator(string_numbers):
    if string_numbers == '':
        return 0
    else:
        string_numbers = map(int, re.findall(r"-?\d+", string_numbers))
        string_numbers = list(string_numbers)
        print(string_numbers)
        negative_numbers = list(filter(lambda x: x < 0, string_numbers))
        if negative_numbers: raise Exception('negatives not allowed ' + str(negative_numbers))
        ans=0            
        for i, val in enumerate(string_numbers):
            if i%2==0 and val<1000:
                ans=ans+val
        return ans
