+++
id = "operator-algebras/cstar-algebra"
title = "C*-algebra"
kind = "definition"
summary = "A Banach *-algebra whose norm and involution satisfy the C*-identity."
aliases = []
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/involutive-algebra", "functional-analysis/banach-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **\(C^*\)-algebra** is a complex [[operator-algebras/involutive-algebra|involutive algebra]] \(A\) that is a [[functional-analysis/banach-algebra|Banach algebra]] and whose norm satisfies the **\(C^*\)-identity**
\[
\lVert a^*a\rVert=\lVert a\rVert^2
\qquad (a\in A).
\]
The definition does not require \(A\) to have an identity element. In every nonzero unital \(C^*\)-algebra, the \(C^*\)-identity forces \(\lVert 1_A\rVert=1\). Morphisms in the standard category are [[operator-algebras/star-homomorphism|*-homomorphism]]s, often with continuity left unstated because every *-homomorphism between \(C^*\)-algebras is automatically contractive. An [[operator-algebras/faithful-star-homomorphism|injective *-homomorphism]] is isometric.

## Abstract and concrete forms

For a concrete example, \(M_n(\mathbb C)\) uses the operator norm and the
conjugate-transpose involution. The identity becomes
\(\|A^*A\|=\|A\|^2\), the finite-dimensional model for the abstract axiom.

A concrete \(C^*\)-algebra is a norm-closed self-adjoint subalgebra of \(B(H)\) for a complex Hilbert space \(H\). The Gelfand–Naimark representation theorem says that every abstract \(C^*\)-algebra admits an isometric *-representation of this form. Thus the abstract axioms capture exactly the operator-norm structure of closed operator algebras, without choosing a preferred [[linear-algebra/hilbert-space|Hilbert space]] representation.

## Consequences of the identity

The \(C^*\)-identity forces the involution to be isometric:
\[
\lVert a^*\rVert=\lVert a\rVert.
\]
It also ties the norm to spectral theory; for example, \(\lVert a\rVert^2\) is the spectral radius of the positive element \(a^*a\). This rigidity distinguishes \(C^*\)-algebras from general Banach *-algebras, where the algebra norm and involution can carry substantially less spectral information.

## Examples and conventions

The scalar field \(\mathbb C\), matrix algebras \(M_n(\mathbb C)\), \(B(H)\), and \(C_0(X)\) for a locally compact [[topology/hausdorff-space|Hausdorff space]] \(X\) are \(C^*\)-algebras. The algebra \(C_0(X)\) is unital exactly when \(X\) is compact. Real \(C^*\)-algebras also form a useful theory, but “\(C^*\)-algebra” without a qualifier normally means a complex one.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [Elsevier DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1, defining paragraph and equation (1), and Theorem 3.4.1.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., edited by Søren Eilers and Dorte Olesen, Academic Press, 2018. [Elsevier DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.1.
