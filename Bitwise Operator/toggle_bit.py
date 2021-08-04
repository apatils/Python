'''
    Program to toggle a bit of given number
'''
import my_util as util

def toggle_bit(num, pos):
    return num ^ (1 << pos - 1)

if __name__ == '__main__':
    num = int(input('Enter number: '))
    print('BINARY REPRESENTATION: ', util.decimal_to_binary(num))
    pos = int(input('Enter position: '))
    result = toggle_bit(num, pos)
    print('RESULT: ', util.decimal_to_binary(result))