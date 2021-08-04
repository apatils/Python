'''
    Program to count set bits of given number
'''

import my_util as util

def count_bits(num):
    count = 0
    while num:
        if num & 1:
            count += 1
        num >>= 1
    return count

if __name__ == '__main__':
   num = int(input("Enter number: "))
   print('BINARY REPRESENTATION: ', util.decimal_to_binary(num))
   result = count_bits(num)
   print(result) 