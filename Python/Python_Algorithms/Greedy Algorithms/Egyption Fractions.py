import math

def egypt_fract(numerator, denominator):
    egypt_list = []
    while numerator != 0:
        x = math.ceil(denominator / numerator)
        egypt_list.append(x)

        numerator = x * numerator - denominator
        denominator *= x

    string = ""
    
    for ones in egypt_list:
        string += f"1/{ones} + "

    final_string = string[:-3]
    return final_string

print(egypt_fract(7, 12))

