# Stable degree reductions of the three-dimensional Jacobian counterexample

This repository contains exact certificates for three polynomial maps obtained from the known three-dimensional degree-seven counterexample by **stabilization** and polynomial changes of source and target coordinates.

The resulting dimension–degree trade-off is:

| Map | Dimension | Total degree | Component degrees |
|---|---:|---:|---|
| Original map $F$ | 3 | 7 | $(7,6,4)$ |
| One-register reduction $G_4$ | 4 | 6 | $(5,6,4,3)$ |
| Two-register reduction $G_5$ | 5 | 5 | $(5,5,4,3,2)$ |
| Seven-register reduction $G_{10}$ | 10 | 3 | $(3,3,3,3,3,2,3,2,3,2)$ |

Every map in the table has the exact constant Jacobian determinant

```math
-2
```

and an explicit fiber containing three distinct rational points.

## Starting map

Put $u=1+xy$ and define $F=(F_1,F_2,F_3)$ by

- $F_1=u^3z+y^2u(4+3xy)$,
- $F_2=y+3xu^2z+3xy^2(4+3xy)$,
- $F_3=2x-3x^2y-x^3z$.

The two small reductions come from the exact cancellations

```math
F_1+y^3F_3=3x^2y^2z+9xy^3+3xyz+4y^2+z,
```

```math
F_2+3y^2F_3=6x^2yz+18xy^2+3xz+y.
```

Introducing one register for $y^3$ gives the four-dimensional degree-six map

```math
G_4=\left(F_1+(t+y^3)F_3,\ F_2,\ F_3,\ t+y^3\right).
```

Introducing separate registers for $y^3$ and $y^2$ gives the five-dimensional degree-five map

```math
G_5=\left(F_1+(a+y^3)F_3,\ F_2+3(b+y^2)F_3,\ F_3,\ a+y^3,\ b+y^2\right).
```

The cubic map $G_{10}$ uses seven shared registers and a more substantial source/target factorization. All expanded formulas, collision points, and proofs are collected in one place:

**[Constructions and exact certificates](CONSTRUCTIONS.md)**

## Verification

Install SymPy and run the single canonical verifier:

```bash
python3 -m pip install -r requirements.txt
python3 verify_all.py
```

It checks, using exact rational polynomial arithmetic:

- the original three-dimensional map;
- the four-dimensional degree-six map;
- the five-dimensional degree-five map;
- the ten-dimensional cubic map;
- every component degree;
- every Jacobian determinant;
- every stated three-point collision;
- the compact factorization of the expanded ten-dimensional map.

The independent Wolfram Language check for the cubic map is in [`verify_cubic10.wl`](verify_cubic10.wl).

## Repository contents

- [`CONSTRUCTIONS.md`](CONSTRUCTIONS.md) — all maps, proofs, and exact collision data
- [`verify_all.py`](verify_all.py) — canonical exact SymPy verifier
- [`verify_cubic10.wl`](verify_cubic10.wl) — independent Wolfram Language check of $G_{10}$
- [`cubic10_map.json`](cubic10_map.json) — machine-readable expanded cubic map and collision data

## Claim boundary

These constructions improve explicit dimension–degree trade-offs. They are all stably equivalent to the same known three-dimensional map, so they do **not** provide a new geometric source of noninjectivity. No claim of optimality or publication priority is made.
