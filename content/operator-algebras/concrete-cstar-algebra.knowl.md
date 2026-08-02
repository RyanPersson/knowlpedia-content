+++
id = "operator-algebras/concrete-cstar-algebra"
title = "Concrete C*-algebra"
kind = "definition"
summary = "A norm-closed operator algebra on a Hilbert space that is closed under adjoints."
aliases = ["operator C*-algebra", "norm-closed *-algebra of operators"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(\mathcal H\) be a complex
[[linear-algebra/hilbert-space|Hilbert space]]. A **concrete
\(C^*\)-algebra** on \(\mathcal H\) is a norm-closed subalgebra
\(A\subseteq B(\mathcal H)\) of the
[[operator-algebras/bounded-operator-cstar-algebra|bounded operators]] that is
closed under operator adjoints. With the inherited
[[linear-algebra/operator-norm|operator norm]] and involution, \(A\) is a
[[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. The definition does not
require \(A\) to contain the identity operator unless “unital concrete
\(C^*\)-algebra” is explicitly stated.

## Relation to abstract \(C^*\)-algebras

The Gelfand--Naimark representation theorem says that every abstract
\(C^*\)-algebra admits an isometric \(*\)-isomorphism onto a concrete
\(C^*\)-algebra.
Thus the abstract axioms capture exactly the norm-closed adjoint-stable
operator algebras, although a given abstract algebra can have many inequivalent
realizations on Hilbert spaces. “Concrete” records a chosen faithful operator
realization, not an additional algebraic axiom.

## Degeneracy and units

The action of \(A\) on \(\mathcal H\) is nondegenerate when
\(\overline{A\mathcal H}=\mathcal H\). A unital abstract algebra can be
represented degenerately with its unit acting as a proper projection rather
than as \(I_{\mathcal H}\); a unital representation convention rules this
out. Likewise, a concrete algebra may possess an identity that is a projection
onto \(\overline{A\mathcal H}\) even when it does not contain the ambient
identity operator.

## Examples and non-examples

The algebras \(B(\mathcal H)\) and
[[operator-algebras/compact-operator-cstar-algebra|\(K(\mathcal H)\)]] are
concrete \(C^*\)-algebras. Multiplication operators by functions in
\(C_0(X)\) give commutative concrete models on suitable \(L^2\)-spaces. The
upper-triangular matrices are norm closed but not adjoint closed, so they are
an operator algebra but not a concrete \(C^*\)-algebra.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1 and Theorem 3.4.1 on concrete algebras and faithful representations.
2. Gert K. Pedersen, *\(C^*\)-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: Chapters 1 and 3 on abstract \(C^*\)-algebras and representations.
