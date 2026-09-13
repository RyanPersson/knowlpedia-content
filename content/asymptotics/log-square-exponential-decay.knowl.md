+++
id = "asymptotics/log-square-exponential-decay"
title = "Exponential decay in the square of a logarithm"
kind = "theorem"
summary = "A Gaussian in log one over the scale dominates every fixed inverse power and logarithmic loss."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["real-analysis/exponential-function", "real-analysis/natural-logarithm", "asymptotics/logarithmic-loss-absorption", "asymptotics/big-o"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For fixed \(c>0\), \(A,B\ge0\), and every \(N\ge0\),
\[
q^{-A}(1+|\log q|)^B e^{-c(\log(1/q))^2}=O(q^N)
\qquad(q\downarrow0).
\]
Thus decay exponential in the square of the logarithm is stronger than any fixed power of \(q\), even after [[asymptotics/logarithmic-loss-absorption|polynomial and logarithmic losses]].

## Proof and derivative use

Set \(s=\log(1/q)\). Dividing the left side by \(q^N\) gives \((1+s)^B\exp(-cs^2+(A+N)s)\), which tends to zero since the negative quadratic term dominates. If each prescribed derivative of a family obeys a bound of this form, with its own fixed \(A,B,C\), every derivative has infinite-order decay. The scalar value estimate alone makes no claim about derivatives of another family sharing that value bound.
