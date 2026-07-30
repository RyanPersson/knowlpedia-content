+++
id = "algebra-hyperstructures/stringent-hyperfield"
title = "Stringent hyperfield"
kind = "definition"
summary = "A hyperfield whose sum is single-valued unless the summands are additive inverses."
aliases = ["stringent commutative hyperfield"]
domains = ["algebra-hyperstructures", "matroid-theory"]
section_mode = "progressive"
+++

A [[algebra-hyperstructures/hyperfield|hyperfield]] \(F\) is **stringent** if
\[
a\ne-b\quad\Longrightarrow\quad a\boxplus b
\text{ is a singleton}
\]
for every \(a,b\in F\). Thus genuine ambiguity can occur only when adding an
element to its hyper-additive inverse.

## Examples

Every ordinary field is stringent because all of its sums are singletons.
The Krasner and sign hyperfields are stringent. Every
[[algebra-hyperstructures/valuative-hyperfield|valuative hyperfield]] is
stringent as well: each nonzero element is its own additive inverse, unequal
inputs have the unique maximum as their sum, and only a tied sum can be
multivalued.

## Double distributivity

A hyperfield is **doubly distributive** if
\[
(a\boxplus b)(c\boxplus d)
=ac\boxplus ad\boxplus bc\boxplus bd
\]
as subsets for all \(a,b,c,d\). Every doubly distributive hyperfield is
stringent, but stringent hyperfields need not be doubly distributive. The two
properties should therefore not be used interchangeably.

## Classification context

Bowler and Su classify stringent hyperfields using tropical extensions: an
ordered abelian value group is combined with a residue object that is an
ordinary field, the Krasner hyperfield, or the sign hyperfield. This explains
why ordinary, sign-valued, and valuative examples all occur in the stringent
class without identifying them.

Stringency is useful in matroid theory because it controls cancellation and
implies strong orthogonality properties. The adjectives **weak** and
**strong** for matroids over a hyperfield are separate notions from
stringency.

## References

1. Nathan Bowler and Ting Su, “Classification of doubly distributive skew hyperfields and stringent hypergroups,” *Journal of Algebra* 574 (2021), 669–698. [arXiv:2003.03751](https://arxiv.org/abs/2003.03751). Relevant: definition and classification of stringent hyperfields.
2. Nathan Bowler and Rudi Pendavingh, “Perfect matroids over hyperfields,” 2019. [arXiv:1908.03420](https://arxiv.org/abs/1908.03420). Relevant: stringent hyperfields and matroid orthogonality.
