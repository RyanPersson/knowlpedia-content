+++
id = "catalog/relationships/triality-algebra"
title = "Triality algebra of a composition algebra"
kind = "knowl"
summary = "Triples of skew linear maps satisfying a three-slot Leibniz identity."
aliases = ["Triality algebra of a composition algebra"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/composition-algebra", "linear-algebra/bilinear-form"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

For a real [[nonassociative-algebra/composition-algebra|composition algebra]] \(A\) with its norm [[linear-algebra/bilinear-form|bilinear form]], its **triality algebra** is
\[
\operatorname{tri}(A)=
\{(T_1,T_2,T_3)\in\mathfrak{so}(A)^3:
T_1(xy)=T_2(x)y+xT_3(y)\text{ for all }x,y\in A\},
\]
with componentwise commutator. Here \(\mathfrak{so}(A)\) means the skew endomorphisms for the specified bilinear form, which may be indefinite for split \(A\). This fixes the order of the three slots.

## Division inputs

For the positive-definite real composition algebras,
\[
\begin{aligned}
\operatorname{tri}(\mathbb R)&=0,&
\operatorname{tri}(\mathbb C)&\cong\mathbb R^2\text{ with zero bracket},\\
\operatorname{tri}(\mathbb H)&\cong\mathfrak{sp}(1)^{\oplus3},&
\operatorname{tri}(\mathbb O)&\cong\mathfrak{so}(8).
\end{aligned}
\]
Their dimensions are \(0,2,9,28\). The quaternionic output is the [[catalog/relationships/sp1-triple-direct-sum|triple direct sum]], while the octonionic output gives [[lie-groups/spin8-triality|infinitesimal triality]].

## Derivations inside triality

A derivation \(D\) gives the diagonal triple \((D,D,D)\). Expanding two applications of the defining identity shows that componentwise commutators satisfy it again; thus the displayed set is a Lie subalgebra of \(\mathfrak{so}(A)^3\).

## References

1. C. H. Barton and A. Sudbery, “Magic squares and matrix models of Lie algebras,” §4.1, Definition 2, Lemma 4.1 and the table on p. 13; our last two slots are interchanged relative to Definition 2. [Paper](https://arxiv.org/pdf/math/0203010).
