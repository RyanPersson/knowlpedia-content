+++
id = "algebra-rings/prime-ring"
title = "Prime ring"
kind = "knowl"
summary = "A ring in which the product of nonzero ideals is never zero."
aliases = ["prime-ring", "Prime ring"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/ring", "algebra-rings/two-sided-ideal", "algebra-rings/product-of-ideals"]
dependency_review_count = 1
legacy_source_path = "algebra-rings/prime-ring.md"
+++

A **prime ring** is a [[algebra-rings/ring|ring]] \(R\) such that for any nonzero [[algebra-rings/two-sided-ideal|two-sided ideals]] \(A,B\subseteq R\), one has \(AB\neq 0\), where \(AB\) denotes the [[algebra-rings/product-of-ideals|product of ideals]]. Equivalently: if \(A\) and \(B\) are ideals with \(AB=0\), then \(A=0\) or \(B=0\).

## Remarks

In the commutative unital case with \(1\neq 0\), primeness is equivalent to being an [[algebra-rings/integral-domain|integral domain]]: the ideals \((a)\) and \((b)\) show that \(ab=0\) forces \(a=0\) or \(b=0\).

## Examples

- If \(D\) is a division ring and \(n\ge 1\), then \(M_n(D)\) is a prime ring.
- Any integral domain is a prime ring (commutative case).
- A direct product \(R_1\times R_2\) with \(R_1,R_2\neq 0\) is not prime: \((R_1\times 0)(0\times R_2)=0\).
