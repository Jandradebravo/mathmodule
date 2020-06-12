from math import pi as pi, e as e
from source import fun_file as fun_file
from os import remove as rem

#Definite Integral
def intg(f, a, b, n = 10000):
	
	fun_file(f)
	from tmp import fun as funint

	dx = (b-a)/n

	xi = a
	s = 0

	for i in range(0,n):
		xii = xi + dx
		ai = (dx/2)*(funint(xi) + funint(xii))
		s += ai
		xi = xii

	rem('tmp.py')
	return s