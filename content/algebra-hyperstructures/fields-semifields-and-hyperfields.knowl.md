+++
id = "algebra-hyperstructures/fields-semifields-and-hyperfields"
title = "Fields, semifields, and hyperfields"
kind = "comparison"
summary = "A comparison of multiplicative division structures with single-valued or multivalued addition."
aliases = ["comparison of fields semifields and hyperfields", "field as a semifield and hyperfield"]
domains = ["algebra-hyperstructures", "algebra-rings"]
section_mode = "progressive"
+++

An ordinary [[algebra-rings/field|field]] is both a
[[algebra-rings/semifield|semifield]] and a
[[algebra-hyperstructures/hyperfield|hyperfield]]: forget the requirement of
additive inverses to get the first viewpoint, or regard each ordinary sum as
a singleton hyper-sum to get the second. Neither converse holds.

## What each notion changes

| Structure | Addition | Additive inverse | Nonzero multiplication |
|---|---|---|---|
| Field | single-valued | unique in an abelian group | abelian group |
| Semifield | single-valued | not required | abelian group |
| Hyperfield | nonempty-set-valued | unique in a canonical hypergroup | abelian group |

The Boolean and tropical semifields are not fields because they lack ordinary
additive inverses. The Krasner, sign, and tropical hyperfields are not fields
because their addition is genuinely multivalued.

## Non-inclusions

A general semifield is not a hyperfield. For example, tropical semiring
addition is idempotent and single-valued, but its finite elements do not have
additive inverses in an abelian group or canonical hypergroup. A general
hyperfield is not a semiring because a semiring requires a function
\(S\times S\to S\), not a set of possible sums.

The overlap of semifields and hyperfields, when their additions are required
to be the same operation, is exactly ordinary fields: singleton-valued
canonical hypergroup addition supplies additive inverses.

## A field in both categories

Sending a field to its underlying semifield and sending it to the hyperfield
with singleton hyper-sums give two fully faithful embeddings:
\[
\mathbf{Field}\hookrightarrow\mathbf{SemiField},
\qquad
\mathbf{Field}\hookrightarrow\mathbf{HyperField}.
\]
A unit-preserving semiring map between fields automatically preserves
additive inverses, hence is a field homomorphism. A weak hyperfield map
between singleton-addition hyperfields also preserves addition by equality,
so it too is a field homomorphism. These are two presentations of the same
field operations in different ambient categories, not a functor identifying
all semifields with all hyperfields.

## Semirings and hyperrings are incomparable

The same distinction holds one level up. Semirings retain single-valued
addition but may lose negatives; hyperrings retain reversible additive
negation but allow multivalued sums. Both contain commutative rings as a
special case, yet neither is a subclass of the other. Ordered blueprints can
encode both kinds of structure in a wider framework, but this does not make
semirings and hyperrings equivalent.

## References

1. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: §2, fields and standard hyperfields.
2. Jaiung Jun, “Algebraic Geometry Over Hyperrings,” *Advances in Mathematics* 323 (2018), 142–192. [arXiv:1512.04837](https://arxiv.org/abs/1512.04837). Relevant: semiring-to-hyperfield constructions and structural comparisons.
