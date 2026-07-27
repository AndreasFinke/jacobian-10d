v = {x, y, z, a, b, c, d, e, h, q};

g = {
 -a*b + a*e*z - 3*a*y^2 - b*e^2 + d*e + d*x*y + 3*e^2*z - 7*e*y^2 + 3*x*y*z + 4*y^2 + z,
 -3*a*c - 3*a*x*z - 9*a*y - 3*c*e^2 + 3*e*h - 6*e*x*z + 3*h*x*y + 12*x*y^2 + 3*x*z + y,
 c*q + c*x^2 + q*x*z + 3*q*y + 2*x,
 a - e^2 - 2*e*x*y,
 b + x*y*z + 3*y^2,
 c + x*z + 3*y,
 a*z - b*e + b*x*y + d + 3*e*z - 3*x*y*z - 7*y^2,
 e + x*y,
 -c*e + c*x*y + h - 2*x*z,
 q + x^2
};

p = {
 {0, 0, -1/4, 0, 0, 0, 0, 0, 0, 0},
 {1, -3/2, 13/2, -9/4, 3, -2, -153/8, 3/2, 7, -1},
 {-1, 3/2, 13/2, -9/4, 3, 2, -153/8, 3/2, -7, -1}
};

images = (g /. Thread[v -> #]) & /@ p;

{
 Factor[Det[Table[D[g[[i]], v[[j]]], {i, 10}, {j, 10}]]],
 Length[DeleteDuplicates[p]] == 3,
 DeleteDuplicates[images]
}
