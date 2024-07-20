
from random import randint

a = randint(1, 1000)
b = randint(1, 1000)
d = randint(1, 1000)

c = int(input('{} + {} - {} = '.format(a, b, d)))

if c == (a+b-d):
	print('To`g`ri')
else:
	print('Xato, {}'.format(a+b-d))