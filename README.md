# Small explicit Keller counterexamples from the degree-seven map

This repository now contains exact certificates for three stable reductions of the known dimension-three counterexample:

| Dimension | Total degree | Component degrees |
|---:|---:|---|
| 4 | 6 | $(5,6,4,3)$ |
| 5 | 5 | $(5,5,4,3,2)$ |
| 10 | 3 | $(3,3,3,3,3,2,3,2,3,2)$ |

Every displayed map has constant Jacobian determinant

```math
-2
```

and three distinct rational points with one exact common image.

The particularly small new constructions are documented in [`SMALLER_MAPS.md`](SMALLER_MAPS.md). They come from the elementary cancellations

```math
F_1+y^3F_3=3x^2y^2z+9xy^3+3xyz+4y^2+z
```

and

```math
F_2+3y^2F_3=6x^2yz+18xy^2+3xz+y.
```

One register variable gives a degree-six counterexample in four variables; two registers give a degree-five counterexample in five variables.

## Verify the four- and five-dimensional maps

```bash
python3 -m pip install -r requirements.txt
python3 verify_small_maps.py
```

The script expands both Jacobian determinants directly over exact rational polynomial arithmetic and verifies both three-point collisions.

## Cubic map in dimension ten

The cubic construction is an explicit polynomial map

```math
G:\mathbb{Q}^{10}\longrightarrow\mathbb{Q}^{10}
```

with component degrees

```math
(3,3,3,3,3,2,3,2,3,2),
```

constant Jacobian determinant

```math
\det JG=-2,
```

and three distinct rational points with the same image. Its construction and stable-equivalence proof are in [`PROOF.md`](PROOF.md).

Verify it with:

```bash
python3 verify.py
```

The verifier constructs the symbolic $10\times10$ Jacobian, proves the determinant by an exact block-determinant calculation, and evaluates the rational collision. The independent Wolfram Language calculation is in [`verify.wl`](verify.wl).

## Files

- [`SMALLER_MAPS.md`](SMALLER_MAPS.md) — the four-dimensional degree-six and five-dimensional degree-five constructions
- [`verify_small_maps.py`](verify_small_maps.py) — direct exact SymPy certificates for those maps
- [`PROOF.md`](PROOF.md) — construction and proof of the ten-dimensional cubic map
- [`verify.py`](verify.py) — exact SymPy certificate for the cubic map
- [`verify.wl`](verify.wl) — independent Wolfram Language certificate
- [`cubic10_map.json`](cubic10_map.json) — machine-readable cubic map and collision data

All three maps are stable-equivalent compressions of the original three-dimensional degree-seven counterexample. They do not provide a new geometric source of noninjectivity, and no claim of optimality or publication priority is made.
