+++
id = "complex-analysis/subharmonic-function"
title = "Subharmonic function"
kind = "definition"
summary = "An upper-semicontinuous function dominated at each point by its local spherical averages."
aliases = ["subharmonicity", "SH function"]
domains = ["complex-analysis", "potential-theory", "partial-differential-equations"]
section_mode = "progressive"
+++

Let \(U\subseteq\mathbb R^m\) be open. A function
\(u:U\to[-\infty,\infty)\), not identically \(-\infty\) on any connected
component, is **subharmonic** if it is
[[complex-analysis/upper-semicontinuous-function|upper-semicontinuous]] and
\[
u(x)\le \frac{1}{|S^{m-1}|}\int_{S^{m-1}}u(x+r\omega)\,d\omega
\]
whenever the [[topology/closed-ball|closed ball]]
\(\overline{B_r(x)}\) lies in \(U\). For \(m=2\), after identifying
\(\mathbb R^2\cong\mathbb C\), this is the usual circular sub-mean
inequality.

## Distributional characterization

If \(u\in L^1_{\mathrm{loc}}(U)\), subharmonicity is equivalent to
\(\Delta u\ge0\) in the [[functional-analysis/distribution|distributional]]
sense. For \(u\in C^2\), this becomes the pointwise inequality
\(\Delta u\ge0\).

## Examples

[[complex-analysis/harmonic-function|Harmonic functions]] satisfy equality in
the mean-value formula and are subharmonic. Every convex function on a convex
open set is subharmonic. If \(f\) is holomorphic, then
[[complex-analysis/log-modulus-subharmonic|\(\log|f|\) is subharmonic]], with
its distributional Laplacian recording the zeros of \(f\).

## References

1. Thomas Ransford, *Potential Theory in the Complex Plane*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511623776).
2. David H. Armitage and Stephen J. Gardiner, *Classical Potential Theory*, Springer, 2001. [DOI record](https://doi.org/10.1007/978-1-4471-0233-5).
