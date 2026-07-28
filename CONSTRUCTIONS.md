# Constructions and exact certificates

**Date:** 28 July 2026  
**Status:** exact characteristic-zero certificates; no claim of optimality or publication priority

## 1. The starting map

Let

```math
u=1+xy
```

and define

```math
F=(F_1,F_2,F_3):\mathbb{Q}^3\longrightarrow\mathbb{Q}^3
```

by

```math
F_1=u^3z+y^2u(4+3xy),
```

```math
F_2=y+3xu^2z+3xy^2(4+3xy),
```

```math
F_3=2x-3x^2y-x^3z.
```

Its component degrees are

```math
(7,6,4),
```

and

```math
\det JF=-2.
```

The three distinct rational points

```math
p_0=\left(0,0,-\frac14\right),
```

```math
p_+=\left(1,-\frac32,\frac{13}{2}\right),
```

```math
p_-=\left(-1,\frac32,\frac{13}{2}\right)
```

have the common image

```math
F(p_0)=F(p_+)=F(p_-)=\left(-\frac14,0,0\right).
```

Everything below is derived from this map by stabilization and polynomial coordinate changes.

## 2. Stable-equivalence principle

Suppose $S$ and $T$ are polynomial automorphisms with constant Jacobian determinant $1$. For any $m\geq 0$, let $I_m$ be the identity map on $\mathbb{Q}^m$. Then

```math
G=T\circ(F\times I_m)\circ S
```

satisfies

```math
\det JG=\det JF=-2.
```

If the auxiliary coordinates are chosen identically at several preimages of one point under $F$, the corresponding points remain a collision for $G$.

The constructions below use only this principle. Their determinant proofs therefore do not rely on numerical tests.

## 3. One-register reduction: degree six in dimension four

The identity

```math
F_1+y^3F_3=3x^2y^2z+9xy^3+3xyz+4y^2+z
```

cancels the degree-seven terms of $F_1$.

Use variables $(x,y,z,t)$ and define

```math
G_4=\left(F_1+(t+y^3)F_3,\ F_2,\ F_3,\ t+y^3\right).
```

### Expanded map

```math
(G_4)_1=-tx^3z-3tx^2y+2tx+3x^2y^2z+9xy^3+3xyz+4y^2+z.
```

```math
(G_4)_2=3x^3y^2z+9x^2y^3+6x^2yz+12xy^2+3xz+y.
```

```math
(G_4)_3=-x^3z-3x^2y+2x.
```

```math
(G_4)_4=t+y^3.
```

The component degrees are

```math
(5,6,4,3).
```

### Factorization and determinant

Use the source automorphism

```math
S_4(x,y,z,t)=(x,y,z,t+y^3)
```

and the target automorphism

```math
T_4(U_1,U_2,U_3,T)=(U_1+TU_3,U_2,U_3,T).
```

Both have Jacobian determinant $1$, and

```math
G_4=T_4\circ(F\times I_1)\circ S_4.
```

Hence

```math
\det JG_4=-2.
```

### Exact collision

The points

```math
P^{(4)}_0=\left(0,0,-\frac14,0\right),
```

```math
P^{(4)}_+=\left(1,-\frac32,\frac{13}{2},\frac{27}{8}\right),
```

```math
P^{(4)}_-=\left(-1,\frac32,\frac{13}{2},-\frac{27}{8}\right)
```

are distinct and satisfy

```math
G_4(P^{(4)}_0)=G_4(P^{(4)}_+)=G_4(P^{(4)}_-)=\left(-\frac14,0,0,0\right).
```

Thus $G_4$ is an explicit noninjective Keller map of total degree six in four variables.

## 4. Two-register reduction: degree five in dimension five

The second cancellation is

```math
F_2+3y^2F_3=6x^2yz+18xy^2+3xz+y.
```

Use variables $(x,y,z,a,b)$ and define

```math
G_5=\left(F_1+(a+y^3)F_3,\ F_2+3(b+y^2)F_3,\ F_3,\ a+y^3,\ b+y^2\right).
```

### Expanded map

```math
(G_5)_1=-ax^3z-3ax^2y+2ax+3x^2y^2z+9xy^3+3xyz+4y^2+z.
```

```math
(G_5)_2=-3bx^3z-9bx^2y+6bx+6x^2yz+18xy^2+3xz+y.
```

```math
(G_5)_3=-x^3z-3x^2y+2x.
```

```math
(G_5)_4=a+y^3.
```

```math
(G_5)_5=b+y^2.
```

The component degrees are

```math
(5,5,4,3,2).
```

### Factorization and determinant

Use the source automorphism

```math
S_5(x,y,z,a,b)=(x,y,z,a+y^3,b+y^2)
```

and the target automorphism

```math
T_5(U_1,U_2,U_3,A,B)=(U_1+AU_3,U_2+3BU_3,U_3,A,B).
```

Both have Jacobian determinant $1$, and

```math
G_5=T_5\circ(F\times I_2)\circ S_5.
```

Therefore

```math
\det JG_5=-2.
```

### Exact collision

The points

```math
P^{(5)}_0=\left(0,0,-\frac14,0,0\right),
```

```math
P^{(5)}_+=\left(1,-\frac32,\frac{13}{2},\frac{27}{8},-\frac94\right),
```

```math
P^{(5)}_-=\left(-1,\frac32,\frac{13}{2},-\frac{27}{8},-\frac94\right)
```

are distinct and satisfy

