+++
id = "algebra-groups/commutative-monoid"
title = "Commutative monoid"
kind = "definition"
summary = "A monoid whose multiplication is commutative."
aliases = ["abelian monoid", "commutative multiplicative monoid"]
domains = ["algebra-groups", "algebra-rings"]
prerequisites = ["algebra-groups/monoid"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **commutative monoid** is a [[algebra-groups/monoid|monoid]] \((A,\cdot,1)\) such that
\[
ab=ba
\]
for all \(a,b\in A\). A **commutative monoid with zero** also has an absorbing element \(0\), so \(0a=0\) for every \(a\in A\).

## Conventions

“Abelian monoid” is a common synonym. Additively written commutative monoids use \((A,+,0)\); multiplicative notation is standard in blueprint theory. In that setting \(0\) and \(1\) are distinguished and usually required to be different unless the trivial object is explicitly allowed.

## Examples

- The nonnegative integers under addition form a commutative monoid.
- The underlying multiplicative monoid of a commutative ring consists of all
  ring elements and has \(0\) as an absorbing element. If the ring has no
  [[algebra-rings/zero-divisor|zero divisors]], its nonzero elements are also closed under multiplication.
- Every [[algebra-groups/abelian-group|abelian group]] is a commutative monoid, but a commutative monoid need not have inverses.

## References

1. Nicolas Bourbaki, *Algebra I: Chapters 1–3*, Springer, 1989. [Publisher record](https://doi.org/10.1007/978-3-642-61698-3). Relevant: Chapter I, algebraic structures with one composition law.
