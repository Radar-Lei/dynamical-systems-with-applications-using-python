from sympy import *
t, v, V, m = symbols('t v V m')
theta = symbols('theta', cls=Function)
eqn1 = Eq((exp(v*t/V)*theta(t)).diff(t), exp(v*t/V)*m/V)
sol = dsolve(eqn1, theta(t))
print(sol)
