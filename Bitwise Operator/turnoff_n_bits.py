'''
    Program to turn off n number of bits
'''
import my_util as util

def turnoff_n_bits(num, pos, no_of_bits):
    return num & ~ ( (2 ** no_of_bits - 1) << (pos - no_of_bits) )

if __name__ == '__main__':
    num = int(input("Enter Number: "))
    print('BINARY REPRESENTATION: ', util.decimal_to_binary(num))
    pos = int(input('Enter Position: '))
    no_of_bits = int(input('Enter Number of bits to turn off: '))
    result = turnoff_n_bits(num, pos, no_of_bits)
    print('Result - {} | Binary - {}'.format(result, util.decimal_to_binary(result)))
