def int_to_roman(num):
    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]  
    result = ""
    for symbol, value in roman_numerals:
        while num >= value:
            result += symbol  
            num -= value
    return result
number = int(input())
assert 1 <= number <= 3999
roman_numeral = int_to_roman(number)
print(roman_numeral)




