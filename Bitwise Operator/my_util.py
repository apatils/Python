'''
    My own util functions
'''

def decimal_to_binary(num):
    binary_result = ''
    while num >= 1:
        i = num % 2 
        binary_result = str(i) + binary_result
        num //= 2
    return binary_result