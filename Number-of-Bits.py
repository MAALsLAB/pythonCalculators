# This Program Calculates Number of Bits needed
# Needed for a decimal Number
# N = log2(decimal number)
# Where N = Number of bits
import math

D_number = input('Decimal number value = ')

if D_number.isnumeric():
    D_number = int(D_number)  # Convert to int
elif '.' in D_number:
    D_number = float(D_number)
else:
    print("Pleas Enter a Decimal Number")
    exit()

number_of_bits = round(math.log2(D_number))

print(f'Number of Bits = {number_of_bits}')
