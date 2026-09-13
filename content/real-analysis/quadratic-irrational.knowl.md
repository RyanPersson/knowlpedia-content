+++
id = "real-analysis/quadratic-irrational"
title = "Quadratic irrational"
kind = "definition"
summary = "An irrational real root of a quadratic polynomial with integer coefficients."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/irrational-number", "real-analysis/polynomial", "shared-foundations/integers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **quadratic irrational** is an [[real-analysis/irrational-number|irrational real number]] \(\alpha\) satisfying
\[
a\alpha^2+b\alpha+c=0
\]
for some integers \(a,b,c\) with \(a\ne0\). Because \(\alpha\) is irrational, the polynomial cannot factor into linear polynomials over \(\mathbb Q\). Its discriminant \(b^2-4ac\) is positive and is not an integer square.

## Examples

The numbers \(\sqrt2\) and \(\sqrt2-1\) satisfy \(x^2-2=0\) and \(x^2+2x-1=0\), respectively. Each has a second real root, its [[real-analysis/quadratic-algebraic-conjugate|quadratic algebraic conjugate]]. The two roots together provide arithmetic lower bounds on nonzero integer linear forms.

## References

- [Fukshansky, Diophantine Approximation, §3 (quadratic irrationals)](https://www1.cmc.edu/pages/faculty/lenny/classes/spring_2015/m195/m195_lectures.pdf).
