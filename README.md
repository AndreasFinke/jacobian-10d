# Cubic noninjective Keller map in dimension 10

This repository contains exact verification files for an explicit polynomial map

\[
G:\mathbb{Q}^{10}\to\mathbb{Q}^{10}
\]

with coordinate degrees

```text
(3, 3, 3, 3, 3, 2, 3, 2, 3, 2),
```

constant Jacobian determinant `-2`, and three distinct rational points with the same image.

## Verify with Python and SymPy

```bash
python3 -m pip install -r requirements.txt
python3 verify.py
```

Expected final data:

```text
det(Jg): -2
common image: (-1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0)
```

The Python verifier uses exact rational polynomial arithmetic. It forms the expanded `10 x 10` Jacobian, proves that the lower-right carrier block has determinant one, and computes the exact Schur complement. No floating-point tests are used.

## Verify with Wolfram Language

Evaluate `verify.wl` in Mathematica or a Wolfram Cloud notebook. It returns the determinant, verifies that the three source points are distinct, and displays their single common image.

## Files

- `verify.py` — concise exact SymPy certificate
- `verify.wl` — concise Wolfram Language certificate
- `PROOF.md` — construction and algebraic proof
- `cubic10_map.json` — machine-readable expanded map and collision data

The construction is derived from the known three-dimensional degree-seven counterexample by a polynomial stable-equivalence compression.
