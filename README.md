# Cubic noninjective Keller map in dimension 10

This repository gives an exact certificate for an explicit polynomial map

```math
G:\mathbb{Q}^{10}\longrightarrow\mathbb{Q}^{10}
```

with coordinate degrees

```math
(3,3,3,3,3,2,3,2,3,2),
```

constant Jacobian determinant

```math
\det JG=-2,
```

and three distinct rational points with the same image. Thus $G$ is a noninjective cubic Keller map.

The construction, exact collision, and algebraic factorization proof are given in [`PROOF.md`](PROOF.md).

## Verify with Python and SymPy

```bash
python3 -m pip install -r requirements.txt
python3 verify.py
```

The verifier uses exact rational polynomial arithmetic. It checks the coordinate degrees, constructs the symbolic $10\times10$ Jacobian, proves the determinant through an exact block-determinant calculation, and evaluates the three rational preimages.

Expected final data:

```text
det(Jg): -2
common image: (-1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0)
```

No floating-point approximation or sampling is used.

## Verify with Wolfram Language

Evaluate [`verify.wl`](verify.wl) in Mathematica or a Wolfram Cloud notebook. It computes the symbolic determinant, verifies that the three source points are distinct, and displays their single common image.

## Files

- [`PROOF.md`](PROOF.md) — construction and algebraic proof
- [`verify.py`](verify.py) — concise exact SymPy certificate
- [`verify.wl`](verify.wl) — concise Wolfram Language certificate
- [`cubic10_map.json`](cubic10_map.json) — machine-readable expanded map and collision data

The construction is derived from the known three-dimensional degree-seven counterexample by a polynomial stable-equivalence compression. No claim of minimality is made.
