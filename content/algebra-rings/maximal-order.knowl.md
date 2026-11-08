+++
id = "algebra-rings/maximal-order"
title = "Maximal order"
kind = "definition"
summary = "An order contained in no strictly larger order over the same base in the same algebra."
aliases = ["maximal order", "maximal R-order", "maximal Z-order"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/order-in-algebra"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

An \(R\)-[[algebra-rings/order-in-algebra|order]] \(\mathcal O\) in an algebra \(A\) is **maximal** if every \(R\)-order \(\mathcal O'\) with \(\mathcal O\subseteq\mathcal O'\subseteq A\) equals \(\mathcal O\).

The base ring and ambient algebra are fixed. Maximality is with respect to inclusion among orders, not among all subrings of \(A\).

## Number fields

For a number field \(K\), its [[algebra-fields-galois/ring-of-integers|ring of integers]] \(\mathcal O_K\) is the unique maximal \(\mathbb Z\)-order: every order consists of [[algebra-fields-galois/algebraic-integer|algebraic integers]], and \(\mathcal O_K\) is itself a [[algebra-modules/full-lattice|full lattice]].

An order in \(K\) is a [[algebra-commutative/dedekind-domain|Dedekind domain]] exactly when it equals \(\mathcal O_K\). Every such order is Noetherian of dimension one; the missing condition for a nonmaximal order is integral closedness.

## Noncommutative algebras

Maximal orders need not be unique as embedded subrings. For example, \(M_2(\mathbb Z)\) and \(gM_2(\mathbb Z)g^{-1}\), with \(g=\operatorname{diag}(2,1)\), are distinct maximal orders in \(M_2(\mathbb Q)\).

To see maximality of \(M_2(\mathbb Z)\), an overorder containing a matrix \(x\) also contains \(E_{ai}xE_{ja}=x_{ij}E_{aa}\). Each rational coefficient \(x_{ij}\) must be integral over \(\mathbb Z\), hence an integer. Conjugation preserves maximality.

The number of conjugacy classes of maximal orders is a [[algebra-rings/quaternion-type-number|type number]] in the quaternion setting.

## Dedekind ideal arithmetic: the two-sided theorem

Let \(R\) be a [[algebra-commutative/dedekind-domain|Dedekind domain]], let \(K=\operatorname{Frac}(R)\), let \(A\) be a finite-dimensional central simple \(K\)-algebra, and let \(\mathcal O\subset A\) be a maximal \(R\)-order. Every nonzero integral **two-sided** ideal has a factorization
\[
I=P_1\cdots P_r
\]
into nonzero prime two-sided ideals, unique up to permutation; \(I=\mathcal O\) corresponds to the empty product. Here a proper two-sided ideal \(P\) is prime if \(UV\subseteq P\) implies \(U\subseteq P\) or \(V\subseteq P\) for two-sided ideals \(U,V\). The nonzero primes are maximal two-sided ideals. Full two-sided fractional ideals are invertible and form the free abelian group on these primes, allowing integer exponents. In particular, their multiplication is commutative even when \(\mathcal O\) is not.

For \(\mathcal O=M_2(\mathbb Z)\), every two-sided integral ideal is \(M_2(n\mathbb Z)=n\mathcal O\) for a unique integer \(n\ge0\). Indeed, multiplying a matrix in the ideal on both sides by matrix units isolates any entry in any position. Thus all possible entries form a single ideal of \(\mathbb Z\), and every matrix with entries in that ideal belongs to the original ideal. For \(n>0\), its prime factorization is exactly the integer prime factorization of \(n\).

This theorem applies to the [[catalog/arithmetic/hurwitz-order|Hurwitz order]] in the rational Hamilton quaternion algebra. It does not assert unique factorization of quaternion elements, nor factorization of arbitrary right ideals into two-sided prime ideals: such a product would necessarily be two-sided. The [[algebra-rings/quaternion-fractional-ideal|matrix example for one-sided ideals]] shows the obstruction explicitly.

## Scope of the analogy

For a Dedekind domain \(R\), all nonzero fractional ideals are invertible, \(R\) is a two-sided multiplicative identity, and multiplication gives \(I\otimes_RJ\cong IJ\). For maximal orders, the analogous group concerns **two-sided** fractional ideals. Full one-sided ideals instead have inverses between their possibly different left and right orders; see the [[algebra-rings/ideal-tensor-multiplication-isomorphism|typed multiplication theorem]].

Maximal orders are an arithmetic generalization in this setting, not a definition encompassing every Dedekind domain when the base is fixed to \(\mathbb Z\). They need not be domains: \(M_2(\mathbb Z)\) has zero divisors. The central simple ambient algebra and Dedekind base above are sufficient hypotheses, not assertions about arbitrary maximal orders in arbitrary algebras.

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definition 10.4.1 and §10.5.

2. John Voight, *Quaternion Algebras*, [Chapter 18](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_18), Theorem 18.1.2 and §18.2.
