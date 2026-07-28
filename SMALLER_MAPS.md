# Smaller explicit degree reductions

**Date:** 28 July 2026  
**Status:** exact characteristic-zero certificates; no claim of optimality or publication priority

Starting from the known map

```math
F=(F_1,F_2,F_3):\mathbb{Q}^3\longrightarrow\mathbb{Q}^3,
```

put $u=1+xy$ and

- $F_1=u^3z+y^2u(4+3xy)$,
- $F_2=y+3xu^2z+3xy^2(4+3xy)$,
- $F_3=2x-3x^2y-x^3z$.

It has $\det JF=-2$ and maps the three points

```math
\left(0,0,-\frac14\right),\quad
\left(1,-\frac32,\frac{13}{2}\right),\quad
\left(-1,\frac32,\frac{13}{2}\right)
```

to $(-1/4,0,0)$.

The two elementary identities

```math
F_1+y^3F_3=3x^2y^2z+9xy^3+3xyz+4y^2+z
```

and

```math
F_2+3y^2F_3=6x^2yz+18xy^2+3xz+y
```

remove the degree-seven and degree-six leading parts. Introducing one or two register variables turns these identities into polynomial stable equivalences.

## A degree-six map in four variables

Use variables $(x,y,z,t)$ and define

```math
G^{(4)}_1=-tx^3z-3tx^2y+2tx+3x^2y^2z+9xy^3+3xyz+4y^2+z.
```

```math
G^{(4)}_2=3x^3y^2z+9x^2y^3+6x^2yz+12xy^2+3xz+y.
```

```math
G^{(4)}_3=-x^3z-3x^2y+2x.
```

```math
G^{(4)}_4=t+y^3.
```

The component degrees are

```math
(5,6,4,3).
```

This map is the composition of three maps:

1. the source automorphism $(x,y,z,t)\mapsto(x,y,z,t+y^3)$;
2. the stabilization $F\times I_1$;
3. the target automorphism $(U_1,U_2,U_3,T)\mapsto(U_1+TU_3,U_2,U_3,T)$.

Both automorphisms have Jacobian determinant one. Therefore

```math
\det JG^{(4)}=-2.
```

The three distinct points

```math
\left(0,0,-\frac14,0\right),
```

```math
\left(1,-\frac32,\frac{13}{2},\frac{27}{8}\right),
```

```math
\left(-1,\frac32,\frac{13}{2},-\frac{27}{8}\right)
```

all map to

```math
\left(-\frac14,0,0,0\right).
```

Thus $G^{(4)}$ is an explicit noninjective Keller map of total degree six in four variables.

## A degree-five map in five variables

Use variables $(x,y,z,a,b)$ and define

```math
G^{(5)}_1=-ax^3z-3ax^2y+2ax+3x^2y^2z+9xy^3+3xyz+4y^2+z.
```

```math
G^{(5)}_2=-3bx^3z-9bx^2y+6bx+6x^2yz+18xy^2+3xz+y.
```

```math
G^{(5)}_3=-x^3z-3x^2y+2x.
```

```math
G^{(5)}_4=a+y^3.
```

```math
G^{(5)}_5=b+y^2.
```

The component degrees are

```math
(5,5,4,3,2).
```

This time use the source automorphism

```math
(x,y,z,a,b)\longmapsto(x,y,z,a+y^3,b+y^2)
```

and the target automorphism

```math
(U_1,U_2,U_3,A,B)\longmapsto(U_1+AU_3,U_2+3BU_3,U_3,A,B).
```

Again both determinants are one, so

```math
\det JG^{(5)}=-2.
```

The three points

```math
\left(0,0,-\frac14,0,0\right),
```

```math
\left(1,-\frac32,\frac{13}{2},\frac{27}{8},-\frac94\right),
```

```math
\left(-1,\frac32,\frac{13}{2},-\frac{27}{8},-\frac94\right)
```

all map to

```math
\left(-\frac14,0,0,0,0\right).
```

Thus $G^{(5)}$ is an explicit noninjective Keller map of total degree five in five variables.

## Current explicit trade-off ladder

| Dimension | Total degree | Component degrees | Added variables |
|---:|---:|---|---:|
| 3 | 7 | $(7,6,4)$ | 0 |
| 4 | 6 | $(5,6,4,3)$ | 1 |
| 5 | 5 | $(5,5,4,3,2)$ | 2 |
| 9 | 4 | recorded in the earlier stable reduction | 6 |
| 10 | 3 | $(3,3,3,3,3,2,3,2,3,2)$ | 7 |

The first two new rows are substantially simpler than the ten-dimensional cubic compression. They still derive from the original three-sheeted map and therefore do not constitute a new geometric source of noninjectivity.

## Verification

Run

```bash
python3 -m pip install -r requirements.txt
python3 verify_small_maps.py
```

The script expands both Jacobian determinants directly over the rationals and checks the exact collisions.
