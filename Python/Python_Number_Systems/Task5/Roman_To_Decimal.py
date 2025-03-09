def roman_to_decimal(num, ns):
    if ns == "decimal":
        roman_dict = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}
        roman_reversed = list(reversed(list(num)))
        value = 0
        right_val = roman_dict[roman_reversed[0]]
        for i in roman_reversed:
            left_val = roman_dict[i]
            if left_val < right_val:
                value -= left_val
            else:
                value += left_val
            right_val = left_val
        return value

    elif ns == "roman":
        num = int(num)
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
             "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L",
             "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
             "VI", "VII", "VIII", "IX"]

        thousands = m[num // 1000]
        hundreds = c[(num % 1000) // 100]
        tens = x[(num % 100) // 10]
        ones = i[num % 10]

        ans = (thousands + hundreds +
               tens + ones)

        return ans


print(roman_to_decimal('10', "roman"))
