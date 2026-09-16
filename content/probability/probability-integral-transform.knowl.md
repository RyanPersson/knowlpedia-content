+++
id = "probability/probability-integral-transform"
title = "Probability integral transform"
kind = "theorem"
summary = "A continuous cumulative distribution function sends its random variable to the uniform law."
aliases = []
domains = ["probability"]
section_mode = "progressive"
prerequisites = ["probability/cumulative-distribution-function", "probability/random-variable"]
+++

If a real random variable \(Z\) has continuous [[probability/cumulative-distribution-function|cumulative distribution function]] \(F\), then **the probability integral transform** states that \(F(Z)\) is uniform on \((0,1)\).

## Standard normal coordinates

For the strictly increasing standard normal CDF
\[
\Phi(t)=\frac1{\sqrt{2\pi}}\int_{-\infty}^t e^{-s^2/2}\,ds,
\]
the map \(\Phi:\mathbb R\to(0,1)\) is a bijection, and \(\mathbb P(\Phi(Z)\leq u)=\mathbb P(Z\leq\Phi^{-1}(u))=u\). Applying it coordinatewise gives a measure-space isomorphism
\[
F_d:(\mathbb R^d,\gamma_d)\to((0,1)^d,\lambda_d),
\qquad F_d(x)_j=\Phi(x_j).
\]

## Scope

A CDF with jumps does not generally produce a uniform variable by direct composition. Continuity is the hypothesis of the theorem. Strict monotonicity is the additional property used in the Gaussian example to obtain an ordinary inverse function.
