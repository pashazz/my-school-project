#!/usr/bin/python3
#нахождение НОД алгоритмом Евклида.
import math

def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a

def lcm(a,b, gcd):
    return abs(a*b)//gcd

def prime_divisors(a):
  """Возвращает все простые от 2 до N"""
  sieve = set(range(2, a))
  for i in range(2, int(math.sqrt(a))):
    if i in sieve:
      sieve -= set(range(2*i, a, i))
  return sieve

def primes(n):
    a = [0] * n # создание массива с n количеством элементов
    for i in range(n): # заполнение массива ...
        a[i] = i # значениями от 0 до n-1
      
    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
      
    m = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n: # перебор всех элементов до заданного числа
        if a[m] != 0: # если он не равен нулю, то
            j = m * 2 # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0 # заменить на 0
                j = j + m # перейти в позицию на m больше
        m += 1
      
    # вывод простых чисел на экран (может быть реализован как угодно)
    return list(filter(lambda p: p != 0, a))

def divisors(a):
    # '''список простых делителей a'''
    lst = []
    div = primes(a)
    while a not in div:
        for j in div:
            if a % j == 0:
                lst.append(j)
                break
        a = a // j
    lst.append(a)
    return lst


if __name__ == '__main__':
    x = int(input('X => '))
    y = int(input ('Y => '))
    d = gcd(x, y)
    print('НОД: ', d, 'НОК: ', lcm(x, y, d))
    print ('Простые делители {}: '.format(x), divisors(x))
    print ('Простые делители {}: '.format(y), divisors(y))
