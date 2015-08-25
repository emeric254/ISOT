ISOT
====

Soit une matrice 3D de cases (X, Y, Z) de taille T

Position 2D (x et y)
```
x = X * T + (Y % 2) * T / 2
y = Y * T / 4 + Z * T / 2
```

Position 3D naturelle (x, y et z)
```
x = Y % 2 + Y / 2 + X
y = Y / 2 + X
z = Z
```
