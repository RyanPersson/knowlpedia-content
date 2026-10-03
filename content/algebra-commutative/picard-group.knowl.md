+++
id = "algebra-commutative/picard-group"
title = "Picard group of a ring"
kind = "definition"
summary = "The abelian group of isomorphism classes of invertible modules under tensor product."
aliases = ["Picard group of a ring", "Picard group", "Pic(R)", "ideal class group of an order"]
domains = ["algebra-commutative"]
section_mode = "progressive"
prerequisites = ["algebra-modules/invertible-module", "algebra-modules/tensor-product", "algebra-groups/abelian-group"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

For a commutative [[algebra-rings/unital-ring|unital ring]] \(R\), the **Picard group** \(\operatorname{Pic}(R)\) is the set of isomorphism classes of [[algebra-modules/invertible-module|invertible \(R\)-modules]], with operation
\[
[L][M]=[L\otimes_R M].
\]

The identity is \([R]\), and \([L]^{-1}=[\operatorname{Hom}_R(L,R)]\). Associativity and symmetry of the [[algebra-modules/tensor-product|tensor product]] make this an [[algebra-groups/abelian-group|abelian group]].

## Fractional ideals over a domain

If \(R\) is a domain with [[algebra-rings/fraction-field|fraction field]] \(K\), every invertible module can be embedded in \(K\) after choosing a basis of its one-dimensional scalar extension. This identifies
\[
\operatorname{Pic}(R)\cong
\frac{\{\text{invertible fractional ideals of }R\}}
     {\{aR:a\in K^\times\}}.
\]
Two such ideals are isomorphic as \(R\)-modules exactly when one is a nonzero scalar multiple of the other. Changing the chosen embedding therefore does not change the class.

## Orders and number rings

For a number-field order \(\mathcal O\), this is the group of [[algebra-commutative/invertible-fractional-ideal|invertible fractional ideals]] modulo [[algebra-commutative/principal-fractional-ideal|principal ones]]. Noninvertible ideals are excluded.

For the [[algebra-rings/maximal-order|maximal order]] \(\mathcal O_K\), all nonzero fractional ideals are invertible, and \(\operatorname{Pic}(\mathcal O_K)\) is the existing [[algebra-fields-galois/ideal-class-group|ideal class group]] of \(K\).

## References

1. The Stacks Project, [Picard groups of rings](https://stacks.math.columbia.edu/tag/0AFW), Definition 15.119.1, Lemma 15.119.2, and the Picard-group definition following the lemma.
