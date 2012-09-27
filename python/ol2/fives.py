#!/usr/bin/python3

import argparse
import itertools

def calculate (k):
    result = 0
    for i in itertools.count(): # беск. цикл
        if k == 0:
            break
        binary = (k % 2) * (10 ** i)
        result += binary  # перевод в двоичную систему
        k = k // 2
    return result*5
if __name__=='__main__':
    parser = argparse.ArgumentParser(epilog='Круглые числа с 0 и 5')
    parser.add_argument('k', metavar='K',type=int, choices=range(1,500))
    k = parser.parse_args().k - 1
    print(calculate(k))
