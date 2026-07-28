#!/usr/bin/env python3
"""Exact SymPy certificates for the 4D degree-6 and 5D degree-5 maps."""

import sympy as s

x, y, z, t, a, b = s.symbols("x y z t a b")
u = 1 + x * y

f1 = s.expand(u**3 * z + y**2 * u * (4 + 3 * x * y))
f2 = s.expand(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
f3 = s.expand(2 * x - 3 * x**2 * y - x**3 * z)

# One-register stabilization: C^4, total degree 6.
g4 = s.Matrix(
    [
        s.expand(f1 + (t + y**3) * f3),
        f2,
        f3,
        t + y**3,
    ]
)
v4 = (x, y, z, t)

# Two-register stabilization: C^5, total degree 5.
g5 = s.Matrix(
    [
        s.expand(f1 + (a + y**3) * f3),
        s.expand(f2 + 3 * (b + y**2) * f3),
        f3,
        a + y**3,
        b + y**2,
    ]
)
v5 = (x, y, z, a, b)

R = s.Rational

points4 = [
    (0, 0, -R(1, 4), 0),
    (1, -R(3, 2), R(13, 2), R(27, 8)),
    (-1, R(3, 2), R(13, 2), -R(27, 8)),
]

points5 = [
    (0, 0, -R(1, 4), 0, 0),
    (1, -R(3, 2), R(13, 2), R(27, 8), -R(9, 4)),
    (-1, R(3, 2), R(13, 2), -R(27, 8), -R(9, 4)),
]


def certify(name: str, mapping: s.Matrix, variables: tuple, points: list, expected_degrees: list) -> None:
    degrees = [s.Poly(component, *variables).total_degree() for component in mapping]
    determinant = s.factor(mapping.jacobian(variables).det())
    images = [tuple(mapping.subs(dict(zip(variables, point)))) for point in points]

    assert degrees == expected_degrees
    assert determinant == -2
    assert len(set(points)) == 3
    assert images[0] == images[1] == images[2]

    print(name)
    print("  degrees:", degrees)
    print("  det(J):", determinant)
    print("  common image:", images[0])


certify("C^4 degree-6 map", g4, v4, points4, [5, 6, 4, 3])
certify("C^5 degree-5 map", g5, v5, points5, [5, 5, 4, 3, 2])
print("CERTIFIED: exact noninjective Keller maps in bidegrees (4,6) and (5,5).")
