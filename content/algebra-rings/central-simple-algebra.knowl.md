+++
id = "algebra-rings/central-simple-algebra"
title = "Central simple algebra"
kind = "definition"
summary = "A nonzero finite-dimensional associative algebra whose center is the base field and whose only two-sided ideals are trivial."
aliases = ["central simple algebra", "CSA"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-modules/algebra-over-ring", "algebra-rings/center-of-ring", "algebra-rings/simple-ring"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

A **central simple algebra** over a field \(F\) is a nonzero finite-dimensional associative unital \(F\)-[[algebra-modules/algebra-over-ring|algebra]] \(A\) such that its [[algebra-rings/center-of-ring|center]] is \(F1_A\) and \(A\) is [[algebra-rings/simple-ring|simple]]: its only [[algebra-rings/two-sided-ideal|two-sided ideals]] are \(0\) and \(A\).

Both the base field and the algebra structure are part of this assertion.

## Examples

The matrix algebra \(M_n(F)\), \(n\ge1\), is central simple. A nonzero two-sided ideal contains every matrix unit after left and right multiplication by matrix units and scalar rescaling; a matrix commuting with all matrix units must be scalar.

Every [[algebra-rings/quaternion-algebra|quaternion algebra]] over \(F\) is central simple, including both division and split examples. Thus “simple” does not imply that every nonzero element is invertible.

A nontrivial [[algebra-fields-galois/field-extension|field extension]] \(K/F\), viewed as an \(F\)-algebra, is simple but not central over \(F\), since its center is \(K\).

## Change of scalars

Central simplicity persists under extension of the base field. Over an [[algebra-fields-galois/algebraic-closure|algebraic closure]], a central simple algebra becomes a matrix algebra. [[algebra-rings/brauer-group|Brauer classes]] record its structure up to matrix-algebra factors.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), §§7.2 and 7.5–7.6, especially Lemma 7.5.4 and Proposition 7.6.1.
