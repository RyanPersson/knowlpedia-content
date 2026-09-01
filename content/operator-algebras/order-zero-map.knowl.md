+++
id = "operator-algebras/order-zero-map"
title = "Completely positive order-zero map"
kind = "definition"
summary = "A completely positive map that sends orthogonal positive elements to orthogonal positive elements."
aliases = ["order zero map", "orthogonality-preserving CP map"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/completely-positive-map"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]].
A
[[operator-algebras/completely-positive-map|completely positive map]]
\(\phi:A\to B\) has **order zero** if it preserves orthogonality of positive
elements:
\[
a,b\in A_+,\quad ab=0
\quad\Longrightarrow\quad
\phi(a)\phi(b)=0.
\]
Because positive \(a\) and \(b\) with \(ab=0\) also satisfy \(ba=0\), the
condition is symmetric. Order zero does not mean that \(\phi\) vanishes, has
zero algebraic order, or is multiplicative. Contractivity is not included in
the convention used here; a map that is both contractive and order zero is
called a **CPC order-zero map**.

## Structure theorem

Let \(C=C^*(\phi(A))\). The order-zero structure theorem supplies a positive
element \(h\) in the center of the
[[operator-algebras/multiplier-algebra|multiplier algebra]] \(M(C)\) and a
\(*\)-homomorphism \(\pi_\phi:A\to M(C)\) such that
\[
\phi(a)=\pi_\phi(a)h=h\pi_\phi(a).
\]
For unital \(A\), one can take \(h=\phi(1_A)\). This factorization explains
why order-zero maps retain much of the orthogonality behavior of
\(*\)-homomorphisms without themselves preserving products.

## Cone correspondence

Contractive completely positive order-zero maps \(A\to B\) correspond
naturally to \(*\)-homomorphisms
\[
C_0((0,1])\otimes A\longrightarrow B,
\]
with the coordinate function on \((0,1]\) sent, together with \(a\), to
\(\phi(a)\). This converts a nonlinear-looking orthogonality condition into
ordinary multiplicative data.

## Examples and near-misses

Every \(*\)-homomorphism has order zero, as does a positive scalar multiple
of one. A compression \(a\mapsto V^*aV\) is completely positive but generally
not order zero: two orthogonal positive operators can acquire overlapping
compressions. Thus complete positivity alone does not preserve
orthogonality.

## References

1. Wilhelm Winter and Joachim Zacharias, “Completely positive maps of order zero,” *Münster Journal of Mathematics* 2 (2009), 311–324. [Author-institution record](https://eprints.gla.ac.uk/71562/). Relevant: Definition 2.1, Theorem 2.3, and Corollary 3.1.
