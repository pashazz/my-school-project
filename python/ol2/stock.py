#!/usr/bin/python3
#Calculate how many boxes the stock can contain
import argparse
import itertools
def calculate (stock, box):
    '''вычислить, сколько коробок поместится на складе
    @param stock: размер склада
    @param box: размер коробки
    '''
    x, y, z = (m//n for (m,n) in zip(stock,box))
    return x*y*z

def maximum (stock, box):
    '''вычислить макс. значение с помощью calculate'''
    results = tuple(itertools.starmap(calculate, ((s,b) for s in itertools.permutations(stock) for b in itertools.permutations(box))))
    return max(results)



if __name__=='__main__':
    parser = argparse.ArgumentParser(epilog='Вычислить, сколько коробок поместится на складе')
    parser.add_argument('s_length', metavar='ДС', type=int, choices=range(1,1001))
    parser.add_argument('s_height',  metavar='ВС',type=int, choices=range(1,1001))
    parser.add_argument('s_width', metavar='ШС', type=int, choices=range(1, 1001))
    parser.add_argument('b_length', metavar='ДК', type=int, choices=range(1,1001))
    parser.add_argument('b_height', metavar='ВК', type=int, choices=range(1, 1001))
    parser.add_argument('b_width', metavar='ШК', type=int, choices=range(1,1001))
    args = parser.parse_args()
    stock = tuple((args.s_length, args.s_height, args.s_width))
    box = tuple((args.b_length, args.b_height, args.b_width))
    print (maximum(stock, box))

