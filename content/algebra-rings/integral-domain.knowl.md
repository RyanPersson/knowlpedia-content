+++
id = "algebra-rings/integral-domain"
title = "Integral domain"
kind = "knowl"
summary = "A commutative unital ring with no zero divisors."
aliases = ["integral-domain", "Integral domain"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/commutative-ring", "algebra-rings/zero-divisor"]
dependency_review_count = 1
legacy_source_path = "algebra-rings/integral-domain.md"
+++

An **integral domain** is a [[algebra-rings/commutative-ring|commutative ring]] with \(1\neq 0\) such that for all \(a,b\in R\), \(ab=0\) implies \(a=0\) or \(b=0\) (equivalently, \(R\) has no [[algebra-rings/zero-divisor|zero divisors]]).

## Remarks

Integral domains are the natural setting for divisibility and factorization, and every [[algebra-rings/field|field]] is an integral domain. Many constructions (e.g. forming the [[algebra-rings/fraction-field|field of fractions]]) require the domain hypothesis.

## Examples

- \(\mathbb{Z}\) is an integral domain.
- If \(k\) is a field, then \(k[x]\) is an integral domain.
- \(\mathbb{Z}/6\mathbb{Z}\) is not an integral domain since \(2\cdot 3=0\) in the quotient.
