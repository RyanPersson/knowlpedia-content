+++
id = "partial-differential-equations/heat-kernel-solution"
title = "Solution of the heat equation by Gaussian convolution"
kind = "theorem"
summary = "Convolving Schwartz initial data with the heat kernel gives a smooth solution attaining its initial value."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/heat-semigroup", "partial-differential-equations/initial-datum", "functional-analysis/schwartz-space", "measure-theory/differentiation-under-integral"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(u_0\) in the [[functional-analysis/schwartz-space|Schwartz space]] on \(\mathbb R^n\),
\[
u(t,x)=\int_{\mathbb R^n}G_\nu(t,x-y)u_0(y)\,dy
\]
is a smooth solution of \(\partial_tu=\nu\Delta u\) for \(t>0\), with \(u(t)\to u_0\) uniformly as \(t\downarrow0\).

## Verification

For positive time, derivatives of the Gaussian are integrable and differentiate under the integral. Applying its heat equation gives the equation for \(u\). To recover the initial value, write the difference as the average of \(u_0(x-y)-u_0(x)\); uniform continuity handles small \(y\), and Gaussian concentration handles the complement. Spatial derivatives can be moved onto the Schwartz initial datum, so the same argument gives convergence of every fixed spatial derivative. Uniqueness requires an appropriate growth or norm class and is a separate assertion.

## References

- [Hunter, The Heat and Schrödinger Equations, §§5.1–5.3](https://www.math.ucdavis.edu/~hunter/pdes/ch5.pdf).
