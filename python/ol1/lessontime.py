#!/usr/bin/env python3
'''Calculate current time without datetime module'''
import argparse

def calculate(lesson_number, lesson_time, lesson_len=45, change_len=15):
    start_time = (8, 30)
    assert lesson_number in range(1,7)
    assert lesson_time in range(-45,46)
    real_number = lesson_number - 1
    minutes = start_time[0]*60 + start_time[1]
    minutes += (lesson_len+change_len)*lesson_number
    minutes += lesson_time
    if lesson_time < 0:
        minutes += lesson_len

    current_time = []
    current_time.append(minutes // 60)
    current_time.append(minutes % 60)
    return current_time

if __name__=='__main__':
    parser = argparse.ArgumentParser(epilog='Олимпиадная задача #1: Время от Пети')
    parser.add_argument('lesson',metavar='K', type=int, choices=range(1,7))
    parser.add_argument('time',metavar='T', type=int, choices=range(-45,46))
    args = parser.parse_args()
    print ('{}:{}'.format(*calculate(args.lesson, args.time)))


