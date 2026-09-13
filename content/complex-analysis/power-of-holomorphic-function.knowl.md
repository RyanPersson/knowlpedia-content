+++
id = "complex-analysis/power-of-holomorphic-function"
title = "Power of a holomorphic function using a chosen logarithm"
kind = "definition"
summary = "The branch-dependent expression exp(a L(z)) when L is a holomorphic logarithm of f."
aliases = ["analytic fractional power", "complex power on a branch"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/holomorphic-logarithm", "real-analysis/exponential-function", "real-analysis/chain-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Given a [[complex-analysis/holomorphic-logarithm|holomorphic logarithm]] \(L\) of a nonvanishing function \(f\), define its **power on that branch** by
\[
f(z)^a=\exp(aL(z)),\qquad a\in\mathbb C.
\]
It is holomorphic jointly in \(z\) and \(a\). Changing the logarithm by \(2\pi i k\) multiplies the result by \(e^{2\pi i k a}\), so a noninteger exponent requires a branch choice.

## Derivatives and real values

For fixed \(a\), \((f^a)'=a f^a f'/f\), and \(\partial_a f^a=L f^a\). If \(f\) is positive on a real interval and \(L\) agrees with the real logarithm there, this definition agrees with the real positive-base power. Derivative estimates require a bound on the chosen branch in a complex neighborhood.
