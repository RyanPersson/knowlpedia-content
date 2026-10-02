+++
id = "catalog/relationships/magic-square-transposition"
title = "Transposition symmetry of the magic square"
kind = "theorem"
summary = "Swapping the two input composition algebras gives isomorphic magic-square Lie algebras."
aliases = ["Transposition symmetry of the magic square"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/relationships/vinberg-magic-square-construction", "lie-groups/lie-algebra-isomorphism"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

For real composition algebras \(A,B\), exchanging the two derivation factors and applying \(a\otimes b\mapsto b\otimes a\) entrywise gives a [[lie-groups/lie-algebra-isomorphism|Lie algebra isomorphism]]
\[
\mathfrak M(A,B)\cong\mathfrak M(B,A)
\]
in the [[catalog/relationships/vinberg-magic-square-construction|Vinberg construction]]. Consequently the [[catalog/relationships/compact-freudenthal-magic-square|compact magic square]] is symmetric across its diagonal.

## Verification

The tensor flip preserves multiplication, conjugation and matrix trace. It exchanges the two terms in the tensor derivation correction. It therefore preserves each of the three bracket rules, and applying it twice gives the identity.

## What the symmetry identifies

The ordered inputs remain distinct catalogue data. For example, the constructions from \((\mathbb R,\mathbb O)\) and \((\mathbb O,\mathbb R)\) both yield compact \(\mathfrak f_4\). This identifies their constructed Lie algebras; it does not assert an algebra isomorphism \(\mathbb R\cong\mathbb O\).

## References

1. C. H. Barton and A. Sudbery, “Magic squares and matrix models of Lie algebras,” §4.2, equation (4.19) and Theorem 4.3. [Paper](https://arxiv.org/pdf/math/0203010).
