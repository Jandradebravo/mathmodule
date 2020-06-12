#Function file
def fun_file(f):

	file = open('tmp.py','w')

	file.write('def fun(x): from math import')
	#Power and Logarithmic
	file.write(' exp as exp')
	file.write(',log10 as log10')
	file.write(',log as log')
	file.write(',sqrt as sqrt')
	#Trig
	file.write(',cos as cos')
	file.write(',sin as sin')
	file.write(',tan as tan')
	file.write(',acos as acos')
	file.write(',asin as asin')
	file.write(',atan as atan')
	#Hyperbolic
	file.write(',acosh as acosh')
	file.write(',asinh as asinh')
	file.write(',atanh as atanh')
	file.write(',cosh as cosh')
	file.write(',sinh as sinh')
	file.write(',tanh as tanh')
	#Special
	file.write(',gamma as gamma')
	#Constants
	file.write(',pi as pi')
	file.write(',e as e')

	file.write('; return ' + f)
	file.close()