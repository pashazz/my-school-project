#!/usr/bin/env python3

'''Вычислить минимальное количество ходов фишки для включения всех лампочек в ряду'''
import logging, argparse
log = logging.Logger('diodes')
frm = logging.Formatter(style='{', fmt='{name}: {message}')
hldr = logging.StreamHandler()


def moveLeft(state, pos):
    '''поместить фишку в позицию pos - 1'''
    if pos <= 0:
        raise IndexError ('Incorrect call of moveLeft: position {}'.format(pos))
    pos -= 1
    state [pos] = not state [pos]
    logging.debug('Moving cursor: {old} -> {p}; setting value for {p}: {state} '.format(state = state[pos], old = pos+1, p=pos))
    return state, pos

def moveRight(state, pos):
    '''поместить фишку в позицию pos+1'''
    if pos == len(state)-1:
        raise IndexError ('Incorrect call of moveRight - there is no more diodes.')

    pos += 1
    state[pos] = not state[pos]
    logging.debug('Moving cursor: {old} -> {p}; setting value for {p}: {state} '.format(state = state[pos], old = pos-1, p=pos))
    return state, pos

def calculate (diodes_count):
    '''Вычислить минимальное количество ходов для фишки, которая действует для
    ряда с лампочками в роли ключа, переключая их состояние
    @rtype: int 
    '''
    if diodes_count < 2:
        raise ValueError ('There must be 3 diodes or more')
    pos, count = 0, 0
    state = [False] * diodes_count 

    while True:
        if pos > 0 and (not state[pos-1]):
            state, pos =  moveLeft(state, pos)
        else:
            state, pos =  moveRight(state, pos)
        count +=1

        if all(state):
            return count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(epilog='Олимпиадная задача #2: Фишка и лампы')
    parser.add_argument('-d', '--debug', help='Отладка', action='store_true')
    parser.add_argument('diodes', metavar='ЛАМПОЧКИ', help='Количество лампочек', type=int, nargs='?', choices=range(2,2001))
    args = parser.parse_args()
    if args.debug:
        log.setLevel(logging.DEBUG)
    else:
        x = args.diodes

    if  x not in range (2, 2001):
        print ('Invalid input (too small/big): exiting')
        exit()

    res = calculate(x)
    print (res)
