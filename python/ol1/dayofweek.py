#!/usr/bin/env python3
import argparse

def weeknumber(yearfirstday, curday, weeklen=7):
    '''
    @param yearfirstday: first day of week in year
    @param curday: current day of year'''
    assert (yearfirstday in range (1, weeklen+1))
    assert (curday in range (1, 366))

    firstweekcount = weeklen + 1 - yearfirstday
    if curday <= firstweekcount:
        return curday
    else:
        curday = curday - firstweekcount
        return curday % weeklen

if __name__ == '__main__':
    parser = argparse.ArgumentParser(epilog='Олимпиадная задача #3: День недели в году')
    parser.add_argument('curday', help='Текущий день года', metavar='N', type=int, choices=range(1,366))
    parser.add_argument('yearfirstday', help='Первый день недели в году', metavar='НОМЕР', type=int, choices=range(1, 8))

    args = parser.parse_args()
    print (weeknumber(args.yearfirstday, args.curday))
