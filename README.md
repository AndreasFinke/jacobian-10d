# Explicit degree reductions of the three-dimensional Jacobian counterexample

[![Exact verification](https://github.com/AndreasFinke/jacobian-10d/actions/workflows/verify.yml/badge.svg)](https://github.com/AndreasFinke/jacobian-10d/actions/workflows/verify.yml)

This repository gives exact certificates for several polynomial maps obtained
from the known three-dimensional degree-seven counterexample by stabilization
and polynomial changes of source and target coordinates.

It contains two related results:

1. a dimension-degree ladder ending with a general total-degree-three map in
   dimension ten;
2. a stricter cubic-homogeneous map of the form $I+H_3$ in dimension eighteen.

## Dimension-degree ladder

| Map | Dimension | Total degree | Component degrees |
|---|---:|---:|---|
| Original map $F$ | 3 | 7 | $(7,6,4)$ |
| One-register reduction $G_4$ | 4 | 6 | $(5,6,4,3)$ |
| Two-register reduction $G_5$ | 5 | 5 | $(5,5,4,3,2)$ |
| Five-register reduction $G_8$ | 8 | 4 | $(3,4,4,3,3,3,2,4)$ |
| Seven-register reduction $G_{10}$ | 10 | 3 | $(3,3,3,3,3,2,3,2,3,2)$ |

Every map in this table has exact constant Jacobian determinant

```math
-2
```

and an explicit fiber containing three distinct rational points.

## Cubic-homogeneous form

The ten-dimensional map has total degree three, but its nonlinear part mixes
quadratic and cubic terms.

The repository also certifies an eighteen-dimensional map

```math
G(U)=U+H_3(U)
```

such that every nonzero monomial of $H_3$ has total degree exactly three. It
satisfies

```math
\det JG=1,
```

has generic degree three, and has an exact three-point rational collision.

This is a stricter normal form, not an improvement over dimension ten for
general degree-three maps.

The compact construction, proof, collision, comparison, and claim boundary are
in:

**[Cubic-homogeneous form in dimension 18](CUBIC_HOMOGENEOUS.md)**

## Starting map

Put $u=1+xy$ and define $F=(F_1,F_2,F_3)$ by

- $F_1=u^3z+y^2u(4+3xy)$,
- $F_2=y+3xu^2z+3xy^2(4+3xy)$,
- $F_3=2x-3x^2y-x^3z$.

The first two reductions follow from the exact cancellations

```math
F_1+y^3F_3=3x^2y^2z+9xy^3+3xyz+4y^2+z,
```

```math
F_2+3y^2F_3=6x^2yz+18xy^2+3xz+y.
```

The four-dimensional and five-dimensional maps are

```math
G_4=\left(F_1+(t+y^3)F_3,\ F_2,\ F_3,\ t+y^3\right),
```

```math
G_5=\left(F_1+(a+y^3)F_3,\ F_2+3(b+y^2)F_3,\ F_3,\ a+y^3,\ b+y^2\right).
```

The degree-four map $G_8$ uses five shared carrier coordinates; the general
cubic map $G_{10}$ uses seven. Their compact factorizations, expanded formulas,
exact collision points, and proofs are collected in:

**[Constructions and exact certificates](CONSTRUCTIONS.md)**

## Verification

Install SymPy:

```bash
python3 -m pip install -r requirements.txt
```

Verify the dimension-degree ladder:

```bash
python3 verify_all.py
```

Verify the cubic-homogeneous map and regenerate its machine-readable record:

```bash
python3 verify_cubic_homogeneous18.py \
  --output cubic_homogeneous18.json
```

The independent checks are:

```bash
# Wolfram Language check of the ten-dimensional general cubic map
wolframscript -file verify_cubic10.wl

# Singular check of the displayed eighteen-dimensional homogeneous map
Singular -q verify_cubic_homogeneous18.sing
```

GitHub Actions runs both Python verifiers on every push and pull request.

## Repository contents

- [`CONSTRUCTIONS.md`](CONSTRUCTIONS.md) — maps of dimensions $3,4,5,8,10$, factorizations, proofs, and collisions
- [`CUBIC_HOMOGENEOUS.md`](CUBIC_HOMOGENEOUS.md) — compact dimension-$18$ homogeneous construction and proof
- [`verify_all.py`](verify_all.py) — exact SymPy verifier for the dimension-degree ladder
- [`verify_cubic_homogeneous18.py`](verify_cubic_homogeneous18.py) — exact reconstruction and verification of the homogeneous map
- [`verify_cubic10.wl`](verify_cubic10.wl) — independent Wolfram Language check of $G_{10}$
- [`verify_cubic_homogeneous18.sing`](verify_cubic_homogeneous18.sing) — independent Singular check of the displayed $18\times18$ Jacobian
- [`cubic10_map.json`](cubic10_map.json) — machine-readable ten-dimensional map and collision
- [`cubic_homogeneous18.json`](cubic_homogeneous18.json) — machine-readable homogeneous map and collision

## Claim boundary

All constructions in this repository are obtained from the same known
three-dimensional counterexample by stable-equivalence operations. They do
**not** provide a new geometric source of noninjectivity.

The dimension-$18$ map is potentially a smaller explicit construction within
the cubic-homogeneous normal form. It is not a smaller unrestricted cubic map
than the dimension-$10$ construction, and no claim is made that dimension
$18$ is globally minimal.
