def intToRoman(num):
    numeral = ""

    def convertToNumerals(digit, value, numeral):
        if value == 1:
            base, five, ten = "I", "V", "X"
        elif value == 10:
            base, five, ten = "X", "L", "C"
        elif value == 100:
            base, five, ten = "C", "D", "M"
        elif value == 1000:
            base, five, ten = "M", None, None  # No need for 'five' and 'ten' at 1000s place

        if digit == 1:
            numeral = base + numeral
        elif digit == 2:
            numeral = base + base + numeral
        elif digit == 3:
            numeral = base + base + base + numeral
        elif digit == 4:
            numeral = base + five + numeral
        elif digit == 5:
            numeral = five + numeral
        elif digit == 6:
            numeral = five + base + numeral
        elif digit == 7:
            numeral = five + base + base + numeral
        elif digit == 8:
            numeral = five + base + base + base + numeral
        elif digit == 9:
            numeral = base + ten + numeral
        return numeral

    num = str(num)
    value = 1
    for i in range(len(num) - 1, -1, -1):
        digit = int(num[i])
        numeral = convertToNumerals(digit, value, numeral)
        value *= 10

    return numeral

print(intToRoman(3749))
