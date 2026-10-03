+++
id = "algebra-rings/brauer-group"
title = "Brauer group of a field"
kind = "definition"
summary = "Central simple algebras modulo matrix stabilization, with tensor product as group law."
aliases = ["Brauer group", "Brauer equivalence", "Br(F)"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/central-simple-algebra", "algebra-rings/matrix-ring", "algebra-modules/tensor-product-algebras", "algebra-rings/opposite-ring"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

For a field \(F\), the **Brauer group** \(\operatorname{Br}(F)\) consists of [[algebra-rings/central-simple-algebra|central simple \(F\)-algebras]] modulo the equivalence
\[
A\sim B\quad\Longleftrightarrow\quad
M_r(A)\cong M_s(B)\text{ as }F\text{-algebras for some }r,s\ge1.
\]

The group law is \([A][B]=[A\otimes_F B]\), using the [[algebra-modules/tensor-product-algebras|tensor product of algebras]]. Its identity is \([F]\), and the inverse of \([A]\) is the class of the [[algebra-rings/opposite-ring|opposite algebra]] \(A^{\mathrm{op}}\).

## What the equivalence forgets

The algebras \(F\) and \(M_n(F)\) have the same Brauer class even though their dimensions differ. More generally, \(A\) and \(M_n(A)\) represent the same class.

The inverse law comes from
\[
A\otimes_F A^{\mathrm{op}}\cong\operatorname{End}_F(A),
\qquad a\otimes b\longmapsto(x\mapsto axb),
\]
whose right side is a matrix algebra.

## Quaternion classes

Standard quaternion conjugation gives \(B\cong B^{\mathrm{op}}\). Hence a quaternion class has order at most two: its class is trivial when \(B\) splits, and has order two otherwise. This does not mean that two arbitrary [[algebra-rings/quaternion-algebra|quaternion algebras]] have isomorphic tensor product presentations.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Lemma 8.3.2, Definition 8.3.3, and §8.3.4.