```math
G_5(P^{(5)}_0)=G_5(P^{(5)}_+)=G_5(P^{(5)}_-)=\left(-\frac14,0,0,0,0\right).
```

Thus $G_5$ is an explicit noninjective Keller map of total degree five in five variables.

## 5. Seven-register reduction: degree three in dimension ten

Use the ordered variables

```math
(x,y,z,a,b,c,d,e,h,q).
```

The expanded cubic map $G_{10}:\mathbb{Q}^{10}\to\mathbb{Q}^{10}$ is:

```math
(G_{10})_1=-ab+aez-3ay^2-be^2+de+dxy+3e^2z-7ey^2+3xyz+4y^2+z.
```

```math
(G_{10})_2=-3ac-3axz-9ay-3ce^2+3eh-6exz+3hxy+12xy^2+3xz+y.
```

```math
(G_{10})_3=cq+cx^2+qxz+3qy+2x.
```

```math
(G_{10})_4=a-e^2-2exy.
```

```math
(G_{10})_5=b+xyz+3y^2.
```

```math
(G_{10})_6=c+xz+3y.
```

```math
(G_{10})_7=az-be+bxy+d+3ez-3xyz-7y^2.
```

```math
(G_{10})_8=e+xy.
```

```math
(G_{10})_9=-ce+cxy+h-2xz.
```

```math
(G_{10})_{10}=q+x^2.
```

Its component degrees are

```math
(3,3,3,3,3,2,3,2,3,2).
```

### Source automorphism

Define the seven carrier coordinates

- $A=a+x^2y^2$,
- $B=b+xyz+3y^2$,
- $C=c+xz+3y$,
- $D=d+xy(b-3z)+az-e(b-3z)-7y^2$,
- $E=e+xy$,
- $H=h+xyc-ce-2xz$,
- $Q=q+x^2$.

Set

```math
S_{10}(x,y,z,a,b,c,d,e,h,q)=(x,y,z,A,B,C,D,E,H,Q).
```

This is a polynomial automorphism. Its inverse is obtained in the following order:

- $e=E-xy$,
- $a=A-x^2y^2$,
- $b=B-xyz-3y^2$,
- $c=C-xz-3y$,
- $q=Q-x^2$,
- $d=D-xy(b-3z)-az+e(b-3z)+7y^2$,
- $h=H-xyc+ce+2xz$.

In particular,

```math
\det JS_{10}=1.
```

### Target automorphism

For coordinates $(U_1,U_2,U_3,A,B,C,D,E,H,Q)$, define $T_{10}$ by

- $V_1=U_1-AB+DE$,
- $V_2=U_2-3AC+3HE$,
- $V_3=U_3+CQ$,
- $V_4=A-E^2$,
- $(V_5,V_6,V_7,V_8,V_9,V_{10})=(B,C,D,E,H,Q)$.

To invert $T_{10}$, first recover

```math
A=V_4+V_8^2,
```

and then use

- $U_1=V_1+AV_5-V_7V_8$,
- $U_2=V_2+3AV_6-3V_9V_8$,
- $U_3=V_3-V_6V_{10}$.

The remaining coordinates are read off directly. Hence

```math
\det JT_{10}=1.
```

### Composition and determinant

The expanded map above is exactly

```math
G_{10}=T_{10}\circ(F\times I_7)\circ S_{10}.
```

Therefore

```math
\det JG_{10}=(\det JT_{10})(\det JF)(\det JS_{10})=-2.
```

The canonical SymPy verifier also constructs the expanded $10\times10$ Jacobian and checks this determinant independently by an exact block-determinant calculation.

### Exact collision

The three distinct points

```math
P^{(10)}_0=\left(0,0,-\frac14,0,0,0,0,0,0,0\right),
```

```math
P^{(10)}_+=\left(1,-\frac32,\frac{13}{2},-\frac94,3,-2,-\frac{153}{8},\frac32,7,-1\right),
```

```math
P^{(10)}_-=\left(-1,\frac32,\frac{13}{2},-\frac94,3,2,-\frac{153}{8},\frac32,-7,-1\right)
```

have the common image

```math
G_{10}(P^{(10)}_0)=G_{10}(P^{(10)}_+)=G_{10}(P^{(10)}_-)=\left(-\frac14,0,0,0,0,0,0,0,0,0\right).
```

Thus $G_{10}$ is an explicit noninjective cubic Keller map in ten variables.

## 6. Summary

| Map | Dimension | Total degree | Component degrees | Added variables |
|---|---:|---:|---|---:|
| $F$ | 3 | 7 | $(7,6,4)$ | 0 |
| $G_4$ | 4 | 6 | $(5,6,4,3)$ | 1 |
| $G_5$ | 5 | 5 | $(5,5,4,3,2)$ | 2 |
| $G_{10}$ | 10 | 3 | $(3,3,3,3,3,2,3,2,3,2)$ | 7 |

## 7. Verification

Run

```bash
python3 -m pip install -r requirements.txt
python3 verify_all.py
```

The script checks all four maps over exact rational polynomial arithmetic. It verifies every degree vector, every determinant, every collision, and the compact factorization of $G_{10}$.

The independent Wolfram Language calculation for $G_{10}$ is in [`verify_cubic10.wl`](verify_cubic10.wl).

## 8. Claim boundary

The certificates establish the displayed formulas, total degrees, nonzero constant Jacobian determinants, and exact rational collisions.

All three derived maps are stably equivalent to $F$. They improve explicit dimension–degree trade-offs but do not supply a new geometric mechanism for the failure of injectivity. No minimality theorem or publication-priority claim is made.
