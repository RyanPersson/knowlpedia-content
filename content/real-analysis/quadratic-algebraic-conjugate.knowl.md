+++
id = "real-analysis/quadratic-algebraic-conjugate"
title = "Quadratic algebraic conjugate"
kind = "definition"
summary = "The other root of the irreducible rational quadratic polynomial satisfied by a quadratic irrational."
aliases = ["algebraic conjugate of a quadratic irrational"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/quadratic-irrational", "shared-foundations/rational-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If \(\alpha\) is a [[real-analysis/quadratic-irrational|quadratic irrational]] with \(a\alpha^2+b\alpha+c=0\), its **quadratic algebraic conjugate** is
\[
\alpha'=-b/a-\alpha.
\]
It is the other root of the same irreducible quadratic. Multiplying the polynomial by a nonzero rational constant does not change either root.

## Product identity

The identities \(\alpha+\alpha'=-b/a\) and \(\alpha\alpha'=c/a\) imply
\[
a(m+n\alpha)(m+n\alpha')=am^2-bmn+cn^2.
\]
For integers \((m,n)\ne(0,0)\), this is a nonzero integer. For example, the conjugate of \(\sqrt2-1\) is \(-\sqrt2-1\). This algebraic conjugation differs from complex conjugation: both numbers here are real.

## References

- [Fukshansky, Diophantine Approximation, §3 (quadratic irrationals)](https://www1.cmc.edu/pages/faculty/lenny/classes/spring_2015/m195/m195_lectures.pdf).
