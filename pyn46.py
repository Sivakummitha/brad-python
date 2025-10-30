# Write a Python class to convert an integer to a roman numeral
class RomanNumeralConverter:
    roman_map= [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    def __init__(self, number):
        if not (1 <= number <= 3999):
            pass 
        self._number = number
    def to_roman(self):
        roman_numeral = ""
        current_number = self._number
        for value, symbol in self.roman_map:
            while current_number >= value:
                roman_numeral += symbol
                current_number -= value
        return roman_numeral
converter1 = RomanNumeralConverter(2004)
print(f"2004 in Roman numerals: {converter1.to_roman()}")
converter2 = RomanNumeralConverter(6)
print(f"6 in Roman numerals: {converter2.to_roman()}")
converter3 = RomanNumeralConverter(19)
print(f"19 in Roman numerals: {converter3.to_roman()}")