+++
id = "algebra-rings/semiring-homomorphism"
title = "Semiring homomorphism"
kind = "definition"
summary = "A map preserving zero, one, addition, and multiplication."
aliases = ["homomorphism of semirings", "semiring map"]
domains = ["algebra-rings", "algebra-hyperstructures"]
section_mode = "progressive"
prerequisites = ["algebra-rings/semiring"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For [[algebra-rings/semiring|semirings]] \(S\) and \(T\), a **semiring
homomorphism** is a function \(f:S\to T\) satisfying
\[
f(0)=0,\qquad f(1)=1,\qquad
f(a+b)=f(a)+f(b),\qquad f(ab)=f(a)f(b)
\]
for all \(a,b\in S\). In particular, semiring homomorphisms are
unit-preserving in the house convention.

## Categorical role

Identity functions and composites are semiring homomorphisms, so semirings
and these maps form a category. Restricting to [[algebra-rings/commutative-semiring|commutative semirings]] gives the
category used in the tropical-algebra pages.

## Convention warning

Some authors permit maps with \(f(1)\ne1\), especially when studying ideals
or nonunital semirings. Such a map is not a semiring homomorphism here unless
it is explicitly called **nonunital**. This differs from a weak hyperring
homomorphism: ordinary semiring addition is single-valued, so its preservation
is an equality rather than an inclusion.

## References

1. Jonathan S. Golan, *Semirings and their Applications*, Kluwer, 1999. [Publisher DOI record](https://doi.org/10.1007/978-94-015-9333-5). Relevant: semiring morphisms in Chapter 1.
