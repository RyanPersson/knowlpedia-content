+++
id = "noncommutative-geometry/hochschild-cycle"
title = "Hochschild cycle"
kind = "definition"
summary = "A Hochschild chain annihilated by the Hochschild boundary."
aliases = ["Hochschild homology cycle", "b-cycle"]
domains = ["noncommutative-geometry", "algebra-homological"]
prerequisites = ["algebra-modules/algebra-over-ring", "noncommutative-geometry/hochschild-chain-complex", "algebra-homological/homology-module"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be a unital [[algebra-modules/algebra-over-ring|algebra over a commutative ring]] \(k\), let \(M\) be an \(A\)-bimodule, and let
\[
\bigl(C_\bullet(A,M),b\bigr)
\]
be the [[noncommutative-geometry/hochschild-chain-complex|Hochschild chain complex]]. A **Hochschild \(n\)-cycle** is an element \(c\in C_n(A,M)\) satisfying \(b(c)=0\). The module of such cycles is
\[
Z_n(A,M)=\ker\!\left(b:C_n(A,M)\to C_{n-1}(A,M)\right).
\]
A cycle determines a class \([c]\) in the [[algebra-homological/homology-module|Hochschild homology module]]
\[
HH_n(A,M)=Z_n(A,M)/bC_{n+1}(A,M).
\]
Accordingly, a cycle is a representative chain, not the homology class itself; two cycles represent the same class exactly when their difference is a Hochschild boundary.

## Low-degree examples

Every zero-chain is a zero-cycle because the boundary out of degree zero
vanishes. When \(M=A\), a one-chain \(a_0\otimes a_1\) has boundary
\[
b(a_0\otimes a_1)=a_0a_1-a_1a_0.
\]
It is therefore a cycle precisely when \(a_0\) and \(a_1\) commute. Sums of
one-chains can be cycles even when their individual summands are not.

## Orientation in spectral geometry

The orientation axiom for a [[noncommutative-geometry/spectral-triple|spectral triple]] uses a Hochschild cycle with
coefficients in a bimodule involving the [[operator-algebras/opposite-algebra|opposite algebra]]. Its represented
image under
\[
a_0\otimes\cdots\otimes a_n
\longmapsto a_0[D,a_1]\cdots[D,a_n]
\]
is required to recover the grading in the even case, or the identity in the
odd case, subject to the selected convention. This is extra geometric data,
not a property of every Hochschild cycle.

## Conventions and scope

**Warning.** A cyclic cycle, a cyclic cocycle, and a Hochschild cycle are
different notions. Topological algebras may require completed tensor products
and continuous chains. In nonunital settings one must also choose reduced,
normalized, or unitized complexes before the cycle condition is fully
specified.

## References

1. J.-L. Loday, *Cyclic Homology*, 2nd ed., Springer, 1998. [Publisher record](https://doi.org/10.1007/978-3-662-11389-9). Relevant: §1.1 on Hochschild chains, cycles, boundaries, and homology.
2. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-maintained text](https://www.alainconnes.org/docs/book94bigpdf.pdf). Relevant: chapters III and VI on Hochschild homology and the orientation axiom.
