#!/usr/bin/env python3
"""Exact SymPy certificate for the cubic Keller map C^10 -> C^10."""
import sympy as s

x,y,z,a,b,c,d,e,h,q = s.symbols("x y z a b c d e h q")
v = (x,y,z,a,b,c,d,e,h,q)

g = s.Matrix([
 -a*b+a*e*z-3*a*y**2-b*e**2+d*e+d*x*y+3*e**2*z-7*e*y**2+3*x*y*z+4*y**2+z,
 -3*a*c-3*a*x*z-9*a*y-3*c*e**2+3*e*h-6*e*x*z+3*h*x*y+12*x*y**2+3*x*z+y,
 c*q+c*x**2+q*x*z+3*q*y+2*x,
 a-e**2-2*e*x*y,
 b+x*y*z+3*y**2,
 c+x*z+3*y,
 a*z-b*e+b*x*y+d+3*e*z-3*x*y*z-7*y**2,
 e+x*y,
 -c*e+c*x*y+h-2*x*z,
 q+x**2,
])

# Exact symbolic determinant check via the block determinant identity.
J = g.jacobian(v)
A, B, C, D = J[:3,:3], J[:3,3:], J[3:,:3], J[3:,3:]
assert s.expand(D.det()) == 1
schur = (A - B*D.inv()*C).applyfunc(s.expand)
assert s.expand(s.det(schur)) == -2

# The map is cubic.
degrees = [s.Poly(f, *v).total_degree() for f in g]
assert max(degrees) == 3

# Three distinct rational points have one image.
R = s.Rational
points = [
 (0,0,-R(1,4),0,0,0,0,0,0,0),
 (1,-R(3,2),R(13,2),-R(9,4),3,-2,-R(153,8),R(3,2),7,-1),
 (-1,R(3,2),R(13,2),-R(9,4),3,2,-R(153,8),R(3,2),-7,-1),
]
images = [tuple(g.subs(dict(zip(v,p)))) for p in points]
assert len(set(points)) == 3 and images[0] == images[1] == images[2]

print("degrees:", degrees)
print("det(Jg): -2")
print("three distinct preimages:", points)
print("common image:", images[0])
