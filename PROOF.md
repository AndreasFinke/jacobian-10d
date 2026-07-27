# A cubic Keller counterexample in dimension 10

**Date:** 26 July 2026
**Status:** exact characteristic-zero certificate; publication priority not asserted

## Result

There is an explicit polynomial map

\[
G:\mathbb C^{10}\longrightarrow\mathbb C^{10}
\]

of total degree three with

\[
\det JG=-2
\]

identically, and with a fiber containing three distinct rational points. Thus
`G` is a noninjective cubic Keller map.

The variables are ordered as

\[
(x,y,z,a,b,c,d,e,h,q).
\]

The ten coordinates are

\[
\begin{aligned}
G*1={}&-ab+aez-3ay^2-be^2+de+dxy+3e^2z-7ey^2\\
&\qquad+3xyz+4y^2+z,\\
G_2={}&-3ac-3axz-9ay-3ce^2+3eh-6exz+3hxy\\
&\qquad+12xy^2+3xz+y,\\
G_3={}&cq+cx^2+qxz+3qy+2x,\\
G_4={}&a-e^2-2exy,\\
G_5={}&b+xyz+3y^2,\\
G_6={}&c+xz+3y,\\
G_7={}&az-be+bxy+d+3ez-3xyz-7y^2,\\
G_8={}&e+xy,\\
G_9={}&-ce+cxy+h-2xz,\\
G*{10}={}&q+x^2.
\end{aligned}
\]

The component degrees are

```text
(3,3,3,3,3,2,3,2,3,2)
```

and the expanded map contains 50 monomial terms.

## Exact collision

The three distinct points

\[
\begin{aligned}
P*0={}&(0,0,-\tfrac14,0,0,0,0,0,0,0),\\
P*+={}&(1,-\tfrac32,\tfrac{13}2,-\tfrac94,3,-2,
-\tfrac{153}8,\tfrac32,7,-1),\\
P\_-={}&(-1,\tfrac32,\tfrac{13}2,-\tfrac94,3,2,
-\tfrac{153}8,\tfrac32,-7,-1)
\end{aligned}
\]

satisfy

\[
G(P*0)=G(P*+)=G(P\_-)=(-\tfrac14,0,0,0,0,0,0,0,0,0).
\]

Everything here is over the rationals; no numerical approximation is used.

## Construction

Start from the dimension-three map, with `u=1+xy`,

\[
\begin{aligned}
f_1&=u^3z+y^2u(4+3xy),\\
f_2&=y+3xu^2z+3xy^2(4+3xy),\\
f_3&=2x-3x^2y-x^3z.
\end{aligned}
\]

Its Jacobian determinant is `-2`, and it has the three-point collision stated
in the existing repository.

Adjoin seven carrier variables and apply the following source automorphism:

\[
\begin{aligned}
A&=a+x^2y^2,\\
B&=b+xyz+3y^2,\\
C&=c+xz+3y,\\
D&=d+xy(b-3z)+az-e(b-3z)-7y^2,\\
E&=e+xy,\\
H&=h+xyc-ce-2xz,\\
Q&=q+x^2.
\end{aligned}
\]

Thus

\[
S(x,y,z,a,b,c,d,e,h,q)=(x,y,z,A,B,C,D,E,H,Q).
\]

This is a polynomial automorphism. One explicit inverse is obtained in the
order

\[
\begin{aligned}
e&=E-xy,\\
a&=A-x^2y^2,\\
b&=B-xyz-3y^2,\\
c&=C-xz-3y,\\
q&=Q-x^2,\\
d&=D-xy(b-3z)-az+e(b-3z)+7y^2,\\
h&=H-xyc+ce+2xz.
\end{aligned}
\]

In particular, `det(JS)=1`.

Next apply the target automorphism

\[
\begin{aligned}
T(U_1,U_2,U_3,A,B,C,D,E,H,Q)=ig(&U_1-AB+DE,\\
&U_2-3AC+3HE,\\
&U_3+CQ,\\
&A-E^2,B,C,D,E,H,Q\big).
\end{aligned}
\]

Its inverse is polynomial: recover `A=V_4+V_8^2`, then

\[
\begin{aligned}
U*1&=V_1+AV_5-V_7V_8,\\
U_2&=V_2+3AV_6-3V_9V_8,\\
U_3&=V_3-V_6V*{10},
\end{aligned}
\]

with the other seven coordinates read off directly. Hence `det(JT)=1`.

The displayed map is exactly

\[
G=T\circ(f\times\operatorname{id}\_{\mathbb C^7})\circ S.
\]

Consequently

\[
\det JG=(\det JT)(\det Jf)(\det JS)=-2.
\]

Expanding this composition gives precisely the ten cubic polynomials above.
The collision is transported by taking the seven carrier outputs
`A=B=C=D=E=H=Q=0` over each of the three colliding points of `f`.

## Independent determinant check

The verifier does not rely only on the composition argument. It differentiates
the expanded ten-coordinate map, partitions its Jacobian as

\[
JG=\begin{pmatrix}J*{xx}&J*{xw}\\J*{wx}&J*{ww}\end{pmatrix},
\]

checks `det(Jww)=1`, computes `Jww^{-1}` exactly, and proves entry by entry that

\[
J*{xx}-J*{xw}J*{ww}^{-1}J*{wx}=Jf.
\]

The `10 x 10` determinant is therefore exactly `-2`. Three additional full
matrix determinants are evaluated at independent integer points as an indexing
cross-check.

Run:

```sh
python3 tools/verify_cubic10.py
python3 tools/verify_reduction_ladder.py
```

Expected final line:

```text
CERTIFIED: cubic noninjective Keller map C^10 -> C^10 with det J = -2.
```

## Reduction ladder

The same factorization was found by progressively sharing nonlinear pieces.
It gives a compact stable-equivalence ladder from the original `(dimension,
degree)=(3,7)` map:

| dimension | degree | added carriers | target reduction                                                        |
| --------: | -----: | -------------: | ----------------------------------------------------------------------- |
|         5 |      6 |              2 | cancel the degree-seven product with `AB`                               |
|         6 |      5 |              3 | share `x^2y^2`, `xyz+3y^2`, and `xz+3y`                                 |
|         9 |      4 |              6 | add the coupled corrections `DE` and `3HE`, then replace `A` by `A-E^2` |
|        10 |      3 |              7 | add `Q=q+x^2` and cancel the last quartic as `CQ`                       |

The dimension-ten member is the first point in this ladder where every
coordinate is cubic.

## Relation to the earlier dimension-19 cubic map

The public dimension-19 construction applies a mechanical
Bass--Connell--Wright reduction with sixteen carrier variables. The repository's
existing carrier audit checks all coordinate subsets of those sixteen carriers
and correctly finds that no proper subset remains cubic. That calculation does
not cover nonlinear recombination of carriers or a different stable-equivalence
circuit.

The construction here is of the latter kind. It factors _sums_ and shares the
three expressions

```text
x*y,
xyz + 3*y^2,
xz + 3*y,
```

across several coordinates, while the coupled corrections `D` and `H` absorb
all cross-terms created by the source and target shears. It therefore uses
seven rather than sixteen added variables.

## Claim boundary and priority

What is certified here is the explicit map, its total degree, its constant
Jacobian determinant, and its exact collision. No minimality theorem is
claimed: a cubic counterexample in dimensions 4 through 9 may still exist.

Targeted public searches on 26 July 2026 found the dimension-19 mechanical
reduction and its explicit statement that the gap between dimensions 4 and 19
was open, but found no earlier dimension-10 cubic construction. Because the
subject is developing on a day-scale, novelty and priority should be checked
carefully.
