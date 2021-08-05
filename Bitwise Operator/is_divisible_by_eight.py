'''
    Program to check if given num is divisible by 8 
'''

def is_divisible_by_eight(num):
    return num & 7

if __name__ == '__main__':
    while True:
        num = int(input('Number Please: '))
        if is_divisible_by_eight(num) == 0:
            print('Number is divisble by 8')
        else:
            print('Number is not divisble by 8')
