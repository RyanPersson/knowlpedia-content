+++
id = "algebra-hyperstructures/doubly-distributive-hyperfield"
title = "Doubly distributive hyperfield"
kind = "definition"
summary = "A hyperfield in which the product of two binary hypersums equals the four-term hyper-sum of pairwise products."
aliases = ["double-distributive hyperfield", "doubly distributive commutative hyperfield"]
domains = ["algebra-hyperstructures", "matroid-theory"]
prerequisites = ["algebra-hyperstructures/hyperfield"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A [[algebra-hyperstructures/hyperfield|hyperfield]] \(F\) is **doubly
distributive** if
\[
(a\boxplus b)(c\boxplus d)
=ac\boxplus ad\boxplus bc\boxplus bd
\]
as subsets of \(F\) for every \(a,b,c,d\in F\). On the left, multiplication
of subsets means
\[
XY=\{xy:x\in X,\ y\in Y\}.
\]

Ordinary distributivity only distributes multiplication by one element over
one hypersum. Double distributivity is the stronger assertion that
distributing the product of two hypersums introduces no extra or missing
values.

## Examples

[[algebra-rings/field|Ordinary fields]], the
[[algebra-hyperstructures/krasner-hyperfield|Krasner hyperfield]], the
[[algebra-hyperstructures/sign-hyperfield|sign hyperfield]], and the
[[algebra-hyperstructures/tropical-hyperfield|tropical hyperfield]] are doubly
distributive. Every doubly distributive hyperfield is
[[algebra-hyperstructures/doubly-distributive-hyperfields-are-stringent|stringent]],
but the converse fails.

## References
Nathan Bowler and Ting Su,
[*Classification of doubly distributive skew hyperfields and stringent hypergroups*, Definition 2.8](https://arxiv.org/abs/2003.03751).
