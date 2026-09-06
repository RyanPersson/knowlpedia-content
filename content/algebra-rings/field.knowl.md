+++
id = "algebra-rings/field"
title = "Field"
kind = "knowl"
summary = "A commutative unital ring in which every nonzero element is invertible."
aliases = ["field"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/field.md"
prerequisites = ["algebra-rings/commutative-ring", "algebra-rings/unit"]
dependency_heuristic = "semantic-foundations-review-v1"
dependency_review_count = 1
+++

A **field** is a [[algebra-rings/commutative-ring|commutative ring]] that is also [[algebra-rings/unital-ring|unital]], with \(1\neq 0\), such that every nonzero element is a [[algebra-rings/unit|unit]] (equivalently, every \(a\neq 0\) has a multiplicative inverse).

## Convention

Thus, under the convention used here that a ring need not have a multiplicative identity, the unital condition is part of the definition of a field.

## Remarks

For a commutative unital ring \(R\) with \(1\neq 0\), the following are
equivalent: \(R\) is a field; its only [[algebra-rings/ideal|ideals]] are
\((0)\) and \(R\); and \((0)\) is [[algebra-rings/maximal-ideal|maximal]].
The hypotheses matter: a nonunital ring can have only two ideals without
being a field.

## Examples

- \(\mathbb{Q}\) and \(\mathbb{R}\) are fields.
- For a prime \(p\), \(\mathbb{F}_p=\mathbb{Z}/p\mathbb{Z}\) is a field.
- \(\mathbb{Z}\) is not a field since \(2\) has no inverse in \(\mathbb{Z}\).
