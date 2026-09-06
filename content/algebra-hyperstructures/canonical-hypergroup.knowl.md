+++
id = "algebra-hyperstructures/canonical-hypergroup"
title = "Canonical hypergroup"
kind = "definition"
summary = "A commutative associative hyperoperation with zero, unique inverses, and reversibility."
aliases = ["canonical commutative hypergroup", "Krasner hypergroup"]
domains = ["algebra-hyperstructures", "algebra-rings"]
prerequisites = ["algebra-hyperstructures/hyperoperation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **canonical hypergroup** is a set \(H\) with a
[[algebra-hyperstructures/hyperoperation|hyperoperation]] \(\boxplus\), an
element \(0\), and a unary inverse \(a\mapsto-a\) such that, for all
\(a,b,c\in H\):

1. \(\boxplus\) is commutative and associative;
2. \(a\boxplus0=\{a\}\);
3. \(0\in a\boxplus(-a)\), and \(-a\) is the unique element with this property;
4. **reversibility** holds:
   \[
   c\in a\boxplus b\quad\Longleftrightarrow\quad
   b\in c\boxplus(-a).
   \]

## Reversibility as subtraction

In an [[algebra-groups/abelian-group|abelian group]], \(c=a+b\) is equivalent to \(b=c-a\).
Reversibility is the set-valued version of this implication and prevents a
general associative hyperoperation from being called an additive
hypergroup without an adequate subtraction law.

## Ordinary groups

Every abelian group becomes a canonical hypergroup by replacing each sum
\(a+b\) by the singleton \(\{a+b\}\). Conversely, a canonical hypergroup all
of whose sums are singletons is an abelian group.

## Terminology warning

“Hypergroup” also names analytic objects whose products are probability
measures. Those are not the Krasner canonical hypergroups used in hyperring
theory.

## References

1. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: Definition 2.1.
2. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: multigroups and hyperfields.
