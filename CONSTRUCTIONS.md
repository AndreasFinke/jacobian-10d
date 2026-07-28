# Constructions and exact certificates

**Updated:** 29 July 2026  
**Status:** exact characteristic-zero certificates; no claim of optimality or publication priority

This document is self-contained. It starts from the known three-dimensional counterexample and gives four polynomially stably equivalent maps with lower total degree in higher dimension.

## 1. Starting map

Put

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

## 2. Stable-equivalence principle

Suppose that $S$ and $T$ are polynomial automorphisms with Jacobian determinant $1$. For $m\geq0$, let $I_m$ be the identity map on $\mathbb{Q}^m$. Then

```math
G=T\circ(F\times I_m)\circ S
```

satisfies

```math
\det JG=\det JF=-2.
```

The constructions below give explicit $S$ and $T$. Their determinant identities are therefore exact consequences of the chain rule. The verifier also differentiates the expanded maps independently.

## 3. One-register reduction: degree six in dimension four

The identity

```math
F_1+y^3F_3=3x^2y^2z+9xy^3+3xyz+4y^2+z
```

cancels the highest-degree terms of $F_1$.

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

### Factorization

Define

```math
S_4(x,y,z,t)=(x,y,z,t+y^3)
```

and

```math
T_4(U_1,U_2,U_3,T)=(U_1+TU_3,U_2,U_3,T).
```

Both are polynomial automorphisms with Jacobian determinant $1$, and

```math
G_4=T_4\circ(F\times I_1)\circ S_4.
```

Hence

```math
\det JG_4=-2.
```

### Exact collision

The three points

```math
P^{(4)}_0=\left(0,0,-\frac14,0\right),
```

```math
P^{(4)}_+=\left(1,-\frac32,\frac{13}{2},\frac{27}{8}\right),
```

```math
P^{(4)}_-=\left(-1,\frac32,\frac{13}{2},-\frac{27}{8}\right)
```

have the common image

```math
G_4(P^{(4)}_0)=G_4(P^{(4)}_+)=G_4(P^{(4)}_-)=\left(-\frac14,0,0,0\right).
```

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

### Factorization

Define

```math
S_5(x,y,z,a,b)=(x,y,z,a+y^3,b+y^2)
```

and

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

have the common image

```math
G_5(P^{(5)}_0)=G_5(P^{(5)}_+)=G_5(P^{(5)}_-)=\left(-\frac14,0,0,0,0\right).
```

## 5. Five-register reduction: degree four in dimension eight

Use variables

```math
(x,y,z,a,b,d,e,h)
```

and define five carrier coordinates:

- $A=a+x^2y^2$,
- $B=b+xyz+3y^2$,
- $D=d+xy(b-3z)+az-e(b-3z)-7y^2$,
- $E=e+xy$,
- $H=h-(xz+3y)(xy-e)-2xz$.

The map has the compact form

```math
G_8=\left(F_1-AB+DE,\ F_2+3HE,\ F_3,\ A-E^2,\ B,\ D,\ E,\ H\right).
```

### Expanded map

```math
(G_8)_1=-ab+aez-3ay^2-be^2+de+dxy+3e^2z-7ey^2+3xyz+4y^2+z.
```

```math
(G_8)_2=3e^2xz+9e^2y+3eh-6exz+3hxy+12xy^2+3xz+y.
```

```math
(G_8)_3=-x^3z-3x^2y+2x.
```

```math
(G_8)_4=a-e^2-2exy.
```

```math
(G_8)_5=b+xyz+3y^2.
```

```math
(G_8)_6=az-be+bxy+d+3ez-3xyz-7y^2.
```

```math
(G_8)_7=e+xy.
```

```math
(G_8)_8=exz+3ey+h-x^2yz-3xy^2-2xz.
```

The component degrees are

```math
(3,4,4,3,3,3,2,4).
```

### Factorization

Define the source automorphism

```math
S_8(x,y,z,a,b,d,e,h)=(x,y,z,A,B,D,E,H).
```

It is inverted polynomially in the order

- $e=E-xy$,
- $a=A-x^2y^2$,
- $b=B-xyz-3y^2$,
- $d=D-xy(b-3z)-az+e(b-3z)+7y^2$,
- $h=H+(xz+3y)(xy-e)+2xz$.

Define the target automorphism

