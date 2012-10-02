#!/usr/bin/env python3
'''Вычисление счастливого билета'''
import argparse

def check_ticket(ticket):
	'''Checks if abcxyz ticket - abc= xyz'''
	if not isinstance(ticket, int):
		raise ValueError('Ticket is not int')

	if ticket not in range (100000, 999999):
		raise ValueError ('Ticket is not in range')

	c = 100000
	digits = []
	

	while True:
		digits.append(int(ticket//c))
		if (c==1):
			break
		ticket = ticket % c
		c /= 10

	if sum (digits[:3]) == sum (digits[3:]):
		print ('Билет является счастливым')
	else:
		print ('Билет не является счастливым')



if __name__ == '__main__':
	parser = argparse.ArgumentParser(epilog='Счастливый билет')
	parser.add_argument('number', type=int, metavar='N', help='Номер билета', choices=range(100000,1000000))

	args = parser.parse_args()
	check_ticket(args.number)

