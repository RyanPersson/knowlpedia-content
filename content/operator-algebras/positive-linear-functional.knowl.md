+++
id = "operator-algebras/positive-linear-functional"
title = "Positive linear functional"
kind = "definition"
summary = "A complex linear functional on a C*-algebra that is nonnegative on every positive element."
aliases = ["positive functional", "positive form on a C*-algebra"]
domains = ["operator-algebras", "functional-analysis"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/positive-cone"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A **positive linear functional** is a complex-linear map \(\varphi:A\to\mathbb C\) such that
\[
\varphi(a)\geq0\qquad(a\in A_+),
\]
where \(A_+\) is the [[operator-algebras/positive-cone|positive cone]]. Equivalently, \(\varphi(b^*b)\geq0\) for every \(b\in A\). These inequalities force \(\varphi(a^*)=\overline{\varphi(a)}\), and a positive functional is automatically bounded. If \(A\) is unital, then
\[
\lVert\varphi\rVert=\varphi(1).
\]
A state is a positive functional of norm one, an additional normalization rather than part of positivity.

## Cauchy–Schwarz inequality

Positivity of the quadratic form \(a\mapsto\varphi(a^*a)\) yields
\[
|\varphi(b^*a)|^2\leq\varphi(a^*a)\varphi(b^*b).
\]
This inequality controls continuity and identifies the null space used in the [[operator-algebras/gns-construction|GNS construction]]. In the unital case, a bounded functional \(\varphi\) is positive exactly when \(\lVert\varphi\rVert=\varphi(1)\); the equality includes the assertion that \(\varphi(1)\) is real and nonnegative.

## Example: integration

For a compact Hausdorff space \(X\), integration against a finite positive
Borel measure \(\mu\) gives a positive functional on \(C(X)\):
\(\varphi(f)=\int_X f\,d\mu\). Point evaluation is the special case
\(\mu=\delta_{x_0}\); its one-dimensional GNS representation is worked out
in the [[operator-algebras/gns-construction|GNS construction]].

## GNS construction

The form \(\langle a,b\rangle_\varphi=\varphi(b^*a)\) is positive semidefinite. Quotienting \(A\) by its null left ideal and completing gives a Hilbert space \(H_\varphi\). Left multiplication descends to a \(*\)-representation \(\pi_\varphi:A\to B(H_\varphi)\), with a [[operator-algebras/cyclic-vector|cyclic vector]] when \(A\) is unital, such that
\[
\varphi(a)=\langle\pi_\varphi(a)\xi_\varphi,\xi_\varphi\rangle.
\]
Thus positive functionals are exactly the scalar matrix coefficients arising from cyclic representations in this way.

## Nearby notions

A positive functional need not be tracial, multiplicative, faithful, or normalized. A character of a unital \(C^*\)-algebra is positive because it is a nonzero \(*\)-homomorphism to \(\mathbb C\), but most positive functionals are not characters. On a [[operator-algebras/von-neumann-algebra|von Neumann algebra]], normality is a further continuity condition; positivity alone does not imply it.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [Elsevier DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §3.2 on positive functionals and the GNS construction.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [Elsevier DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §3.3 on positive forms and representations.
