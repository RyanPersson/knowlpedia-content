+++
id = "lie-groups/compact-lie-group-structure"
title = "Structure of compact connected Lie groups"
kind = "knowl"
summary = "A compact connected Lie group is a torus times a compact semisimple group modulo a finite central subgroup."
aliases = ["compact-lie-group-structure", "Structure of compact connected Lie groups"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/compact-lie-group", "lie-groups/connected-lie-group", "lie-groups/center-of-a-lie-algebra", "lie-groups/cartans-criterion-semisimplicity"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "lie-groups/compact-lie-group-structure.md"
+++

Let \(G\) be a [[lie-groups/compact-lie-group|compact]], [[lie-groups/connected-lie-group|connected]] Lie group with Lie algebra \(\mathfrak{g}\).

**Theorem (standard structure decomposition).** There exist:
- a torus \(T\) (a compact connected abelian Lie group),
- a simply connected compact semisimple Lie group \(K\),
- and a finite central subgroup \(F\subset T\times K\),

such that
\[
G \cong (T\times K)/F.
\]
On Lie algebras, one has a canonical decomposition
\[
\mathfrak{g} \cong \mathfrak{z}\oplus [\mathfrak{g},\mathfrak{g}],
\]

where \(\mathfrak{z}\) is the [[lie-groups/center-of-a-lie-algebra|center]] of \(\mathfrak{g}\) and \([\mathfrak{g},\mathfrak{g}]\) is semisimple (compare [[lie-groups/cartans-criterion-semisimplicity|Cartan’s semisimplicity criterion]]).

## Remarks

**Context.** The torus factor encodes the abelian part of \(G\) (see [[lie-groups/connected-abelian-lie-group-structure|connected abelian structure]]), while \(K\) encodes the semisimple part. The finite quotient records an overlap between their centers. The universal cover has the form \(\mathbb R^{\dim T}\times K\); its kernel over \(G\) need not be finite because the torus contributes a lattice.

This decomposition is one conceptual reason compact Lie groups have especially rigid representation theory, via [[lie-groups/peter-weyl-theorem|Peter–Weyl]] and highest-weight methods (see [[lie-groups/highest-weight-theorem|the highest weight theorem]]).
