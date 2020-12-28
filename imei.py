import sys
import random

# Src: https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/luhn.py
# Src: https://github.com/bstein/py-imei-generator

# config
imei = ''
# end config

def checksum(number, alphabet='0123456789'):
    n = len(alphabet)
    number = tuple(alphabet.index(i)
                   for i in reversed(str(number)))
    return (sum(number[::2]) +
            sum(sum(divmod(i * 2, n))
                for i in number[1::2])) % n

def calc_check_digit(number, alphabet='0123456789'):
    check_digit = checksum(number + alphabet[0])
    return alphabet[-check_digit]

def main(imei):
    while len(imei) < 14:
        imei += str(random.randint(0, 9))

    imei += calc_check_digit(imei)
    print(imei)

if __name__ == '__main__':
    main(imei)