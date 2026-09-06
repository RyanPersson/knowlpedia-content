+++
id = "operator-algebras/k0-cstar-algebra"
title = "K_0 of a C*-algebra"
kind = "definition"
summary = "The Grothendieck group built from stable equivalence classes of projections over a C*-algebra."
aliases = ["operator K-zero", "projection K-theory", "even K-theory"]
domains = ["operator-algebras", "k-theory"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/murray-von-neumann-equivalence", "operator-algebras/projection-cstar-algebra", "operator-algebras/unitization"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a unital [[operator-algebras/cstar-algebra|\(C^*\)-algebra]].
Form the commutative monoid \(V(A)\) of
[[operator-algebras/murray-von-neumann-equivalence|Murray–von Neumann
equivalence]] classes of
[[operator-algebras/projection-cstar-algebra|projections]] in
\(M_\infty(A)=\bigcup_n M_n(A)\), with addition induced by block sum. The group
\(K_0(A)\) is the Grothendieck group of \(V(A)\). Thus its elements are formal
differences \([p]-[q]\), modulo stabilization and projection equivalence. If
\(A\) is nonunital, define
\[
K_0(A)=\ker\bigl(K_0(\widetilde A)\to K_0(\mathbb C)\bigr),
\]
where \(\widetilde A\) is the
[[operator-algebras/unitization|unitization]] and the map comes from the scalar
quotient.

## Representative calculus

Two formal differences represent the same class precisely after adding
suitable auxiliary projections and passing to Murray–von Neumann equivalence.
A \(*\)-homomorphism \(f:A\to B\) sends a projection \(p\) to its matrix
amplification \(f^{(n)}(p)\), inducing a homomorphism
\(K_0(f):K_0(A)\to K_0(B)\).

## Basic properties

The functor \(K_0\) is invariant under homotopy, matrix stabilization, and
strong Morita equivalence. For the [[linear-algebra/compact-operator|compact operators]] \(\mathcal K(H)\) on an
infinite-dimensional separable [[linear-algebra/hilbert-space|Hilbert space]], finite-rank projections give
\[
K_0(\mathcal K(H))\cong\mathbb Z.
\]
For a unital algebra, \(K_0(A)\) also carries a positive cone and the
distinguished order-unit class \([1_A]\), data often used in classification.

## Conventions and scope

Some authors begin with stable homotopy classes of projections rather than
Murray–von Neumann classes; the resulting group is canonically isomorphic.
The symbol \(K_0\) here denotes operator \(K\)-theory of complex
\(C^*\)-algebras. It is not algebraic \(K_0\), although the two constructions
share the Grothendieck-group pattern.

## References

1. Bruce Blackadar, *K-Theory for Operator Algebras*, 2nd ed., Cambridge University Press, 1998. [DOI record](https://doi.org/10.1017/9781009701907). Relevant: Chapter III on \(K_0\), order, and projection representatives.
2. N. E. Wegge-Olsen, *K-Theory and C*-Algebras: A Friendly Approach*, Oxford University Press, 1993. [DOI record](https://doi.org/10.1093/oso/9780198596943.001.0001). Relevant: Chapters 5–6 on projections and \(K_0\).
