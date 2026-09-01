+++
id = "langlands-letter/knowls/group-algebra-of-lattice"
title = "Group algebra of a lattice"
kind = "knowl"
summary = "The Laurent monomial algebra with basis indexed by a lattice, serving as the coordinate ring of a complex torus."
aliases = ["group-algebra-of-lattice", "Group Algebra of a Lattice and Multiplicative Basis"]
domains = ["langlands-letter"]
prerequisites = ["algebra-groups/abelian-group", "algebra-representation-theory/group-algebra", "algebra-rings/laurent-polynomial-ring"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "langlands-letter/knowls/group-algebra-of-lattice.md"
section_mode = "progressive"
+++

Let \(L\) be a finite free [[algebra-groups/abelian-group|abelian group]].
The **[[algebra-representation-theory/group-algebra|group algebra]]**
\(\mathbb C[L]\) has basis \(\{e^\lambda\}_{\lambda\in L}\) and
multiplication

\[
e^\lambda e^\mu=e^{\lambda+\mu}.
\]

After choosing a basis \(L\simeq\mathbb Z^r\),

\[
\mathbb C[L]
\simeq
\mathbb C[x_1^{\pm1},\ldots,x_r^{\pm1}].
\]

This is a [[algebra-rings/laurent-polynomial-ring|Laurent polynomial ring]].

## Coordinate ring of a torus

If \(T\) is a complex algebraic torus with
[[langlands-letter/knowls/maximal-torus-weight-lattice|character lattice]]
\(X^*(T)=L\), then

\[
\mathcal O(T)=\mathbb C[L].
\]

A point \(t\in T(\mathbb C)\) defines the evaluation character

\[
\mathbb C[L]\longrightarrow\mathbb C,
\qquad
e^\lambda\longmapsto\lambda(t).
\]

Conversely, every complex [[algebra-modules/algebra-homomorphism|algebra homomorphism]] to \(\mathbb C\) arises from
a point of \(T\).

## Weyl invariants

If a [[lie-groups/weyl-group|Weyl group]] \(W\) acts on \(L\), then
\(\mathbb C[L]^W\) is the coordinate ring of the affine quotient \(T/W\).
Its complex points encode
[[langlands-letter/knowls/semisimple-element-and-class|semisimple]]
[[algebra-groups/conjugacy-class|conjugacy classes]] in a connected
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] with maximal torus \(T\).

## Satake role

For a [[langlands-letter/knowls/split-reductive-group|split group]] \(G\),
the [[langlands-letter/knowls/spherical-hecke-algebra-satake|normalized
Satake isomorphism]] identifies the spherical Hecke algebra with

\[
\mathbb C[X_*(T)]^W
=
\mathbb C[X^*(\widehat T)]^W.
\]

The letter describes this using the group algebra of its [[langlands-letter/knowls/dual-lattice|dual lattice]].

## References

1. Ichirō Satake, “Theory of spherical functions on reductive algebraic
   groups over \(p\)-adic fields,” *PMIHÉS* 18 (1963), 5–69.
   [Numdam](https://www.numdam.org/item/PMIHES_1963__18__5_0/).
