+++
id = "functional-analysis/distribution"
title = "Distribution"
kind = "definition"
summary = "A distribution on an open Euclidean set is a continuous linear functional on its space of compactly supported smooth test functions."
aliases = ["generalized function", "continuous linear functional on test functions", "Schwartz distribution", "Distribution (generalized function)"]
domains = ["functional-analysis"]
prerequisites = ["functional-analysis/topological-dual", "functional-analysis/test-function-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\Omega\subseteq\mathbb R^n\) be open and let \(\mathcal D(\Omega)=C_c^\infty(\Omega)\) carry its canonical locally convex topology. A **distribution** on \(\Omega\) is a continuous linear functional
\[
T:\mathcal D(\Omega)\to\mathbb C.
\]
Thus the space of distributions, denoted \(\mathcal D'(\Omega)\), is the [[functional-analysis/topological-dual|topological dual]] of the [[functional-analysis/test-function-space|test-function space]]. Continuity means that on functions supported in each fixed compact \(K\subset\Omega\), \(T\) is bounded by finitely many uniform derivative seminorms. This continuity condition distinguishes distributions from arbitrary algebraic linear functionals.

## Regular and singular examples

Every \(f\in L^1_{\mathrm{loc}}(\Omega)\) defines a regular distribution by
\[
T_f(\varphi)=\int_\Omega f(x)\varphi(x)\,dx.
\]
The Dirac distribution \(\delta_a(\varphi)=\varphi(a)\) for \(a\in\Omega\) is singular: it cannot be represented by a locally integrable function. Both satisfy the same continuity requirement.

## Differentiation and support

For a multi-index \(\alpha\), the [[functional-analysis/distributional-derivative|distributional derivative]] is defined by
\[
\langle \partial^\alpha T,\varphi\rangle=(-1)^{|\alpha|}\langle T,\partial^\alpha\varphi\rangle.
\]
This integration-by-parts definition makes every distribution infinitely differentiable in the distributional sense. The support of \(T\) is the complement of the largest open set on which \(T\) vanishes on all test functions.

## Conventions and scope

**Warning.** A Schwartz distribution is a distribution in this sense, not a probability distribution. A [[functional-analysis/tempered-distribution|tempered distribution]] is more restrictive: it acts continuously on [[functional-analysis/schwartz-space|Schwartz space]] rather than merely on compactly supported test functions. Complex distribution theory usually takes \(T\) to be complex-linear; some functional-analytic conventions instead use conjugate-linear duals and must adjust pairings accordingly.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd edition, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: chapters 1–3 on test functions, distributions, and differentiation.
2. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967; Dover reprint, 2006. [Publisher record](https://store.doverpublications.com/products/9780486453521). Relevant: chapters on test-function spaces and distributions.
