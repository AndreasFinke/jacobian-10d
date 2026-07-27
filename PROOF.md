# An explicit cubic noninjective Keller map in dimension 10

**Date:** 26 July 2026  
**Status:** exact characteristic-zero certificate; no claim of minimality or publication priority

## Result

There is an explicit polynomial map over the rationals,

$$
G:\mathbb{Q}^{10}\longrightarrow\mathbb{Q}^{10},
$$

which, after base change, is also a polynomial map on $\mathbb{C}^{10}$. Its total degree is three, its Jacobian determinant is the nonzero constant

$$
\det JG=-2,
$$

and one fiber contains three distinct rational points. Therefore $G$ is a noninjective cubic Keller map.

Use the ordered variables

$$
(x,y,z,a,b,c,d,e,h,q).
$$

The ten coordinates are

$$
\begin{aligned}
G_1={}&-ab+aez-3ay^2-be^2+de+dxy+3e^2z-7ey^2\\
     &\quad+3xyz+4y^2+z,\\[2mm]
G_2={}&-3ac-3axz-9ay-3ce^2+3eh-6exz+3hxy\\
     &\quad+12xy^2+3xz+y,\\[2mm]
G_3={}&cq+cx^2+qxz+3qy+2x,\\
G_4={}&a-e^2-2exy,\\
G_5={}&b+xyz+3y^2,\\
G_6={}&c+xz+3y,\\
G_7={}&az-be+bxy+d+3ez-3xyz-7y^2,\\
G_8={}&e+xy,\\
G_9={}&-ce+cxy+h-2xz,\\
G_{10}={}&q+x^2.
\end{aligned}
$$

Their total degrees are

$$
(3,3,3,3,3,2,3,2,3,2).
$$

The expanded map contains 50 monomial terms.

## Exact collision

Define

$$
\begin{aligned}
P_0={}&\left(0,0,-\frac14,0,0,0,0,0,0,0\right),\\[1mm]
P_+={}&\left(1,-\frac32,\frac{13}{2},-\frac94,3,-2,
-\frac{153}{8},\frac32,7,-1\right),\\[1mm]
P_-={}&\left(-1,\frac32,\frac{13}{2},-\frac94,3,2,
-\frac{153}{8},\frac32,-7,-1\right).
\end{aligned}
$$

These points are pairwise distinct and satisfy

$$
G(P_0)=G(P_+)=G(P_-)
=\left(-\frac14,0,0,0,0,0,0,0,0,0\right).
$$

Everything in this certificate is exact over $\mathbb{Q}$; no numerical approximation is used.

## Construction

Start with the known three-dimensional map. Put

$$
u=1+xy
$$

and define

$$
\begin{aligned}
f_1&=u^3z+y^2u(4+3xy),\\
f_2&=y+3xu^2z+3xy^2(4+3xy),\\
f_3&=2x-3x^2y-x^3z.
\end{aligned}
$$

This map has

$$
\det Jf=-2
$$

and the three-point collision in its first three variables.

### Source automorphism

Adjoin seven variables and define

$$
\begin{aligned}
A&=a+x^2y^2,\\
B&=b+xyz+3y^2,\\
C&=c+xz+3y,\\
D&=d+xy(b-3z)+az-e(b-3z)-7y^2,\\
E&=e+xy,\\
H&=h+xyc-ce-2xz,\\
Q&=q+x^2.
\end{aligned}
$$

Set

$$
S(x,y,z,a,b,c,d,e,h,q)
=(x,y,z,A,B,C,D,E,H,Q).
$$

This is a polynomial automorphism. Its inverse is obtained polynomially in the following order:

$$
\begin{aligned}
e&=E-xy,\\
a&=A-x^2y^2,\\
b&=B-xyz-3y^2,\\
c&=C-xz-3y,\\
q&=Q-x^2,\\
d&=D-xy(b-3z)-az+e(b-3z)+7y^2,\\
h&=H-xyc+ce+2xz.
\end{aligned}
$$

In particular,

$$
\det JS=1.
$$

### Target automorphism

For coordinates $(U_1,U_2,U_3,A,B,C,D,E,H,Q)$, define

