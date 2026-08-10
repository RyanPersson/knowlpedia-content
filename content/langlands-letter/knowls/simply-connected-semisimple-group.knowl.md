+++
id = "langlands-letter/knowls/simply-connected-semisimple-group"
title = "Simply connected semisimple algebraic group"
kind = "knowl"
summary = "A semisimple algebraic group with no nontrivial central isogeny cover."
aliases = ["simply-connected-semisimple-group", "Simply Connected Semisimple Algebraic Group"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/simply-connected-semisimple-group.md"
section_mode = "progressive"
+++

A connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive algebraic group]] is **semisimple** if its connected
center is trivial, equivalently if it has no positive-dimensional central
torus.

A **central isogeny** \(f:H\to G\) of connected semisimple groups is a
surjective morphism with finite central kernel. The group \(G\) is
**simply connected** in the algebraic sense if every central isogeny
\(H\to G\) is an isomorphism.

## Root-datum criterion

For a maximal torus \(T\subset G\), semisimple \(G\) is simply connected
exactly when

\[
X_*(T)=\mathbb Z\Phi^\vee,
\]

the coroot lattice. Equivalently, its character lattice is the full
[[lie-groups/weight-lattice|weight lattice]].

Every connected semisimple group has a simply connected central cover

\[
G_{\mathrm{sc}}\longrightarrow G.
\]

## Not topological simple connectedness

This is a notion in the category of [[algebraic-geometry-foundations/algebraic-group|algebraic groups]]. Over
\(\mathbb C\), it is closely related to simple connectedness of the
associated [[lie-groups/complex-lie-group|complex Lie group]], but over \(\mathbb R\) or a nonarchimedean
field it should not be defined from the topology of \(G(F)\).

For example, \(\operatorname{SL}_n\) is algebraically simply connected,
whereas \(\operatorname{PGL}_n\) is adjoint and not simply connected.

## Langlands duality

The [[langlands-letter/knowls/langlands-dual-group|Langlands dual]] of a
simply connected semisimple group is adjoint, and the dual of an adjoint
group is simply connected. This is the isogeny-form information carried by
the root datum.

## Relation to the letter

The letter chooses simply connected nonabelian factors so that the root,
weight, and [[langlands-letter/knowls/dual-lattice|dual lattice]] constructions have their clean extremal form.

## References

1. A. Borel, *Linear Algebraic Groups*, second edition, Springer, 1991.
2. Robert Steinberg, *Lectures on Chevalley Groups*, AMS, 2016.
