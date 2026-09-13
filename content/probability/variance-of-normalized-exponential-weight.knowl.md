+++
id = "probability/variance-of-normalized-exponential-weight"
title = "Variance of a normalized exponential weight"
kind = "theorem"
summary = "The variance of an exponential likelihood ratio is a ratio of moment generating functions and increases with a positive tilt parameter."
aliases = []
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/exponential-tilt", "probability/variance", "probability/derivatives-of-log-mgf"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a bounded real random variable and define the normalized weight \(W_t=e^{tX}/M(t)\), where \(M(t)=\mathbb E e^{tX}\). Then \(\mathbb EW_t=1\), and its [[probability/variance|variance under the original measure]] is
\[
\operatorname{Var}(W_t)=\frac{M(2t)}{M(t)^2}-1.
\]
If \(X\) is not almost surely constant, this variance is strictly increasing for \(t>0\).

## Proof and limits

The formula follows by integrating \(W_t^2\). With \(g=\log M\), the derivative of \(g(2t)-2g(t)\) is \(2(g'(2t)-g'(t))>0\), since the tilted variance identity gives \(g''>0\). The variance of \(W_t\) is different from the tilted variance of \(X\). Monotonicity alone does not imply divergence as \(t\to\infty\): for a Bernoulli variable with success probability \(p\in(0,1)\), the limit is \(1/p-1\).
