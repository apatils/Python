'''
    Program to turn off rightmost set bit of a given number
'''
import my_util as util

def turn_off_rightmost_bit(num):
    return num & (num - 1)

if __name__ == '__main__':
    num = int(input('Enter Number'))
    print('BINARY REPRESENTATION: ', util.decimal_to_binary(num))
    result = turn_off_rightmost_bit(num)
    print('RESULT: ', util.decimal_to_binary(result))