# Cubic-homogeneous form in dimension 18

**Updated:** 4 August 2026  
**Status:** exact characteristic-zero certificate; no claim of global minimality

## What “cubic homogeneous” means

The ten-dimensional map in this repository has total degree three, but its
nonlinear part contains both quadratic and cubic terms.

A cubic-homogeneous map has the stricter form

```math
G(U)=U+H_3(U),
```

where every nonzero monomial in every coordinate of $H_3$ has total degree
exactly three. For example, $x^2y$ is allowed, while $x^2$ is not.

This document gives such a counterexample in dimension $18$. It does **not**
improve the dimension-$10$ bound for unrestricted degree-three maps; it gives
a smaller realization inside the narrower cubic-homogeneous normal form.

## Result

There is an explicit polynomial map

```math
G:\mathbb{Q}^{18}\longrightarrow\mathbb{Q}^{18}
```

of the form $G=I+H_3$ such that:

- every nonzero coordinate of $H_3$ is homogeneous cubic;
- $\det JG=1$;
- the generic fiber has degree three;
- one fiber contains three distinct rational points.

## Compact construction

Use ten variables

```math
X=(x,y,z,a,b,c,d,e,h,q),
```

seven carrier variables

```math
W=(w_1,w_2,w_3,w_4,w_5,w_6,w_7),
```

and one homogenizing variable $\tau$.

Define the quadratic vector $R_2=(Q_1,\ldots,Q_{10})$ by:

- $Q_1=-ab+de+4y^2$;
- $Q_2=-3ac+3eh+\frac32xz$;
- $Q_3=cq$;
- $Q_4=-e^2$;
- $Q_5=3y^2$;
- $Q_6=\frac12xz$;
- $Q_7=ax-be+3ex-7y^2$;
- $Q_8=\frac12yz$;
- $Q_9=-ce+3ey-xz$;
- $Q_{10}=\frac14z^2$.

Define the cubic vector $\gamma=(\gamma_1,\ldots,\gamma_7)$ by:

```math
\gamma_1=aex-3ay^2-be^2+\frac12dyz+3e^2x-7ey^2+\frac32xyz.
```

```math
\gamma_2=-\frac32axz-3ce^2+9e^2y-3exz+\frac32hyz+6y^2z.
```

```math
\gamma_3=\frac14cz^2+\frac12qxz-\frac34yz^2.
```

```math
\gamma_4=-eyz.
```

```math
\gamma_5=\frac12xyz.
```

```math
\gamma_6=\frac12byz-\frac32xyz.
```

```math
\gamma_7=\frac12cyz-\frac32y^2z.
```

Let

```math
BW=(w_1,w_2,w_3,w_4,w_5,0,w_6,0,w_7,0).
```

Then define

```math
G(X,W,\tau)=
\left(
X+\tau R_2(X)+\tau^2BW,
\ W-\gamma(X),
\ \tau
\right).
```

Every nonlinear term has total degree three:

- $\tau R_2$ has degree $1+2$;
- $\tau^2BW$ has degree $2+1$;
- every $\gamma_i$ has degree three.

The fully expanded coordinates are stored in
[`cubic_homogeneous18.json`](cubic_homogeneous18.json).

## Why the determinant is one

After the exact linear source normalization

```math
(x_{\rm old},y_{\rm old},z_{\rm old},c_{\rm old})
=
\left(\frac z2,y,x,c-3y\right),
```

the public ten-dimensional map becomes

```math
f(X)=X+R_2(X)+R_3(X),
```

with identity linear part and $\det Jf=1$.

The ten cubic coordinates of $R_3$ span a seven-dimensional vector space, and
exact coefficient reduction gives

```math
R_3=B\gamma.
```

For an indeterminate $s$, put

```math
f_s(X)=s^{-1}f(sX)=X+sR_2(X)+s^2B\gamma(X).
```

Because $f_s$ is obtained from $f$ by invertible linear scaling,

```math
\det Jf_s=1.
```

Now set

```math
N(X,W)=\left(R_2(X)+BW,-\gamma(X)\right).
```

Two explicit determinant-one block operations reduce

```math
I_{17}+sJ_N
```

to

```math
\operatorname{diag}(Jf_s,I_7).
```

The verifier performs this matrix identity coefficient by coefficient. Hence

```math
\det(I_{17}+sJ_N)=1.
```

The upper $17\times17$ block of $JG$ is the same identity after substituting
$s=\tau$. The final output is exactly $\tau$, so the last Jacobian row is the
last identity row. Therefore

```math
\det JG=1.
```

The independent Singular verifier also expands and directly computes the
determinant of the displayed $18\times18$ Jacobian.

## Exact collision

Order the variables as

```math
(x,y,z,a,b,c,d,e,h,q,w_1,w_2,w_3,w_4,w_5,w_6,w_7,\tau).
```

The three distinct points are:

```math
P_0=
\left(-\frac14,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,1\right).
```

```math
P_+=
\left(
\frac{13}{2},-\frac32,2,-\frac94,3,-\frac{13}{2},-\frac{153}{8},
\frac32,7,-1,
\frac{99}{16},-\frac{45}{8},-\frac{17}{2},\frac92,-\frac{39}{4},
\frac{99}{4},3,1
\right).
```

```math
P_-=
\left(
\frac{13}{2},\frac32,-2,-\frac94,3,\frac{13}{2},-\frac{153}{8},
\frac32,-7,-1,
\frac{99}{16},\frac{45}{8},\frac{17}{2},\frac92,-\frac{39}{4},
\frac{99}{4},-3,1
\right).
```

They satisfy

```math
G(P_0)=G(P_+)=G(P_-)
=
\left(-\frac14,0,\ldots,0,1\right).
```

The generic degree remains three: after the target shear

```math
(Y,Z,\tau)\longmapsto(Y-\tau^2BZ,Z,\tau),
```

the first ten outputs become $f_\tau(X)$, while $W$ is recovered uniquely from
$Z+\gamma(X)$.

## Relation to the other constructions in this repository

| Dimension | Form | Nonlinear degrees | Role |
|---:|---|---|---|
| 10 | general total-degree-three map | quadratic and cubic | smaller unrestricted cubic construction |
| 18 | $I+H_3$ | cubic only | stricter cubic-homogeneous construction |

The dimension-$18$ result should therefore be compared only with other
explicit cubic-homogeneous maps, not with the smaller dimension-$10$ general
cubic map.

A dated primary-source audit found earlier explicit cubic-homogeneous formulas
in dimensions $23$ and $24$, and no public explicit example in dimension at
most $17$. This is a priority search result, not a proof that dimension $18$ is
minimal or that no unindexed construction exists.

## Verification

Install SymPy and run:

```bash
python3 verify_cubic_homogeneous18.py \
  --output cubic_homogeneous18.json
```

For an independent exact check with Singular:

```bash
Singular -q verify_cubic_homogeneous18.sing
```

The Python verifier reconstructs the map from the ten-dimensional formulas in
this repository. It does not assume the displayed $R_2$, $\gamma$, or rank
factorization.

## Claim boundary

This repository certifies:

- the explicit $18$-variable map;
- cubic homogeneity of its nonlinear part;
- the exact identity $\det JG=1$;
- three distinct rational preimages of one point;
- generic degree three;
- the rank-seven compression from the normalized ten-dimensional map.

It does **not** claim:

- that dimension $18$ is globally minimal;
- that this improves the dimension-$10$ unrestricted cubic construction;
- that the construction supplies a new geometric source of noninjectivity;
- exhaustive publication priority over private or unindexed work.
