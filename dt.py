from math import pi as pi, e as e
from source import fun_file as fun_file
from os import remove as rem

#Derivative calculator
def dt(f, xo, order = 1, h = 0.0001):

	fun_file(f)
	from tmp import fun as fundt

	if order == 1:
		fprime = (fundt(xo + h) - fundt(xo - h))/(2*h)
		rem('tmp.py')
		return fprime
	elif order == 2:
		fprime = (fundt(xo+h) - 2*fundt(xo) + fundt(xo-h))/(h**2)
		rem('tmp.py')
		return fprime
	else:
		rem('tmp.py')
		return 'Please enter a first or second derivative'