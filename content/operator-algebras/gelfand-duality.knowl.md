+++
id = "operator-algebras/gelfand-duality"
title = "Gelfand duality"
kind = "theorem"
summary = "A contravariant equivalence between locally compact Hausdorff spaces and commutative C-star algebras."
aliases = ["commutative Gelfand–Naimark theorem", "Gelfand representation theorem", "Gelfand duality theorem"]
domains = ["operator-algebras", "topology", "algebra-category-theory"]
prerequisites = ["operator-algebras/commutative-cstar-algebra", "operator-algebras/character-space", "operator-algebras/gelfand-transform", "topology/locally-compact-space", "topology/hausdorff-space", "topology/continuous-map", "operator-algebras/nondegenerate-star-homomorphism"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[operator-algebras/commutative-cstar-algebra|commutative \(C^*\)-algebra]] \(A\), let \(\Delta(A)\) be its
[[operator-algebras/character-space|character space]]. **Gelfand duality**
asserts that the [[operator-algebras/gelfand-transform|Gelfand transform]]
\[
A\longrightarrow C_0(\Delta(A)),\qquad a\longmapsto
(\chi\mapsto\chi(a)),
\]
is an isometric \(*\)-isomorphism, while
evaluation gives a homeomorphism \(X\cong\Delta(C_0(X))\) for every
[[topology/locally-compact-space|locally compact]]
[[topology/hausdorff-space|Hausdorff space]] \(X\). Moreover, a proper
[[topology/continuous-map|continuous map]] \(f:X\to Y\) corresponds contravariantly to the
[[operator-algebras/nondegenerate-star-homomorphism|nondegenerate \(*\)-homomorphism]] \(f^*:C_0(Y)\to C_0(X)\), \(h\mapsto h\circ f\).

## Categorical content

The assignments \(X\mapsto C_0(X)\) and \(A\mapsto\Delta(A)\) define
[[algebra-category-theory/contravariant-functor|contravariant functors]]. The two displayed canonical maps are natural
isomorphisms, so the result is an
[[algebra-category-theory/equivalence-of-categories|equivalence of categories]], not merely a classification of objects. Every nondegenerate
\(*\)-homomorphism between commutative \(C^*\)-algebras arises uniquely as
pullback along the corresponding proper continuous map.

## Compact form and examples

Restricting to compact Hausdorff spaces gives the equivalent unital form:
\(X\mapsto C(X)\) is dual to the category of unital commutative
\(C^*\)-algebras and unital \(*\)-homomorphisms. For example,
\(\Delta(C_0(\mathbb R))\) consists exactly of point evaluations and is
homeomorphic to \(\mathbb R\). More generally, the theorem recovers both the
points and topology of \(X\) from
[[operator-algebras/c0-function-algebra|\(C_0(X)\)]].

## Conventions and scope

**Warning.** Allowing all continuous maps between locally compact spaces
requires multiplier-algebra-valued morphisms instead; the proper-map
convention in the core keeps pullbacks inside \(C_0(X)\). Gelfand duality is
also distinct from the general Gelfand–Naimark representation theorem:
the latter represents an arbitrary, possibly noncommutative,
\(C^*\)-algebra by operators on a [[linear-algebra/hilbert-space|Hilbert space]] rather than by scalar-valued
functions on a character space.

## References

1. Gerard J. Murphy, *\(C^*\)-Algebras and Operator Theory*, Academic Press, 1990. [Publisher record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: Theorem 2.1.10, the commutative Gelfand representation theorem.
