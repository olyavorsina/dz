import math

def binary_to_decimal():
    binary = input("Введите двоичное число: ")
    try:
        parts = binary.split('.')
        if len(parts) > 2:
            raise ValueError
        integer_part = parts[0]
        if integer_part[0] == '-':
            sign = -1
            integer_part = integer_part[1:]
        else:
            sign = 1
        decimal = 0
        for i, bit in enumerate(reversed(integer_part)):
            if bit == '1':
                decimal += 2 
        decimal *= sign
        if len(parts) == 2:
            fractional_part = parts[1]
            fractional_decimal = 0
            for i, bit in enumerate(fractional_part):
                if bit == '1':
                    fractional_decimal += 2  -(i + 1)
            decimal += fractional_decimal
        print("Десятичное число:", decimal)
    except ValueError:
        print("Ошибка: введенное число не является двоичным.")

binary_to_decimal()



