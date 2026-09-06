+++
id = "complex-analysis/harmonic-function"
title = "Harmonic function"
kind = "definition"
summary = "A twice differentiable function annihilated by the Laplacian, equivalently a continuous function with the local mean-value property."
aliases = ["harmonicity", "solution of Laplace's equation"]
domains = ["complex-analysis", "potential-theory", "partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["topology/open-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(U\subseteq\mathbb R^n\) be open. A \(C^2\) function
\(u:U\to\mathbb R\) is **harmonic** if
\[
\Delta u=\sum_{j=1}^n\partial_{x_j}^2u=0
\]
on \(U\).

## Mean-value characterization

A continuous function is harmonic exactly when every [[topology/closed-ball|closed ball]]
\(\overline{B_r(x)}\subset U\) satisfies
\[
u(x)=\frac1{|B_r|}\int_{B_r(x)}u(y)\,dy.
\]
Equivalently, one may use averages over boundary spheres.

Because the mean-value equality gives both sub-mean inequalities, \(u\) is
harmonic exactly when both \(u\) and \(-u\) are
[[complex-analysis/subharmonic-function|subharmonic]].

## Complex-analytic source

The real and imaginary parts of a holomorphic function are harmonic. Conversely,
on a [[topology/simply-connected-space|simply connected]] planar domain, every real-valued harmonic function is
locally the real part of a holomorphic function.

## Consequences

Harmonic functions are smooth and real analytic. The
[[complex-analysis/harmonic-maximum-principle|harmonic maximum principle]]
gives uniqueness for the Dirichlet problem and controls Poisson extensions.

## References

1. Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., AMS, 2010. [Publisher record](https://bookstore.ams.org/gsm-19-r/).