$$
\begin{aligned}
T(U_1,U_2,U_3,A,B,C,D,E,H,Q)
=\big(&U_1-AB+DE,\\
      &U_2-3AC+3HE,\\
      &U_3+CQ,\\
      &A-E^2,B,C,D,E,H,Q\big).
\end{aligned}
$$

To invert $T$, first recover

$$
A=V_4+V_8^2,
$$

and then use

$$
\begin{aligned}
U_1&=V_1+AV_5-V_7V_8,\\
U_2&=V_2+3AV_6-3V_9V_8,\\
U_3&=V_3-V_6V_{10}.
\end{aligned}
$$

The remaining seven coordinates are read off directly. Hence $T$ is a polynomial automorphism and

$$
\det JT=1.
$$

### Composition

The displayed cubic map is exactly

$$
G
=
T\circ\left(f\times\operatorname{id}_{\mathbb{C}^{7}}\right)\circ S.
$$

Therefore

$$
\det JG
=
(\det JT)(\det Jf)(\det JS)
=
(1)(-2)(1)
=
-2.
$$

Expanding the composition gives precisely the ten polynomials displayed above.

For each of the three colliding points of $f$, choose the seven source variables so that

$$
A=B=C=D=E=H=Q=0.
$$

This gives the points $P_0,P_+,P_-$ above and transports the collision to $G$.

## Independent symbolic verification

The SymPy verifier differentiates the expanded ten-coordinate map and partitions its Jacobian into blocks,

$$
JG=
\begin{pmatrix}
J_{xx} & J_{xw}\\
J_{wx} & J_{ww}
\end{pmatrix},
$$

where the first block row and column correspond to $(x,y,z)$ and the second to $(a,b,c,d,e,h,q)$.

It verifies exactly that

$$
\det J_{ww}=1
$$

and computes the Schur complement

$$
J_{xx}-J_{xw}J_{ww}^{-1}J_{wx}.
$$

The determinant of this $3\times3$ matrix is exactly $-2$. By the block determinant identity,

$$
\det JG
=
\det J_{ww}\,
\det\!\left(
J_{xx}-J_{xw}J_{ww}^{-1}J_{wx}
\right)
=
-2.
$$

The same script checks all coordinate degrees and evaluates the three collision points over exact rationals.

Run:

```bash
python3 -m pip install -r requirements.txt
python3 verify.py
```

Expected output includes:

```text
degrees: [3, 3, 3, 3, 3, 2, 3, 2, 3, 2]
det(Jg): -2
common image: (-1/4, 0, 0, 0, 0, 0, 0, 0, 0, 0)
```

The independent Wolfram Language calculation is in [`verify.wl`](verify.wl).

## Reduction ladder

The same factorization gives the following stable-equivalence ladder from the original degree-seven map in dimension three:

| Dimension | Degree | Added variables | Main reduction |
|---:|---:|---:|---|
| 5 | 6 | 2 | Cancel the degree-seven product using $AB$ |
| 6 | 5 | 3 | Share $x^2y^2$, $xyz+3y^2$, and $xz+3y$ |
| 9 | 4 | 6 | Add the coupled corrections $DE$ and $3HE$, then replace $A$ by $A-E^2$ |
| 10 | 3 | 7 | Add $Q=q+x^2$ and cancel the remaining quartic using $CQ$ |

The dimension-ten member is the first map in this ladder for which every coordinate is cubic.

## Relation to the earlier dimension-19 construction

The public dimension-19 construction uses a mechanical Bass--Connell--Wright reduction with sixteen carrier variables. The earlier carrier audit checked all coordinate subsets of those sixteen variables and found that no proper subset remains cubic.

That calculation does not cover nonlinear recombinations of carriers or a different stable-equivalence circuit. The construction here does both. It factors sums and shares the expressions

$$
xy,\qquad xyz+3y^2,\qquad xz+3y
$$

across several coordinates, while the coupled carriers $D$ and $H$ absorb the cross-terms created by the source and target shears. It therefore requires seven added variables rather than sixteen.

## Claim boundary

The repository certifies:

- the explicit polynomial map;
- total degree three;
- the exact identity $\det JG=-2$;
- three distinct exact rational preimages of one point;
- the source/target stable-equivalence factorization.

It does **not** prove that dimension ten is minimal. Cubic counterexamples in dimensions four through nine may still exist. Publication priority is also not asserted here.