+++
id = "lie-groups/solvable-lie-algebra"
title = "Solvable Lie algebra"
kind = "knowl"
summary = "A Lie algebra whose derived series eventually becomes zero; the Lie-algebra analogue of solvable groups."
aliases = ["solvable-lie-algebra", "Solvable Lie algebra"]
domains = ["lie-groups"]
legacy_source_path = "lie-groups/solvable-lie-algebra.md"
prerequisites = ["lie-groups/lie-algebra", "lie-groups/derived-series-lie-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathfrak g\) be a [[lie-groups/lie-algebra|Lie algebra]]. Define its [[lie-groups/derived-series-lie-algebra|derived series]] by
\[
\mathfrak g^{(0)}=\mathfrak g,\qquad \mathfrak g^{(k+1)}=[\mathfrak g^{(k)},\mathfrak g^{(k)}],
\]
where \([\cdot,\cdot]\) denotes the Lie algebra bracket. Each derived algebra is an ideal.

The Lie algebra \(\mathfrak g\) is **solvable** if there exists \(n\) such that
\[
\mathfrak g^{(n)}=0.
\]
## Structural properties

This notion is central in the structure theory of general Lie algebras: the maximal solvable ideal is the radical, and the [[lie-groups/levi-decomposition-theorem|Levi decomposition]] splits any finite-dimensional Lie algebra (in characteristic \(0\)) into a semisimple part and a solvable part.

There are several important tests and relations:

- Cartan’s criterion gives a practical characterization in many settings (see [[lie-groups/cartans-criterion-solvability|Cartan’s criterion for solvability]] and [[lie-groups/tfae-solvability-lie-algebra|equivalent conditions for solvability]]).
- Every [[lie-groups/nilpotent-lie-algebra|nilpotent Lie algebra]] is solvable (see [[lie-groups/nilpotent-implies-solvable-lemma|nilpotent implies solvable]]), but not conversely.
