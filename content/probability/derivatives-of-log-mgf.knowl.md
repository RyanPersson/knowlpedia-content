+++
id = "probability/derivatives-of-log-mgf"
title = "Derivatives of the log moment generating function"
kind = "theorem"
summary = "The first two derivatives of a scalar log moment generating function are the tilted mean and tilted variance."
aliases = ["tilted variance identity"]
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/exponential-tilt", "probability/cumulant-generating-function", "probability/variance", "measure-theory/differentiation-under-integral", "real-analysis/quotient-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Suppose \(M(\theta)=\mathbb E e^{\theta X}\) is finite on an open interval \(I\), and let \(g=\log M\). For \(\theta\in I\),
\[
g'(\theta)=\mathbb E_\theta X,\qquad
g''(\theta)=\operatorname{Var}_\theta(X)\ge0,
\]
where \(\mathbb E_\theta\) uses the [[probability/exponential-tilt|tilted measure]]. If \(X\) is not almost surely constant, then \(g''>0\) throughout \(I\).

## Derivation

On compact subintervals of \(I\), nearby exponential moments dominate \(|X|^k e^{\theta X}\) for each fixed \(k\). Differentiation under the integral gives \(M'=\mathbb E[Xe^{\theta X}]\) and \(M''=\mathbb E[X^2e^{\theta X}]\). Hence \(g'=M'/M\) and \(g''=M''/M-(M'/M)^2\). Positivity of the tilted density preserves the property of being almost surely nonconstant, proving strict positivity of the variance in that case.

## References

- [Fithian, Exponential Families (derivatives of the log-partition function)](https://www.stat.berkeley.edu/~wfithian/courses/stat210a/exponential-families.html).
