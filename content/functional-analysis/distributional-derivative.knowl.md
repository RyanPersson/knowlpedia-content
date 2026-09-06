+++
id = "functional-analysis/distributional-derivative"
title = "Distributional derivative"
kind = "definition"
summary = "The distributional derivative transfers differentiation to test functions with the sign dictated by integration by parts."
aliases = ["weak derivative of a distribution", "derivative of a distribution", "generalized derivative"]
domains = ["functional-analysis", "distribution-theory", "partial-differential-equations"]
prerequisites = ["functional-analysis/distribution", "functional-analysis/test-function-space", "real-analysis/integration-by-parts", "real-analysis/partial-derivative"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(T\) be a [[functional-analysis/distribution|distribution]] on an open
set \(\Omega\subseteq\mathbb R^n\). For a multi-index \(\alpha\), its
**distributional derivative** \(\partial^\alpha T\) is the distribution
defined by
\[
\langle\partial^\alpha T,\varphi\rangle
=(-1)^{|\alpha|}\langle T,\partial^\alpha\varphi\rangle
\]
for every \(\varphi\) in the
[[functional-analysis/test-function-space|test-function space]]. The sign is
the one forced by repeated [[real-analysis/integration-by-parts|integration by parts]]. Continuity of
\(\varphi\mapsto\partial^\alpha\varphi\) on the test-function space ensures
that \(\partial^\alpha T\) is again a distribution. For \(|\alpha|=1\), this
extends the classical [[real-analysis/partial-derivative|partial derivative]].

## Agreement with classical differentiation

If \(f\) is continuously differentiable and \(T_f\) is the distribution
induced by \(f\), integration by parts gives
\[
\partial_jT_f=T_{\partial_jf}.
\]
No boundary term appears because test functions have compact support inside
\(\Omega\). Hence the generalized definition does not alter classical
derivatives where those derivatives exist.

## Singular derivatives

Distributional differentiation can detect jumps. On \(\mathbb R\), the
Heaviside function \(H\) defines a regular distribution and satisfies
\(H'=\delta_0\). More generally, differentiating a piecewise smooth function
produces its ordinary derivative away from jumps together with delta terms
whose coefficients are the jump sizes.

## Algebraic properties

Distributional derivatives are linear, commute with one another, and exist
to every order for every distribution. If \(a\) is smooth, the product rule
\[
\partial_j(aT)=(\partial_ja)T+a\,\partial_jT
\]
holds. These properties let differential operators with smooth coefficients
act on distributions without requiring pointwise differentiability.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: §2.1 on differentiation of distributions.
2. F. G. Friedlander and M. Joshi, *Introduction to the Theory of Distributions*, 2nd ed., Cambridge University Press, 1998. [Publisher record](https://www.cambridge.org/core/books/introduction-to-the-theory-of-distributions/05AEF06472B80BEF6677036D47A6D308). Relevant: Chapter 2 on operations on distributions.
