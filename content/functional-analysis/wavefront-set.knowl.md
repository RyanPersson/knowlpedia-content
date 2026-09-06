+++
id = "functional-analysis/wavefront-set"
title = "Wavefront set"
kind = "definition"
summary = "The wavefront set records the points and nonzero cotangent directions in which a distribution is not microlocally smooth."
aliases = ["microlocal singular support", "Hörmander wavefront set"]
domains = ["functional-analysis", "distribution-theory", "microlocal-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/distribution", "functional-analysis/compactly-supported-distribution", "functional-analysis/fourier-transform-tempered-distributions"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T\in\mathcal D'(\Omega)\) be a
[[functional-analysis/distribution|distribution]], where
\(\Omega\subseteq\mathbb R^n\) is open. A pair
\((x_0,\xi_0)\in\Omega\times(\mathbb R^n\setminus\{0\})\) is absent from the
**wavefront set** \(\operatorname{WF}(T)\) if some
\(\chi\in C_c^\infty(\Omega)\), with \(\chi(x_0)\ne0\), and some open conic
neighborhood \(\Gamma\) of \(\xi_0\) satisfy the following condition. The
product \(\chi T\) is a
[[functional-analysis/compactly-supported-distribution|compactly supported
distribution]], hence tempered, and its
[[functional-analysis/fourier-transform-tempered-distributions|distributional
Fourier transform]] obeys
\[
\sup_{\xi\in\Gamma}(1+\lVert\xi\rVert)^N
\lvert\widehat{\chi T}(\xi)\rvert<\infty
\quad\text{for every }N\geq0.
\]
Thus \(\operatorname{WF}(T)\) records where the localized transform fails to
decay rapidly. It is a closed conic subset of \(T^*\Omega\setminus0\), and
different qualifying cutoffs give the same exclusion criterion.

## Relation to singular support

The base projection of \(\operatorname{WF}(T)\) is exactly the
[[functional-analysis/singular-support|singular support]] of \(T\). A point
may therefore be singular while only some cotangent directions above it are
in the wavefront set. The definition uses the
[[functional-analysis/fourier-transform-tempered-distributions|Fourier transform of a tempered distribution]] because \(\chi T\) has compact support
and hence is tempered.

## Behavior under operations

Differentiation and multiplication by smooth functions do not create new
wavefront directions:
\[
\operatorname{WF}(\partial^\alpha T)\subseteq\operatorname{WF}(T),
\qquad
\operatorname{WF}(aT)\subseteq\operatorname{WF}(T).
\]
More delicate transversality conditions on wavefront sets govern whether
products and pullbacks of distributions exist. Wavefront sets also transform
naturally under diffeomorphisms.

## Examples and geometric meaning

A smooth function has empty wavefront set. For the Dirac distribution at the
origin,
\[
\operatorname{WF}(\delta_0)
=\{(0,\xi):\xi\ne0\},
\]
so every nonzero cotangent direction is singular. A distribution conormal to
a smooth hypersurface instead has wavefront directions normal to that
hypersurface, illustrating that the construction detects direction as well as
location.

## Conventions and scope

**Warning.** The zero covector is excluded, and conic means invariance under
positive rescaling in the covector variable. Some Fourier-transform
conventions reverse the sign of covectors; internal formulas must use one
convention consistently. On a [[fiber-bundles/smooth-manifold|smooth manifold]] the chartwise definitions patch to an intrinsic subset of the
punctured [[fiber-bundles/cotangent-bundle|cotangent bundle]].

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: Chapter 8, definition and calculus of wavefront sets.
2. J. J. Duistermaat, *Fourier Integral Operators*, Birkhäuser, 1996. [DOI record](https://doi.org/10.1007/978-1-4612-0301-5). Relevant: Chapter I, wavefront sets and microlocal operations.
