# mathmodule
Python module featuring some math functions scripted by me.

<h2>Functions Included</h2>

It's a small module right now, but I intend to expand it. Currently it support definite integration and first and second order derivative.

<h3>intg(f,a,b,[n]):</h3>
Returns the definite integral from a to b of f(inside "" or ''), using the trapezoidal rule with n steps, default n is 10000.

<h3>dt(f,xo,[order,h]):</h3>
Returns the first(default or order = 1) or second(order = 2) derivative of f(inside "" or '') at x = xo, using the central difference rule with an small step h, default h is 0.0001.

<h2>How to use</h2>

Just import it like any other module.
<p>Examples:</p>
<p>importmathmodule</p>
<p>from mathmodule import intg</p>
