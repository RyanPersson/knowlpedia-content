+++
id = "lie-groups/special-unitary-lie-algebra"
title = "Special unitary Lie algebra"
kind = "knowl"
summary = "The Lie algebra of SU(n): traceless skew-Hermitian matrices with the commutator bracket."
aliases = ["special-unitary-lie-algebra", "Special unitary Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/special-unitary-lie-algebra.md"
+++

The **special unitary Lie algebra** \(\mathfrak{su}(n)\) is the real Lie algebra of the [[lie-groups/special-unitary-group|special unitary group]] \(SU(n)\). Concretely,
\[
\mathfrak{su}(n)=\{X\in M_n(\mathbb C)\mid X^\ast+X=0,\ \mathrm{tr}(X)=0\},
\]

where \(X^\ast=\overline{X}^{\,T}\) is the Hermitian adjoint. The Lie bracket is
\[
[X,Y]=XY-YX.
\]

## Basic structure and context
- As a real vector space, \(\dim_\mathbb{R}\mathfrak{su}(n)=n^2-1\).
- Its center is trivial. In particular, for \(n\ge2\), \(\mathfrak{su}(n)\) is a real [[lie-groups/simple-lie-algebra|simple Lie algebra]].
- The inclusion \(\mathfrak{su}(n)\subset\mathfrak{gl}(n,\mathbb C)\) is the differential at the identity of \(SU(n)\subset GL(n,\mathbb C)\).

\(\mathfrak{su}(n)\) is the compact real form of \(\mathfrak{sl}(n,\mathbb C)\), and its representation theory is a cornerstone of highest-weight methods.

## Equivalent characterizations
Equivalently, \(\mathfrak{su}(n)\) is the trace-zero, codimension-one ideal in the [[lie-groups/unitary-lie-algebra|unitary Lie algebra]] \(\mathfrak u(n)\).
