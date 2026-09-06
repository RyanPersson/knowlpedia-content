+++
id = "algebra-rings/semiring"
title = "Semiring"
kind = "definition"
summary = "An additive commutative monoid with a distributive, unital multiplication and absorbing zero."
aliases = ["rig", "unital semiring"]
domains = ["algebra-rings", "algebra-hyperstructures"]
section_mode = "progressive"
prerequisites = ["algebra-groups/commutative-monoid", "algebra-groups/monoid"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **semiring** is a set \(S\) with operations \(+\) and \(\cdot\) and elements
\(0,1\) such that \((S,+,0)\) is a
[[algebra-groups/commutative-monoid|commutative monoid]],
\((S,\cdot,1)\) is a [[algebra-groups/monoid|monoid]], multiplication
distributes over addition on both sides, and \(0s=s0=0\) for every \(s\in S\).
The house convention includes a multiplicative identity but does not require
\(0\ne1\) or commutative multiplication.

## Relation to rings

Every [[algebra-rings/unital-ring|unital ring]] is a semiring after one
forgets that additive inverses are part of the specified structure.
Conversely, a semiring whose additive monoid is an [[algebra-groups/abelian-group|abelian group]] is a unital
ring. Thus semirings weaken the additive part of unital ring theory while
keeping addition single-valued.

## Examples and conventions

The natural numbers \(\mathbb N\), the nonnegative real numbers, and the
endomorphisms of a commutative monoid under pointwise addition and composition
are semirings. The last example can be noncommutative.

Some authors omit \(1\), allow noncommutative addition, or use **rig** to
emphasize “ring without negatives.” Those are broader conventions than the one
used here. In the rest of this subject, **commutative semiring** explicitly
means that multiplication is also commutative.

## References

1. Jonathan S. Golan, *Semirings and their Applications*, Kluwer, 1999. [Publisher DOI record](https://doi.org/10.1007/978-94-015-9333-5). Relevant: Chapter 1, semirings and their morphisms.
2. Grigori L. Litvinov, Viktor P. Maslov, and Grigori B. Shpiz, “Idempotent (Asymptotic) Mathematics and the Representation Theory,” 2002. [arXiv:math/0206025](https://arxiv.org/abs/math/0206025). Relevant: idempotent-semiring conventions and examples.
