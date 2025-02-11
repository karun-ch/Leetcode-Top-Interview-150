num = 58
num = 3749
value_to_roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
result = ""

for value, roman in value_to_roman:
    # print(value,roman,num)
    while num >= value:
        result += roman  # Append the Roman numeral
        num -= value     # Reduce the number by the value

print(result)