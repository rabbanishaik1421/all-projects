def number_to_words(num):
    if num == 0:
        return "Zero"

    if num < 0:
        return "Minus " + number_to_words(-num)

    ones = [
        "", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen",
        "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]

    tens = [
        "", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]

    def convert(n):
        if n < 20:
            return ones[n]

        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")

        elif n < 1000:
            return ones[n // 100] + " Hundred" + (
                " " + convert(n % 100) if n % 100 != 0 else ""
            )

        elif n < 1000000:
            return convert(n // 1000) + " Thousand" + (
                " " + convert(n % 1000) if n % 1000 != 0 else ""
            )

        elif n < 1000000000:
            return convert(n // 1000000) + " Million" + (
                " " + convert(n % 1000000) if n % 1000000 != 0 else ""
            )

        else:
            return convert(n // 1000000000) + " Billion" + (
                " " + convert(n % 1000000000) if n % 1000000000 != 0 else ""
            )

    return convert(num)


# Input
num = 123

# Output
print(number_to_words(num))