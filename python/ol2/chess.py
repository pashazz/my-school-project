#!/usr/bin/python3
import argparse

def is_black(x,y):
    return (x+y)%2 == 0


def loop (x1, y1, x2, y2):
    '''Проходит по прямоугольнику, возвращая множество черных клеток'''
    return {(x,y) for x in range (x1, x2+1)  for y in range (y1, y2+1) if is_black(x, y)}

def calculate (x1, x2, y1, y2, x3, y3, x4, y4):
    return len (loop(x1, y1, x2, y2) ^ loop(x3, y3, x4, y4))

if __name__ == '__main__':
    r = range(1, 65)
    parser = argparse.ArgumentParser(epilog = 'Выяснить количество черных клеток на участке доски')
    parser.add_argument('x1', help='(и y1) -  координаты левого верхнего угла первого прямоугольника', type=int, choices=r, metavar='X1')
    parser.add_argument('y1', type=int, choices=r,metavar='Y1')
    parser.add_argument('x2', help='(и y2) - координаты правого нижнего угла первого прямоугольника', type=int, choices=r, metavar='X2')
    parser.add_argument('y2', type=int, choices=r, metavar='Y2')
    parser.add_argument('x3', help='(и y3) - координаты левого верхнего угла второго прямоугольника', type=int, choices=r, metavar='X3')
    parser.add_argument('y3', type=int, choices=r, metavar='Y3')
    parser.add_argument('x4', help='(и y4) - координаты правого нижнего угла второго прямоугольника', type=int, choices=r, metavar ='X4')
    parser.add_argument('y4', type=int, choices=r, metavar='Y4')

    args = {name:value-1 for (name,value) in vars(parser.parse_args()).items()}
    print (calculate(**args))