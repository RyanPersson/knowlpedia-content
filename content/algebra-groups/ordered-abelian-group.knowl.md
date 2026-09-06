+++
id = "algebra-groups/ordered-abelian-group"
title = "Ordered abelian group"
kind = "definition"
summary = "An abelian group with a translation-invariant total order."
aliases = ["totally ordered abelian group", "ordered commutative group"]
domains = ["algebra-groups", "order-theory"]
prerequisites = ["algebra-groups/abelian-group", "shared-foundations/total-order"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

An **ordered abelian group** is an [[algebra-groups/abelian-group|abelian group]] \((\Gamma,+,0)\) equipped with a [[shared-foundations/total-order|total order]] \(\leq\) that is translation-invariant:
\[
a\leq b\quad\Longrightarrow\quad a+c\leq b+c
\]
for all \(a,b,c\in\Gamma\). Equivalently, its positive cone
\(\Gamma_{\geq0}=\{a:0\leq a\}\) is closed under addition, satisfies
\(\Gamma_{\geq0}\cap(-\Gamma_{\geq0})=\{0\}\), and obeys
\(\Gamma_{\geq0}\cup(-\Gamma_{\geq0})=\Gamma\).

## Examples

The additive groups \(\mathbb Z\), \(\mathbb Q\), and \(\mathbb R\) with their usual orders are ordered abelian groups. The lexicographic order makes \(\mathbb Z^n\) an ordered abelian group that is generally non-Archimedean.

## Value groups

The codomain of a valuation is commonly an ordered abelian group, often enlarged by an element \(\infty\). The group operation records multiplication of valued elements, while the order compares their sizes.

## Terminology

Some sources use “ordered abelian group” for a translation-invariant [[shared-foundations/partial-order|partial order]] and say **linearly ordered** or **totally ordered** when every pair is comparable. Here the term uses the total-order convention standard for [[algebra-fields-galois/value-group|valuation value groups]].

## References

1. K. R. Goodearl, *Partially Ordered Abelian Groups with Interpolation*, American Mathematical Society, 1986. [DOI record](https://doi.org/10.1090/surv/020). Relevant: Chapter 1.
