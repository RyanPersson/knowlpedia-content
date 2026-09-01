+++
id = "operator-algebras/type-i-factor"
title = "Type I factor"
kind = "definition"
summary = "A von Neumann factor containing a nonzero abelian projection."
aliases = ["type I von Neumann factor"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/von-neumann-factor", "operator-algebras/type-i-von-neumann-algebra", "operator-algebras/abelian-projection", "linear-algebra/hilbert-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **type I factor** is a [[operator-algebras/von-neumann-factor|von Neumann
factor]] \(M\) that is also a
[[operator-algebras/type-i-von-neumann-algebra|type I von Neumann algebra]].
Equivalently, \(M\) contains a nonzero
[[operator-algebras/abelian-projection|abelian projection]] \(p\), meaning that
the corner \(pMp\) is abelian. Factoriality makes the central support of every
nonzero projection equal to \(1_M\), so one such projection detects type I.
This definition is representation-independent. The classification theorem
states that there is a [[linear-algebra/hilbert-space|Hilbert space]] \(K\),
unique up to Hilbert-space dimension, for which \(M\) is isomorphic as a von
Neumann algebra to \(B(K)\).

## Classification by dimension

Choose a maximal family of mutually orthogonal equivalent
[[operator-algebras/minimal-projection|minimal projections]]. Matrix units
constructed between them identify the factor with all bounded operators on a
Hilbert space. Consequently the isomorphism class of a type I factor is
determined by the cardinal dimension of that Hilbert space.

When \(\dim K=n<\infty\), the factor is \(M_n(\mathbb C)\) and is called type
\(\mathrm{I}_n\). When \(K\) is infinite-dimensional, \(B(K)\) is often
denoted type \(\mathrm{I}_\infty\).

## Examples and consequences

The algebra \(\mathbb C=B(\mathbb C)\) is the type \(\mathrm{I}_1\) factor.
Every [[operator-algebras/matrix-cstar-algebra|full matrix algebra]] is a type
I factor. The algebra \(B(\ell^2)\) is an [[operator-algebras/type-i-infinity-factor|infinite type I factor]]: it contains
rank-one abelian projections, although its identity is infinite.

An abelian [[operator-algebras/von-neumann-algebra|von Neumann algebra]] with more than one point in its spectrum is type
I but is not a factor, because its center is larger than the scalars. A type
\(\mathrm{II}\) or type \(\mathrm{III}\) factor has no nonzero abelian
projection and hence is not type I.

## Conventions and scope

**Warning.** “Type I factor,” “type I von Neumann algebra,” and “type I
\(C^*\)-algebra” are different levels of structure. A general type I von
Neumann algebra may have nontrivial center and need not be isomorphic to a
single \(B(K)\).

## References

1. M. Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V, §1 on the classification of type I factors.
2. R. V. Kadison and J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. II, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/016). Relevant: §6.5 on factor types.
