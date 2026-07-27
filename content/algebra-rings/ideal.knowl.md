+++
id = "algebra-rings/ideal"
title = "Ideal"
kind = "knowl"
summary = "A left, right, or two-sided additive subgroup stable under the corresponding multiplication by ring elements."
aliases = ["ideal"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/ideal.md"
+++

Let \(R\) be a [[algebra-rings/ring|ring]] and \(I\le (R,+)\) an additive subgroup. Then \(I\) is a **left ideal** if \(rI\subseteq I\) for every \(r\in R\), a **right ideal** if \(Ir\subseteq I\) for every \(r\in R\), and a **two-sided ideal** if both conditions hold.

## Remarks

Two-sided ideals are exactly the kernels of ring homomorphisms and are the ideals for which the [[algebra-rings/quotient-ring|quotient ring]] \(R/I\) is defined. In commutative rings the three notions coincide.

## Examples

- In \(\mathbb Z\), every ideal has the form \(n\mathbb Z\) for some \(n\ge 0\).
- In \(k[x,y]\), the set \((x,y)\) of polynomials with zero constant term is an ideal.
- In \(M_2(k)\), the set of matrices whose second column is zero is a left ideal but not a right ideal.
