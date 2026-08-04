#!/usr/bin/env python3
"""Exact certificate for the 18D cubic-homogeneous map.

The seed is reconstructed from the public 10D formulas rather than from the
proposed R2/gamma decomposition. Determinants are certified by explicit
unimodular block eliminations of the displayed Jacobian matrices.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def expanded(items):
    return sp.Matrix([sp.expand(item) for item in items])


def homogeneous_part(poly, variables, degree):
    out = 0
    for powers, coefficient in sp.Poly(sp.expand(poly), *variables).terms():
        if sum(powers) == degree:
            out += coefficient * sp.prod(v**p for v, p in zip(variables, powers))
    return sp.expand(out)


def coordinate_matrix(polynomials, variables, degree):
    monomials = sorted(
        {
            powers
            for poly in polynomials
            for powers, _ in sp.Poly(poly, *variables).terms()
            if sum(powers) == degree
        }
    )
    rows = []
    for poly in polynomials:
        coefficients = dict(sp.Poly(poly, *variables).terms())
        rows.append([coefficients.get(monomial, 0) for monomial in monomials])
    return sp.Matrix(rows), monomials


def at(vector, variables, point):
    substitution = dict(zip(variables, point))
    return tuple(
        sp.expand(item.subs(substitution, simultaneous=True)) for item in vector
    )


def assert_zero_matrix(matrix):
    assert all(sp.expand(item) == 0 for item in matrix), matrix


def build_data():
    # Public variables and the general-cubic map from CONSTRUCTIONS.md.
    xo, yo, zo, ao, bo, co, do, eo, ho, qo = sp.symbols(
        "x_old y_old z_old a_old b_old c_old d_old e_old h_old q_old"
    )
    old = (xo, yo, zo, ao, bo, co, do, eo, ho, qo)
    public = expanded(
        (
            -ao * bo
            + ao * eo * zo
            - 3 * ao * yo**2
            - bo * eo**2
            + do * eo
            + do * xo * yo
            + 3 * eo**2 * zo
            - 7 * eo * yo**2
            + 3 * xo * yo * zo
            + 4 * yo**2
            + zo,
            -3 * ao * co
            - 3 * ao * xo * zo
            - 9 * ao * yo
            - 3 * co * eo**2
            + 3 * eo * ho
            - 6 * eo * xo * zo
            + 3 * ho * xo * yo
            + 12 * xo * yo**2
            + 3 * xo * zo
            + yo,
            co * qo + co * xo**2 + qo * xo * zo + 3 * qo * yo + 2 * xo,
            ao - eo**2 - 2 * eo * xo * yo,
            bo + xo * yo * zo + 3 * yo**2,
            co + xo * zo + 3 * yo,
            ao * zo
            - bo * eo
            + bo * xo * yo
            + do
            + 3 * eo * zo
            - 3 * xo * yo * zo
            - 7 * yo**2,
            eo + xo * yo,
            -co * eo + co * xo * yo + ho - 2 * xo * zo,
            qo + xo**2,
        )
    )

    # This source-linear change makes the linear part the identity.
    x, y, z, a, b, c, d, e, h, q = sp.symbols("x y z a b c d e h q")
    X = (x, y, z, a, b, c, d, e, h, q)
    old_from_new = (z / 2, y, x, a, b, c - 3 * y, d, e, h, q)
    normalized = expanded(
        public.subs(dict(zip(old, old_from_new)), simultaneous=True)
    )

    identity = sp.Matrix(X)
    nonlinear = expanded(normalized - identity)
    R2 = expanded(homogeneous_part(item, X, 2) for item in nonlinear)
    R3 = expanded(homogeneous_part(item, X, 3) for item in nonlinear)

    gamma = expanded(
        (
            a * e * x
            - 3 * a * y**2
            - b * e**2
            + d * y * z / 2
            + 3 * e**2 * x
            - 7 * e * y**2
            + 3 * x * y * z / 2,
            -3 * a * x * z / 2
            - 3 * c * e**2
            + 9 * e**2 * y
            - 3 * e * x * z
            + 3 * h * y * z / 2
            + 6 * y**2 * z,
            c * z**2 / 4 + q * x * z / 2 - 3 * y * z**2 / 4,
            -e * y * z,
            x * y * z / 2,
            b * y * z / 2 - 3 * x * y * z / 2,
            c * y * z / 2 - 3 * y**2 * z / 2,
        )
    )
    B = sp.zeros(10, 7)
    for column, row in enumerate((0, 1, 2, 3, 4, 6, 8)):
        B[row, column] = 1

    W = sp.symbols("w1:8")
    tau, scale = sp.symbols("tau s")
    G = expanded(
        list(identity + tau * R2 + tau**2 * B * sp.Matrix(W))
        + list(sp.Matrix(W) - gamma)
        + [tau]
    )
    N = expanded(list(R2 + B * sp.Matrix(W)) + list(-gamma))

    public_points = (
        (0, 0, sp.Rational(-1, 4), 0, 0, 0, 0, 0, 0, 0),
        (
            1,
            sp.Rational(-3, 2),
            sp.Rational(13, 2),
            sp.Rational(-9, 4),
            3,
            -2,
            sp.Rational(-153, 8),
            sp.Rational(3, 2),
            7,
            -1,
        ),
        (
            -1,
            sp.Rational(3, 2),
            sp.Rational(13, 2),
            sp.Rational(-9, 4),
            3,
            2,
            sp.Rational(-153, 8),
            sp.Rational(3, 2),
            -7,
            -1,
        ),
    )
    normalized_points = tuple(
        (
            point[2],
            point[1],
            2 * point[0],
            point[3],
            point[4],
            point[5] + 3 * point[1],
            point[6],
            point[7],
            point[8],
            point[9],
        )
        for point in public_points
    )
    lifted_points = tuple(
        point + at(gamma, X, point) + (sp.Integer(1),)
        for point in normalized_points
    )

    return {
        "old": old,
        "public": public,
        "X": X,
        "old_from_new": old_from_new,
        "normalized": normalized,
        "R2": R2,
        "R3": R3,
        "gamma": gamma,
        "B": B,
        "W": W,
        "tau": tau,
        "scale": scale,
        "G": G,
        "N": N,
        "public_points": public_points,
        "normalized_points": normalized_points,
        "lifted_points": lifted_points,
    }


def verify_public_seed(data):
    old, public = data["old"], data["public"]
    xo, yo, zo, ao, bo, co, do, eo, ho, qo = old

    # Reconstruct G10 = T10 o (F x I7) o S10 independently.
    u = 1 + xo * yo
    seed3 = expanded(
        (
            u**3 * zo + yo**2 * u * (4 + 3 * xo * yo),
            yo + 3 * xo * u**2 * zo + 3 * xo * yo**2 * (4 + 3 * xo * yo),
            2 * xo - 3 * xo**2 * yo - xo**3 * zo,
        )
    )
    assert sp.factor(seed3.jacobian((xo, yo, zo)).det()) == -2

    A = ao + xo**2 * yo**2
    BB = bo + xo * yo * zo + 3 * yo**2
    C = co + xo * zo + 3 * yo
    D = do + xo * yo * (bo - 3 * zo) + ao * zo - eo * (bo - 3 * zo) - 7 * yo**2
    E = eo + xo * yo
    H = ho + xo * yo * co - co * eo - 2 * xo * zo
    QQ = qo + xo**2
    S = expanded((xo, yo, zo, A, BB, C, D, E, H, QQ))
    assert sp.factor(S.jacobian(old).det()) == 1
    factored = expanded(
        (
            seed3[0] - A * BB + D * E,
            seed3[1] - 3 * A * C + 3 * H * E,
            seed3[2] + C * QQ,
            A - E**2,
            BB,
            C,
            D,
            E,
            H,
            QQ,
        )
    )
    assert_zero_matrix(factored - public)

    U1, U2, U3, AA, BBB, CC, DD, EE, HH, QQQ = sp.symbols(
        "U1 U2 U3 AA BBB CC DD EE HH QQQ"
    )
    target_variables = (U1, U2, U3, AA, BBB, CC, DD, EE, HH, QQQ)
    target = expanded(
        (
            U1 - AA * BBB + DD * EE,
            U2 - 3 * AA * CC + 3 * HH * EE,
            U3 + CC * QQQ,
            AA - EE**2,
            BBB,
            CC,
            DD,
            EE,
            HH,
            QQQ,
        )
    )
    assert sp.factor(target.jacobian(target_variables).det()) == 1

    for point in data["public_points"]:
        assert at(public, old, point) == (sp.Rational(-1, 4),) + (0,) * 9

    # Exact m=1 tower relation and generic degree three.
    tower_gamma = 1 - sp.Rational(3, 2) * xo * yo - sp.Rational(1, 2) * xo**2 * zo
    tower_w = sp.expand((1 + xo * yo) * tower_gamma)
    tower_C = seed3[2] / 2
    tower_T = sp.expand(tower_C * seed3[1] / 2)
    tower_H = sp.expand(tower_C**2 * seed3[0])
    assert sp.expand(tower_w**3 - tower_w**2 + tower_T * tower_w - tower_H) == 0
    formal_w, formal_T, formal_H = sp.symbols("formal_w formal_T formal_H")
    tower_polynomial = sp.Poly(
        formal_w**3 - formal_w**2 + formal_T * formal_w - formal_H,
        formal_w,
        domain=sp.QQ.frac_field(formal_T, formal_H),
    )
    assert tower_polynomial.is_irreducible

    tower_s = tower_C / tower_w
    assert sp.cancel(tower_s - xo / u) == 0
    assert sp.cancel(seed3[1] - yo - 3 * tower_s * seed3[0]) == 0
    assert sp.cancel(1 - tower_s * yo - 1 / u) == 0
    assert sp.expand(
        tower_C - (xo - sp.Rational(3, 2) * xo**2 * yo - xo**3 * zo / 2)
    ) == 0

    return seed3


def verify_homogeneous_map(data):
    X, W = data["X"], data["W"]
    R2, R3, gamma, B = data["R2"], data["R3"], data["gamma"], data["B"]
    normalized, G, N = data["normalized"], data["G"], data["N"]
    tau, scale = data["tau"], data["scale"]

    L = sp.Matrix(data["old_from_new"]).jacobian(X)
    assert L.det() == sp.Rational(-1, 2)
    assert normalized.jacobian(X).subs(dict.fromkeys(X, 0)) == sp.eye(10)
    assert_zero_matrix(normalized - sp.Matrix(X) - R2 - R3)
    assert all(
        sp.Poly(item, *X).is_homogeneous
        and sp.Poly(item, *X).total_degree() == 2
        for item in R2
    )
    assert all(
        item == 0
        or (
            sp.Poly(item, *X).is_homogeneous
            and sp.Poly(item, *X).total_degree() == 3
        )
        for item in R3
    )
    cubic_coefficients, _ = coordinate_matrix(R3, X, 3)
    gamma_coefficients, _ = coordinate_matrix(gamma, X, 3)
    assert cubic_coefficients.rank() == 7
    assert gamma_coefficients.rank() == 7
    assert B.rank() == 7
    assert_zero_matrix(R3 - B * gamma)

    scaled_substitution = {variable: scale * variable for variable in X}
    f_scale = expanded(sp.Matrix(X) + scale * R2 + scale**2 * B * gamma)
    scaled_f = expanded(
        normalized.subs(scaled_substitution, simultaneous=True) / scale
    )
    assert_zero_matrix(f_scale - scaled_f)
    M = f_scale.jacobian(X)
    normalized_jacobian_scaled = normalized.jacobian(X).subs(
        scaled_substitution, simultaneous=True
    )
    assert_zero_matrix(M - normalized_jacobian_scaled)

    # Reduce I+s J_N to diag(J f_s, I_7).
    JN = N.jacobian(X + W)
    IN = sp.eye(17) + scale * JN
    left_N = sp.eye(17)
    left_N[:10, 10:] = -scale * B
    right_N = sp.eye(17)
    right_N[10:, :10] = scale * gamma.jacobian(X)
    expected_N = sp.diag(M, sp.eye(7))
    assert_zero_matrix(left_N * IN * right_N - expected_N)
    assert left_N.det() == right_N.det() == 1

    # Reduce the displayed 18x18 Jacobian to the same scaled seed block.
    variables18 = X + W + (tau,)
    JG = G.jacobian(variables18)
    assert JG[-1, -1] == 1 and all(JG[-1, j] == 0 for j in range(17))
    core = JG[:17, :17]
    left_G = sp.eye(17)
    left_G[:10, 10:] = -tau**2 * B
    right_G = sp.eye(17)
    right_G[10:, :10] = gamma.jacobian(X)
    M_tau = M.subs(scale, tau)
    assert_zero_matrix(left_G * core * right_G - sp.diag(M_tau, sp.eye(7)))
    assert left_G.det() == right_G.det() == 1

    nonlinear_G = expanded(G - sp.Matrix(variables18))
    for item in nonlinear_G:
        if item != 0:
            polynomial = sp.Poly(item, *variables18)
            assert polynomial.is_homogeneous and polynomial.total_degree() == 3

    common = (sp.Rational(-1, 4),) + (0,) * 9 + (0,) * 7 + (1,)
    assert len(set(data["lifted_points"])) == 3
    for point in data["lifted_points"]:
        assert at(G, variables18, point) == common

    # After the target shear Y -> Y-tau^2 BZ, the first block is f_tau;
    # W is then recovered uniquely from Z+gamma(X).
    Y = G[:10, :]
    Z = G[10:17, :]
    assert_zero_matrix(Y - tau**2 * B * Z - f_scale.subs(scale, tau))

    return {
        "source_linear_determinant": "-1/2",
        "public_jacobian_determinant": -2,
        "normalized_jacobian_determinant": 1,
        "cubic_coordinate_span_rank": 7,
        "N_determinant_identity": "det(I+s*J_N)=1",
        "homogeneous_map_dimension": 18,
        "homogeneous_map_degree": 3,
        "homogeneous_map_jacobian_determinant": 1,
        "generic_degree": 3,
        "collision_size": 3,
    }


def json_expression(expression):
    return sp.sstr(sp.expand(expression))


def machine_record(data, report):
    variables18 = data["X"] + data["W"] + (data["tau"],)
    common = (sp.Rational(-1, 4),) + (0,) * 9 + (0,) * 7 + (1,)
    return {
        "schema": "jacobian.cubic_homogeneous_map.v1",
        "coefficient_field": "QQ",
        "primary_seed": {
            "repository": "AndreasFinke/jacobian-10d",
            "path": "CONSTRUCTIONS.md",
        },
        "variables": [str(item) for item in variables18],
        "components": [json_expression(item) for item in data["G"]],
        "R2": [json_expression(item) for item in data["R2"]],
        "gamma": [json_expression(item) for item in data["gamma"]],
        "B": [[int(value) for value in data["B"].row(i)] for i in range(10)],
        "collision_points": [
            [str(value) for value in point] for point in data["lifted_points"]
        ],
        "common_image": [str(value) for value in common],
        "certificate": report,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, help="write the machine-readable certificate"
    )
    args = parser.parse_args()

    data = build_data()
    verify_public_seed(data)
    report = verify_homogeneous_map(data)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(machine_record(data, report), indent=2) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("CERTIFIED exact 10D reconstruction and displayed 18D cubic-homogeneous map")


if __name__ == "__main__":
    main()
