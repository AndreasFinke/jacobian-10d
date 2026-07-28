#!/usr/bin/env python3
"""Exact SymPy certificates for all maps documented in this repository."""

from __future__ import annotations

import sympy as s


def degree_vector(mapping: s.Matrix, variables: tuple[s.Symbol, ...]) -> list[int]:
    return [s.Poly(component, *variables).total_degree() for component in mapping]


def images(
    mapping: s.Matrix,
    variables: tuple[s.Symbol, ...],
    points: list[tuple[s.Expr, ...]],
) -> list[tuple[s.Expr, ...]]:
    return [
        tuple(s.cancel(component.subs(dict(zip(variables, point)))) for component in mapping)
        for point in points
    ]


def certify_collision(
    mapping: s.Matrix,
    variables: tuple[s.Symbol, ...],
    points: list[tuple[s.Expr, ...]],
) -> tuple[s.Expr, ...]:
    evaluated = images(mapping, variables, points)
    assert len(set(points)) == len(points)
    assert all(image == evaluated[0] for image in evaluated[1:])
    return evaluated[0]


R = s.Rational
x, y, z, t, a, b, c, d, e, h, q = s.symbols("x y z t a b c d e h q")

# Original three-dimensional degree-seven map.
u = 1 + x * y
f1 = s.expand(u**3 * z + y**2 * u * (4 + 3 * x * y))
f2 = s.expand(y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
f3 = s.expand(2 * x - 3 * x**2 * y - x**3 * z)
f = s.Matrix([f1, f2, f3])
v3 = (x, y, z)
points3 = [
    (0, 0, -R(1, 4)),
    (1, -R(3, 2), R(13, 2)),
    (-1, R(3, 2), R(13, 2)),
]

assert degree_vector(f, v3) == [7, 6, 4]
assert s.factor(f.jacobian(v3).det()) == -2
image3 = certify_collision(f, v3, points3)

# One-register stable reduction: dimension 4, degree 6.
g4 = s.Matrix(
    [
        s.expand(f1 + (t + y**3) * f3),
        f2,
        f3,
        t + y**3,
    ]
)
v4 = (x, y, z, t)
points4 = [
    (0, 0, -R(1, 4), 0),
    (1, -R(3, 2), R(13, 2), R(27, 8)),
    (-1, R(3, 2), R(13, 2), -R(27, 8)),
]

assert degree_vector(g4, v4) == [5, 6, 4, 3]
assert s.factor(g4.jacobian(v4).det()) == -2
image4 = certify_collision(g4, v4, points4)

# Two-register stable reduction: dimension 5, degree 5.
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
points5 = [
    (0, 0, -R(1, 4), 0, 0),
    (1, -R(3, 2), R(13, 2), R(27, 8), -R(9, 4)),
    (-1, R(3, 2), R(13, 2), -R(27, 8), -R(9, 4)),
]

assert degree_vector(g5, v5) == [5, 5, 4, 3, 2]
assert s.factor(g5.jacobian(v5).det()) == -2
image5 = certify_collision(g5, v5, points5)

# Seven-register stable reduction: dimension 10, degree 3.
v10 = (x, y, z, a, b, c, d, e, h, q)
g10 = s.Matrix(
    [
        -a * b
        + a * e * z
        - 3 * a * y**2
        - b * e**2
        + d * e
        + d * x * y
        + 3 * e**2 * z
        - 7 * e * y**2
        + 3 * x * y * z
        + 4 * y**2
        + z,
        -3 * a * c
        - 3 * a * x * z
        - 9 * a * y
        - 3 * c * e**2
        + 3 * e * h
        - 6 * e * x * z
        + 3 * h * x * y
        + 12 * x * y**2
        + 3 * x * z
        + y,
        c * q + c * x**2 + q * x * z + 3 * q * y + 2 * x,
        a - e**2 - 2 * e * x * y,
        b + x * y * z + 3 * y**2,
        c + x * z + 3 * y,
        a * z - b * e + b * x * y + d + 3 * e * z - 3 * x * y * z - 7 * y**2,
        e + x * y,
        -c * e + c * x * y + h - 2 * x * z,
        q + x**2,
    ]
)

# Verify the displayed expanded map against the compact source/target factorization.
carrier_a = a + x**2 * y**2
carrier_b = b + x * y * z + 3 * y**2
carrier_c = c + x * z + 3 * y
carrier_d = d + x * y * (b - 3 * z) + a * z - e * (b - 3 * z) - 7 * y**2
carrier_e = e + x * y
carrier_h = h + x * y * c - c * e - 2 * x * z
carrier_q = q + x**2

g10_from_factorization = s.Matrix(
    [
        f1 - carrier_a * carrier_b + carrier_d * carrier_e,
        f2 - 3 * carrier_a * carrier_c + 3 * carrier_h * carrier_e,
        f3 + carrier_c * carrier_q,
        carrier_a - carrier_e**2,
        carrier_b,
        carrier_c,
        carrier_d,
        carrier_e,
        carrier_h,
        carrier_q,
    ]
).applyfunc(s.expand)

assert g10_from_factorization == g10
assert degree_vector(g10, v10) == [3, 3, 3, 3, 3, 2, 3, 2, 3, 2]

# Exact block determinant calculation for the full symbolic 10 x 10 Jacobian.
jacobian10 = g10.jacobian(v10)
j_xx = jacobian10[:3, :3]
j_xw = jacobian10[:3, 3:]
j_wx = jacobian10[3:, :3]
j_ww = jacobian10[3:, 3:]

assert s.expand(j_ww.det()) == 1
schur = (j_xx - j_xw * j_ww.inv() * j_wx).applyfunc(s.expand)
assert s.expand(s.det(schur)) == -2

points10 = [
    (0, 0, -R(1, 4), 0, 0, 0, 0, 0, 0, 0),
    (1, -R(3, 2), R(13, 2), -R(9, 4), 3, -2, -R(153, 8), R(3, 2), 7, -1),
    (-1, R(3, 2), R(13, 2), -R(9, 4), 3, 2, -R(153, 8), R(3, 2), -7, -1),
]
image10 = certify_collision(g10, v10, points10)

print("Exact certificates passed")
print(f"  C^3  degree 7: degrees {degree_vector(f, v3)}, common image {image3}")
print(f"  C^4  degree 6: degrees {degree_vector(g4, v4)}, common image {image4}")
print(f"  C^5  degree 5: degrees {degree_vector(g5, v5)}, common image {image5}")
print(f"  C^10 degree 3: degrees {degree_vector(g10, v10)}, common image {image10}")
print("  Jacobian determinant of every map: -2")