```math
T_8(U_1,U_2,U_3,A,B,D,E,H)=\left(U_1-AB+DE,\ U_2+3HE,\ U_3,\ A-E^2,\ B,\ D,\ E,\ H\right).
```

Its inverse first recovers $A=V_4+V_7^2$ and then uses

- $U_1=V_1+AV_5-V_6V_7$,
- $U_2=V_2-3V_8V_7$,
- $U_3=V_3$.

Both automorphisms have Jacobian determinant $1$, and

```math
G_8=T_8\circ(F\times I_5)\circ S_8.
```

Therefore

```math
\det JG_8=-2.
```

Equivalently, $G_8$ is obtained from the ten-dimensional carrier construction by setting its carrier coordinates $C$ and $Q$ to zero and deleting the corresponding identical input/output coordinates. The standalone factorization above proves the result without relying on that interpretation.

### Exact collision

The points

```math
P^{(8)}_0=\left(0,0,-\frac14,0,0,0,0,0\right),
```

```math
P^{(8)}_+=\left(1,-\frac32,\frac{13}{2},-\frac94,3,-\frac{153}{8},\frac32,7\right),
```

```math
P^{(8)}_-=\left(-1,\frac32,\frac{13}{2},-\frac94,3,-\frac{153}{8},\frac32,-7\right)
```

have the common image

```math
G_8(P^{(8)}_0)=G_8(P^{(8)}_+)=G_8(P^{(8)}_-)=\left(-\frac14,0,0,0,0,0,0,0\right).
```

## 6. Seven-register reduction: degree three in dimension ten

Use the ordered variables

```math
(x,y,z,a,b,c,d,e,h,q).
```

The expanded cubic map is:

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

Define

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

This is a polynomial automorphism. Its inverse is obtained in the order

- $e=E-xy$,
- $a=A-x^2y^2$,
- $b=B-xyz-3y^2$,
- $c=C-xz-3y$,
- $q=Q-x^2$,
- $d=D-xy(b-3z)-az+e(b-3z)+7y^2$,
- $h=H-xyc+ce+2xz$.

### Target automorphism

For coordinates $(U_1,U_2,U_3,A,B,C,D,E,H,Q)$, define $T_{10}$ by

- $V_1=U_1-AB+DE$,
- $V_2=U_2-3AC+3HE$,
- $V_3=U_3+CQ$,
- $V_4=A-E^2$,
- $(V_5,V_6,V_7,V_8,V_9,V_{10})=(B,C,D,E,H,Q)$.

To invert $T_{10}$, first recover $A=V_4+V_8^2$, then use

- $U_1=V_1+AV_5-V_7V_8$,
- $U_2=V_2+3AV_6-3V_9V_8$,
- $U_3=V_3-V_6V_{10}$.

Both automorphisms have Jacobian determinant $1$, and

```math
G_{10}=T_{10}\circ(F\times I_7)\circ S_{10}.
```

Therefore

```math
\det JG_{10}=-2.
```

### Exact collision

The points

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

## 7. Summary

| Map | Dimension | Total degree | Component degrees | Added variables |
|---|---:|---:|---|---:|
| $F$ | 3 | 7 | $(7,6,4)$ | 0 |
| $G_4$ | 4 | 6 | $(5,6,4,3)$ | 1 |
| $G_5$ | 5 | 5 | $(5,5,4,3,2)$ | 2 |
| $G_8$ | 8 | 4 | $(3,4,4,3,3,3,2,4)$ | 5 |
| $G_{10}$ | 10 | 3 | $(3,3,3,3,3,2,3,2,3,2)$ | 7 |

## 8. Verification

Run

```bash
python3 -m pip install -r requirements.txt
python3 verify_all.py
```

The verifier checks all five maps over exact rational polynomial arithmetic. It verifies every degree vector, every determinant, every collision, and the compact factorizations of $G_8$ and $G_{10}$. For both larger maps it also constructs the expanded symbolic Jacobian and performs an independent exact block-determinant calculation.

The independent Wolfram Language calculation for $G_{10}$ is in [`verify_cubic10.wl`](verify_cubic10.wl).

## 9. Claim boundary

The certificates establish the displayed formulas, total degrees, nonzero constant Jacobian determinants, exact rational collisions, and polynomial stable-equivalence factorizations.

All four derived maps are stably equivalent to $F$. They improve explicit dimension-degree trade-offs but do not supply a new geometric mechanism for noninjectivity. No minimality theorem or publication-priority claim is made.
