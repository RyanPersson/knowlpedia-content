+++
id = "real-analysis/quadratic-irrational-lower-bound"
title = "Quadratic irrational lower bound"
kind = "theorem"
summary = "Integer linear forms in a fixed quadratic irrational have a reciprocal polynomial lower bound."
aliases = []
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/quadratic-algebraic-conjugate", "linear-algebra/euclidean-norm", "real-analysis/absolute-value"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a fixed [[real-analysis/quadratic-irrational|quadratic irrational]] \(\alpha\), there is a constant \(c_\alpha>0\) such that
\[
|m+n\alpha|\ge\frac{c_\alpha}{1+\sqrt{m^2+n^2}}
\quad\text{for all }(m,n)\in\mathbb Z^2\setminus\{(0,0)\}.
\]

## Proof

With \(a,b,c\) and \(\alpha'\) as in the conjugate identity, the product \(a(m+n\alpha)(m+n\alpha')\) is a nonzero integer and has absolute value at least one. Also \(|m+n\alpha'|\le C_\alpha\sqrt{m^2+n^2}\). Dividing gives the claimed bound.

## Rational approximation

There is consequently \(c'\!>0\) such that \(|\alpha-p/q|\ge c'/q^2\) for all integers \(p\) and \(q\ge1\). When \(|p/q-\alpha|\le1\), apply the linear-form estimate and use \(|p|\le(|\alpha|+1)q\); when the difference exceeds one, reduce the constant. This is the badly approximable property of quadratic irrationals.

## References

- [Fukshansky, Diophantine Approximation, §3 (quadratic irrationals)](https://www1.cmc.edu/pages/faculty/lenny/classes/spring_2015/m195/m195_lectures.pdf).
