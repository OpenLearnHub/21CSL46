def roman2Dec(romStr):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Analyze string backwards
    romanBack = list(romStr)[::-1]
    value = 0

    # To keep track of order
    right_val = roman_dict[romanBack[0]]

    for numeral in romanBack:
        leftVal = roman_dict[numeral]

        # Check for subtraction
        if leftVal < right_val:
            value -= leftVal
        else:
            value += leftVal

        right_val = leftVal

    return value


romanStr = input("Enter a Roman Number: ")
print(roman2Dec(romanStr))
