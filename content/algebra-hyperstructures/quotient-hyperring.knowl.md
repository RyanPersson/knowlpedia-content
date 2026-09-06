+++
id = "algebra-hyperstructures/quotient-hyperring"
title = "Quotient hyperring"
kind = "construction"
summary = "The hyperring of multiplicative orbits R/G of a ring under a subgroup of units."
aliases = ["Krasner quotient hyperring", "factor hyperring by a multiplicative subgroup"]
domains = ["algebra-hyperstructures", "algebra-rings"]
prerequisites = ["algebra-rings/commutative-ring", "algebra-rings/group-of-units", "algebra-hyperstructures/hyperring"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(R\) be a [[algebra-rings/commutative-ring|commutative ring]] and let \(G\le R^\times\) be a multiplicative
subgroup of its [[algebra-rings/group-of-units|units]]. The **quotient
hyperring** \(R/G\) is the set of multiplicative orbits
\[
[a]=aG
\]
with multiplication \([a][b]=[ab]\) and hyperaddition
\[
[a]\boxplus[b]
=\{[ag+bh]:g,h\in G\}.
\]
These operations are independent of the chosen representatives and make
\(R/G\) a [[algebra-hyperstructures/hyperring|Krasner hyperring]].

## Why addition is multivalued

A quotient representative can be rescaled independently before addition.
Different choices of \(g\) and \(h\) can place \(ag+bh\) in different
orbits, so addition returns the set of all possible resulting orbits.
Multiplication is single-valued because rescaling \(a\) and \(b\) only
rescales \(ab\) by an element of \(G\).

## The quotient map

The orbit map
\[
\pi:R\longrightarrow R/G,\qquad a\longmapsto[a]
\]
is a [[algebra-hyperstructures/hyperring-homomorphism|weak hyperring homomorphism]] after \(R\) is viewed as a singleton-valued
hyperring. It is generally not strong: the image \(\{[a+b]\}\) can be a
proper subset of \([a]\boxplus[b]\).

## Hyperfield case

If \(R=K\) is a field, every nonzero orbit has a multiplicative inverse, so
\(K/G\) is a
[[algebra-hyperstructures/hyperfield-of-a-field-quotient|quotient
hyperfield]]. The Krasner and [[algebra-hyperstructures/sign-hyperfield|sign hyperfields]] arise this way. This
multiplicative-orbit construction is not the ordinary [[algebra-rings/quotient-ring|quotient ring]] \(R/I\)
by an additive ideal.

## References

1. Alain Connes and Caterina Consani, “The hyperring of adèle classes,” *Journal of Number Theory* 131 (2011), 159–194. [arXiv:1001.4260](https://arxiv.org/abs/1001.4260). Relevant: Proposition 2.6 and quotient hyperrings \(R/G\).
2. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: factor multirings and factor hyperfields.
