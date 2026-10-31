+++
id = "algebra-category-theory/braided-monoidal-category"
title = "Braided monoidal category"
kind = "definition"
summary = "A monoidal category with natural exchanges of tensor factors satisfying both hexagon axioms."
aliases = ["braided category"]
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/monoidal-category", "algebra-category-theory/natural-isomorphism"]
+++

A **braided monoidal category** is a [[algebra-category-theory/monoidal-category|monoidal category]] with a [[algebra-category-theory/natural-isomorphism|natural isomorphism]]
\[
\beta_{X,Y}:X\otimes Y\longrightarrow Y\otimes X
\]
satisfying both hexagon axioms below. The associator is \(\alpha\), and compositions act from right to left:
\[
\alpha_{Y,Z,X}\beta_{X,Y\otimes Z}\alpha_{X,Y,Z}
=(1_Y\otimes\beta_{X,Z})\alpha_{Y,X,Z}(\beta_{X,Y}\otimes1_Z),
\]
\[
\alpha^{-1}_{Z,X,Y}\beta_{X\otimes Y,Z}\alpha^{-1}_{X,Y,Z}
=(\beta_{X,Z}\otimes1_Y)\alpha^{-1}_{X,Z,Y}(1_X\otimes\beta_{Y,Z}).
\]
The maps \(\beta\) are the **braiding**. Unlike a symmetry, a braiding is not required to satisfy \(\beta_{Y,X}\beta_{X,Y}=1\).

## The two hexagons

The first says that moving \(X\) past a pair \(Y,Z\) agrees with moving it past each factor in turn:

```tikz-cd
& X\otimes(Y\otimes Z) \arrow[r, "\beta_{X,Y\otimes Z}"] & (Y\otimes Z)\otimes X \arrow[dr, "\alpha_{Y,Z,X}"] & \\
(X\otimes Y)\otimes Z \arrow[ur, "\alpha_{X,Y,Z}"] \arrow[dr, "\beta_{X,Y}\otimes1_Z"'] & & & Y\otimes(Z\otimes X) \\
& (Y\otimes X)\otimes Z \arrow[r, "\alpha_{Y,X,Z}"'] & Y\otimes(X\otimes Z) \arrow[ur, "1_Y\otimes\beta_{X,Z}"'] &
```

The second moves a pair past \(Z\); it is an independent requirement for a general braiding:

```tikz-cd
& (X\otimes Y)\otimes Z \arrow[r, "\beta_{X\otimes Y,Z}"] & Z\otimes(X\otimes Y) \arrow[dr, "\alpha^{-1}_{Z,X,Y}"] & \\
X\otimes(Y\otimes Z) \arrow[ur, "\alpha^{-1}_{X,Y,Z}"] \arrow[dr, "1_X\otimes\beta_{Y,Z}"'] & & & (Z\otimes X)\otimes Y \\
& X\otimes(Z\otimes Y) \arrow[r, "\alpha^{-1}_{X,Z,Y}"'] & (X\otimes Z)\otimes Y \arrow[ur, "\beta_{X,Z}\otimes1_Y"'] &
```

## Braided versus symmetric

Imposing \(\beta_{Y,X}\beta_{X,Y}=1\) gives a [[algebra-category-theory/symmetric-monoidal-category|symmetric monoidal category]]. A [[algebra-category-theory/fusion-category|fusion category]] need not have any braiding.

For an explicit nonsymmetric braiding, take finite-dimensional \(\mathbb Z\)-graded vector spaces over \(k\), choose \(q\in k^\times\) with \(q^2\ne1\), and put \(\beta(v_m\otimes w_n)=q^{mn}w_n\otimes v_m\). The hexagons reduce to \(q^{m(n+p)}=q^{mn}q^{mp}\) and its analogue in the first variable. Two exchanges on degree-one vectors multiply by \(q^2\), so this braiding is not symmetric.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), Definitions 8.1.1–8.1.2 and §8.2; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
