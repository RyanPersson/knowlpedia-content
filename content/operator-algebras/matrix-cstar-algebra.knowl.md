+++
id = "operator-algebras/matrix-cstar-algebra"
title = "Matrix C*-algebra"
kind = "definition"
summary = "The C-star algebra of square matrices over a C-star algebra with its canonical operator norm."
aliases = ["full matrix algebra", "M_n(C)"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] and let
\(n\geq1\). The **matrix \(C^*\)-algebra** \(M_n(A)\) consists of \(n\times n\)
matrices with entries in \(A\), with matrix addition and multiplication and
involution
\[
(a_{ij})^*=(a_{ji}^*).
\]
Its canonical norm can be obtained by representing \(A\) faithfully on a
[[linear-algebra/hilbert-space|Hilbert space]] \(H\) and taking the [[linear-algebra/operator-norm|operator norm]] of the induced action on
\(H^n\); this norm is independent of the faithful representation. With this
norm, \(M_n(A)\) is a \(C^*\)-algebra. For \(A=\mathbb C\), it is the full
matrix algebra \(M_n(\mathbb C)\).

## Finite-dimensional structure

The algebra \(M_n(\mathbb C)\) is unital, simple, and finite-dimensional. Its
involution is conjugate transpose, its positive elements are the positive
semidefinite matrices, and its norm is the largest singular value. Every
finite-dimensional \(C^*\)-algebra is isomorphic to a finite direct sum of
such full matrix algebras, although that classification is a theorem rather
than part of the definition
[Murphy, §2.1].

## Matrices over a general algebra

The standard [[operator-algebras/hilbert-cstar-module|Hilbert \(A\)-module]]
\(A^n\) identifies \(M_n(A)\) with its algebra of compact module operators.
When \(A\) is unital, these are all adjointable endomorphisms of \(A^n\); for
nonunital \(A\), the adjointable algebra is generally larger. If \(A\) is
unital, the unit of \(M_n(A)\) is
\(\operatorname{diag}(1_A,\ldots,1_A)\); if \(A\) is nonunital, then
\(M_n(A)\) is nonunital. Matrix formation also preserves ideals and quotients:
for a closed [[algebra-rings/two-sided-ideal|two-sided ideal]] \(I\), the kernel of \(M_n(A)\to M_n(A/I)\) is
\(M_n(I)\).

## Amplification and convention

A [[linear-algebra/linear-map|linear map]] \(\phi:A\to B\) has an entrywise amplification
\(\phi_n:M_n(A)\to M_n(B)\). Positivity of all these amplifications defines
complete positivity, so the canonical matrix norms carry information not
visible at level \(n=1\). The phrase “matrix algebra” sometimes means only
\(M_n(\mathbb C)\); writing \(M_n(A)\) is essential when the coefficient
algebra is not the scalars.

## References

1. Gerard J. Murphy, \(C^*\)-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §§2.1–2.2 on matrix examples and finite-dimensional \(C^*\)-algebras.
