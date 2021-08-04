'''
    Program to turn of specific bit of a number
'''
import my_util as util

def turn_ofF_bit(num, pos):
    return num & ~(1 << pos-1)

if __name__ == '__main__':
    num = int(input('Enter Number: '))
    print('BINARY REPRESENTATION: ',util.decimal_to_binary(num))
    pos = int(input('Enter Position: '))
    result = turn_ofF_bit(num, pos)
    print('RESULT: ', util.decimal_to_binary(result))