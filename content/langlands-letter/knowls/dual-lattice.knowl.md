+++
id = "langlands-letter/knowls/dual-lattice"
title = "Dual lattice"
kind = "knowl"
summary = "The integral dual Hom(L,Z) of a finite free abelian group and its role in dual root data."
aliases = ["dual-lattice", "Dual Lattice"]
domains = ["langlands-letter"]
prerequisites = ["algebra-groups/abelian-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 1
legacy_source_path = "langlands-letter/knowls/dual-lattice.md"
section_mode = "progressive"
+++

A **lattice** is a finite free [[algebra-groups/abelian-group|abelian group]] \(L\simeq\mathbb Z^r\). Its
**integral dual lattice** is

\[
L^\vee=\operatorname{Hom}_{\mathbb Z}(L,\mathbb Z).
\]

Evaluation gives a perfect pairing

\[
L\times L^\vee\longrightarrow\mathbb Z.
\]

The bidual map \(L\to L^{\vee\vee}\) is an isomorphism.

## Torus lattices

For the [[langlands-letter/knowls/maximal-torus-weight-lattice|character and
cocharacter lattices]] of an algebraic torus \(T\),

\[
X_*(T)\simeq X^*(T)^\vee.
\]

If \(T\) is defined over a nonsplit field, both lattices carry an
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois-group
action]] and the evaluation pairing is Galois-equivariant.

The coordinate ring of a complex torus with character lattice \(L\) is the
[[algebra-representation-theory/group-algebra|group algebra]]
\(\mathbb C[L]\). Thus passing to a dual torus exchanges its
character and cocharacter lattices.

## Distinctions

The integral dual \(L^\vee\) is not the same object as:

- the real or complex linear dual of \(L\otimes\mathbb R\);
- the [[harmonic-analysis/pontryagin-dual|Pontryagin dual]] of \(L\) as a discrete [[topology/topological-group|topological group]];
- the discriminant dual of a lattice equipped with a [[linear-algebra/bilinear-form|bilinear form]].

These constructions can be related after extra choices but should not be
identified by notation alone.

## Relation to the letter

The letter's “conjugate lattice” \(cL\) participates in the root datum of
the [[langlands-letter/knowls/langlands-dual-group|Langlands dual group]].
Modern notation records both character and cocharacter lattices explicitly,
which avoids hiding the isogeny form.

## References

1. T. A. Springer, *Linear Algebraic Groups*, second edition, Birkhäuser,
   1998.
