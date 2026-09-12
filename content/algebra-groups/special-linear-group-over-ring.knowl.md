+++
id = "algebra-groups/special-linear-group-over-ring"
title = "Special linear group over a ring"
kind = "definition"
summary = "The group of determinant-one matrices over a commutative ring."
aliases = ["SL over a commutative ring"]
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-rings/commutative-ring", "linear-algebra/matrix", "linear-algebra/determinant"]
+++

For a nonzero [[algebra-rings/commutative-ring|commutative ring]] \(R\) with identity and \(n\ge2\), the **special linear group over \(R\)** is
\[
\operatorname{SL}_n(R)=\{A\in M_n(R):\det A=1\}
\]
under matrix multiplication. Here \(M_n(R)\) denotes the \(n\)-by-\(n\) matrices with entries in \(R\), and the determinant is given by its usual signed-permutation polynomial.

## Why it is a group

The determinant is multiplicative, and \(A^{-1}=\operatorname{adj}(A)\) when \(\det A=1\). The adjugate still has entries in \(R\), so inversion stays in the set.

## Rank two

An element is \(\begin{pmatrix}a&b\\c&d\end{pmatrix}\) with \(ad-bc=1\); its inverse is \(\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\). For \(R=\mathbb R\) or \(\mathbb C\), the [[lie-groups/special-linear-group|Lie-group version]] supplies the topology and smooth structure. No Lie-group structure is part of the ring-valued definition.
