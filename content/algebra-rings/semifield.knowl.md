+++
id = "algebra-rings/semifield"
title = "Semifield"
kind = "definition"
summary = "A nontrivial commutative semiring in which every nonzero element is multiplicatively invertible."
aliases = ["commutative semifield", "division semiring"]
domains = ["algebra-rings", "algebra-hyperstructures"]
section_mode = "progressive"
+++

A **semifield** is a [[algebra-rings/commutative-semiring|commutative
semiring]] \(S\) with \(0\ne1\) such that \(S^\times=S\setminus\{0\}\).
Equivalently, the nonzero elements form an abelian group under multiplication.
Additive inverses are not required.

## Examples and non-examples

Every [[algebra-rings/field|field]] is a semifield. The nonnegative real
numbers, the Boolean semifield, and tropical semifields are semifields that
are not fields. The natural numbers are not a semifield because, for example,
\(2\) has no multiplicative inverse in \(\mathbb N\).

## Convention warning

In some literature **semifield** means a possibly noncommutative division
semiring; in finite geometry it can instead mean a nonassociative division
algebra. Neither broader usage is intended here: multiplication is
commutative and associative. A hyperfield is a different object because its
addition may be multivalued.

## References

1. Jonathan S. Golan, *Semirings and their Applications*, Kluwer, 1999. [Publisher DOI record](https://doi.org/10.1007/978-94-015-9333-5). Relevant: division semirings and semifields.
2. Grigori L. Litvinov, Viktor P. Maslov, and Grigori B. Shpiz, “Idempotent (Asymptotic) Mathematics and the Representation Theory,” 2002. [arXiv:math/0206025](https://arxiv.org/abs/math/0206025). Relevant: idempotent semifields.
