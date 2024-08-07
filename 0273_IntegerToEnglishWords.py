# Problem 273


class IntegerToEnglishWords:
    # Copied from my own Java solution
    def __init__(self):
        self.ones = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                     9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
                     16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        self.tens = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty",
                     9: "Ninety"}

    def numberToWords(self, num: int) -> str:
        if num < 20:
            return self.ones[num]

        tokens = []
        billions = num // 1000000000
        if billions > 0:
            tokens.append(self.get_string_for_3_places(billions))
            tokens.append("Billion")

        num = num % 1000000000
        millions = num // 1000000
        if millions > 0:
            tokens.append(self.get_string_for_3_places(millions))
            tokens.append("Million")

        num = num % 1000000
        thousands = num // 1000;
        if thousands > 0:
            tokens.append(self.get_string_for_3_places(thousands))
            tokens.append("Thousand")

        num = num % 1000
        if num > 0:
            tokens.append(self.get_string_for_3_places(num))
        return " ".join(tokens)

    def get_string_for_3_places(self, num: int):
        tokens = []
        num = num % 1000
        hundred = num // 100
        if hundred > 0:
            tokens.append(self.ones[hundred])
            tokens.append("Hundred")
        rem = num % 100
        if 0 < rem < 20:
            tokens.append(self.ones[rem])
        else:
            tens_ = rem // 10
            if tens_ > 1:
                tokens.append(self.tens[tens_])
            units = rem % 10
            if units > 0:
                tokens.append(self.ones[units])

        return " ".join(tokens)


if __name__ == '__main__':
    i = IntegerToEnglishWords()
    print(i.numberToWords(123))
    print(i.numberToWords(12345))
    print(i.numberToWords(1234567))
