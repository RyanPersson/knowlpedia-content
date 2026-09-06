+++
id = "lie-groups/derived-series-lie-algebra"
title = "Derived series of a Lie algebra"
kind = "knowl"
summary = "The descending sequence obtained by repeatedly taking derived subalgebras."
aliases = ["derived-series-lie-algebra", "Derived series of a Lie algebra"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/lie-algebra", "lie-groups/derived-subalgebra", "lie-groups/ideal-lie-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "lie-groups/derived-series-lie-algebra.md"
+++

Let \(\mathfrak g\) be a [[lie-groups/lie-algebra|Lie algebra]]. Its **derived series** is the descending sequence
\[
\mathfrak g^{(0)} := \mathfrak g,\qquad
\mathfrak g^{(k+1)} := [\mathfrak g^{(k)},\,\mathfrak g^{(k)}]
\]
for \(k\ge 0\), where the bracket denotes the [[lie-groups/derived-subalgebra|derived subalgebra]] of \(\mathfrak g^{(k)}\).

Each \(\mathfrak g^{(k)}\) is a characteristic [[lie-groups/ideal-lie-algebra|ideal]] of \(\mathfrak g\).

## Solvability
A Lie algebra is **solvable** if \(\mathfrak g^{(r)}=0\) for some \(r\ge 0\); the least such \(r\) is its **derived length**. See [[lie-groups/solvable-lie-algebra|solvable Lie algebra]].

## Relation to groups
For a connected Lie group \(G\) with Lie algebra \(\mathfrak g\), this is the infinitesimal analogue of repeatedly taking the [[lie-groups/commutator-subgroup-of-a-lie-group|commutator subgroup]].
