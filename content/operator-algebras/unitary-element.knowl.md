+++
id = "operator-algebras/unitary-element"
title = "Unitary element of a C*-algebra"
kind = "definition"
summary = "An element of a unital C*-algebra whose adjoint is its two-sided inverse."
aliases = ["C*-unitary", "unitary multiplier"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "linear-algebra/hilbert-space", "operator-algebras/multiplier-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\) be a unital
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A **unitary element** is an
element \(u\in A\) satisfying
\[
u^*u=uu^*=1_A.
\]
Equivalently, \(u\) is invertible and \(u^{-1}=u^*\). If \(A\) is faithfully
represented on a [[linear-algebra/hilbert-space|Hilbert space]], \(u\) acts as a surjective inner-product
preserving operator. For a nonunital \(C^*\)-algebra there are no literal
unitaries in this sense because \(1_A\) is absent; one must specify unitaries
in a unitization or in the
[[operator-algebras/multiplier-algebra|multiplier algebra]] instead.

## Basic properties

Every unitary has norm one unless the algebra is the zero algebra, and its
spectrum is contained in the unit circle. Products and adjoints of unitaries
are unitary. If \(h=h^*\), [[operator-algebras/continuous-functional-calculus|continuous functional calculus]] gives the unitary
\(e^{ih}\). Conversely, a unitary need not admit a logarithm in the algebra;
the obstruction is related to its homotopy class.

## Stable homotopy and K-theory

Unitary elements in the matrix algebras \(M_n(A)\) form groups under
multiplication. After stabilization and homotopy, they define
[[operator-algebras/k1-cstar-algebra|\(K_1(A)\)]]. For nonunital \(A\), one
uses unitaries in matrices over the unitization whose image in the scalar
quotient is the identity. Thus a \(K_1\)-representative is often written
\(1+a\), but only when that element is actually unitary.

## Multiplier convention

A **unitary multiplier** of a nonunital algebra \(A\) means a unitary element
of \(M(A)\), the unital multiplier algebra. It need not belong to \(A\).
[[operator-algebras/nondegenerate-star-homomorphism|Nondegenerate representations]] of \(A\) extend uniquely to \(M(A)\), so
unitary multipliers act naturally in representation theory. The phrases
“unitary of \(A\)” and “unitary multiplier of \(A\)” are therefore not
interchangeable without stating the ambient algebra.

## References

1. Bruce Blackadar, *K-Theory for Operator Algebras*, 2nd ed., Cambridge University Press, 1998. [Publisher record](https://doi.org/10.1017/9781009701907). Relevant: Chapter IV, especially §8, on stable unitary groups and \(K_1\).
2. Gerard J. Murphy, \(C^*\)-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §§2.1–2.2 on unital \(C^*\)-algebras, spectra, and functional calculus.
