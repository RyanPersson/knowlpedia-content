+++
id = "functional-analysis/singular-support"
title = "Singular support of a distribution"
kind = "definition"
summary = "The singular support records the points near which a distribution cannot be represented by a smooth function."
aliases = ["singular support", "distributional singular locus"]
domains = ["functional-analysis", "distribution-theory"]
section_mode = "progressive"
prerequisites = ["functional-analysis/distribution", "functional-analysis/test-function-space", "functional-analysis/support-of-distribution"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T\) be a [[functional-analysis/distribution|distribution]] on an open set
\(\Omega\subseteq\mathbb R^n\). A point \(x\in\Omega\) is **regular for
\(T\)** if some neighborhood \(U\) of \(x\) and some
\(f\in C^\infty(U)\) satisfy
\[
\langle T,\varphi\rangle=\int_U f(y)\varphi(y)\,dy
\]
for every [[functional-analysis/test-function-space|test function]]
\(\varphi\) supported in \(U\). The **singular
support** \(\operatorname{singsupp}T\) is the complement in \(\Omega\) of
the set of regular points. It is a relatively closed subset of the
[[functional-analysis/support-of-distribution|support of \(T\)]] and records
where \(T\) fails to be locally a smooth function. This definition depends
only on the restriction of \(T\) to arbitrarily small neighborhoods.

## Local character and basic operations

Regularity is local, so \(T\) is induced by a smooth function precisely when
\(\operatorname{singsupp}T=\varnothing\). Multiplication by a smooth function
and distributional differentiation satisfy
\[
\operatorname{singsupp}(aT)\subseteq\operatorname{singsupp}T,
\qquad
\operatorname{singsupp}(\partial^\alpha T)
\subseteq\operatorname{singsupp}T.
\]
Either inclusion may be strict: multiplication can cancel a singularity, and
differentiation in a direction along which a singular distribution is
invariant can annihilate it.

## Examples and relation to wavefront set

A smooth function, regarded as a regular distribution, has empty singular
support. The Dirac distribution \(\delta_a\) and all its nonzero derivatives
have singular support \(\{a\}\). A piecewise smooth function has singular
support contained in the locus where its smooth pieces fail to fit smoothly.

The [[functional-analysis/wavefront-set|wavefront set]] refines singular
support by retaining cotangent directions: the projection of
\(\operatorname{WF}(T)\) to \(\Omega\) is
\(\operatorname{singsupp}T\).

## Conventions and scope

**Warning.** Singular support is not the set-theoretic support. A smooth
compactly supported function can have large support and empty singular
support. Conversely, a distribution supported at one point is singular there
unless it is zero. For distributions on a manifold, the definition is made in
charts; smooth coordinate changes preserve it.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: Chapter 2, support, local regularity, and singular support of distributions.
2. Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed., Wiley, 1999. [Publisher record](https://www.wiley.com/en-us/Real+Analysis%3A+Modern+Techniques+and+Their+Applications%2C+2nd+Edition-p-9780471317166). Relevant: Chapter 9, distributions and their local behavior.
