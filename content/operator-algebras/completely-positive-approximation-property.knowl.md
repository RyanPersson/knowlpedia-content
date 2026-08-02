+++
id = "operator-algebras/completely-positive-approximation-property"
title = "Completely positive approximation property"
kind = "definition"
summary = "Approximation of the identity map of a C*-algebra in point-norm by completely positive contractions factoring through matrix algebras."
aliases = ["CPAP", "Choi-Effros approximation property"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

A [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\) has the
**completely positive approximation property** (**CPAP**) if there are
positive integers \(n(\lambda)\) and [[operator-algebras/completely-positive-map|
completely positive]] contractions
\[
A\xrightarrow{\ \phi_\lambda\ }M_{n(\lambda)}(\mathbb C)
\xrightarrow{\ \psi_\lambda\ }A
\]
such that
\(\|\psi_\lambda\phi_\lambda(a)-a\|\to0\) for every \(a\in A\). The index
\(\lambda\) ranges over a net, so neither separability nor a sequential
approximation is assumed. The convergence is point-norm: it is uniform on
each fixed finite set after choosing a sufficiently advanced approximation,
not uniform on the unit ball.

## Finite-set formulation

Equivalently, for every finite set \(F\subseteq A\) and every
\(\varepsilon>0\), there are an integer \(n\) and completely positive
contractions \(\phi:A\to M_n(\mathbb C)\) and
\(\psi:M_n(\mathbb C)\to A\) such that
\[
\|\psi\phi(a)-a\|<\varepsilon\qquad(a\in F).
\]
The [[operator-algebras/matrix-cstar-algebra|matrix algebra]] may be replaced
by a finite-dimensional \(C^*\)-algebra without changing the property. This
formulation displays the local content: each finite portion of \(A\) is
approximated through finite-dimensional operator-algebraic data while
retaining positivity at every matrix level.

## Equivalence with nuclearity

A \(C^*\)-algebra has CPAP if and only if it is a
[[operator-algebras/nuclear-cstar-algebra|nuclear \(C^*\)-algebra]]. One direction
uses completely positive factorizations to compare tensor norms; the other
extracts finite-dimensional approximations from nuclearity. This equivalence
is why CPAP is often used as the working definition of nuclearity, although
the two knowls emphasize different mechanisms.

## Examples and consequences

For \(M_k(\mathbb C)\), take \(n=k\) and both maps equal to the identity.
Finite direct sums of matrix algebras therefore have CPAP. Approximation by
finite-dimensional subalgebras shows that AF algebras have CPAP, while
commutative \(C^*\)-algebras obtain it from partitions of unity and
finite-dimensional sampling constructions.

Since each composite \(\psi_\lambda\phi_\lambda\) is a finite-rank
contraction, CPAP implies the metric approximation property of the underlying
[[linear-algebra/banach-space|Banach space]]. The converse fails: complete positivity and the
matrix-factorization structure contain information absent from ordinary
finite-rank approximation.

## Conventions and scope

**Warning.** Replacing point-norm convergence by point-ultraweak convergence
produces a von Neumann-algebraic approximation notion related to
semidiscreteness, not CPAP as defined here. Likewise, the completely bounded
approximation property allows finite-rank [[operator-algebras/completely-bounded-map|completely bounded maps]] with a
uniform norm bound; it does not require positive factorizations through
matrix algebras.

Some sources formulate CPAP using finite-rank [[operator-algebras/completely-positive-contraction|completely positive contractions]]
on \(A\) rather than writing the two maps. For nuclearity, the factorized form
above is the standard robust formulation and makes the finite-dimensional
intermediate algebra explicit.

## References

1. Man-Duen Choi and Edward G. Effros, “Nuclear C*-Algebras and the Approximation Property,” *American Journal of Mathematics* 100 (1978), 61–79. [DOI record](https://doi.org/10.2307/2373876). Relevant: completely positive finite-dimensional approximation of nuclear C*-algebras.
2. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/gsm/088). Relevant: §2.3, especially Theorem 2.3.8, on CPAP and nuclearity.
