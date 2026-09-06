+++
id = "complex-analysis/entire-function-several-variables"
title = "Entire function of several complex variables"
kind = "definition"
summary = "A complex-valued function holomorphic on all of complex Euclidean space."
aliases = ["entire function on C^d", "entire holomorphic function of several variables"]
domains = ["complex-analysis", "several-complex-variables"]
prerequisites = ["real-analysis/power-series", "complex-analysis/analytic-continuation"]
dependency_review_count = 1
section_mode = "progressive"
+++

An **entire function of \(d\) complex variables** is a function
\(F:\mathbb C^d\to\mathbb C\) that is holomorphic at every point. Equivalently,
near every point it has a [[real-analysis/power-series|convergent power series]] in \(d\) variables; by
[[complex-analysis/analytic-continuation|analytic continuation]] the Taylor series about any point has a domain of
convergence covering all of \(\mathbb C^d\).

## Relation to complex lines

An entire function restricts to an [[complex-analysis/entire-function|entire
function of one variable]] on every affine complex line. Conversely, a
locally bounded function whose restriction to every complex line is
holomorphic is holomorphic on \(\mathbb C^d\).

For the Taylor claim, Cauchy's coefficient estimates on an arbitrary finite polydisc bound each coefficient by the supremum divided by the corresponding radii. Since the radii are arbitrary, the resulting multiple series converges at every point. The converse is Hartogs' line theorem: local boundedness and line holomorphy supply a joint power series on each coordinate polydisc.

## Exponential type

Growth conditions of the form
\( |F(x+iy)|\le A e^{\sigma|y|}\) encode
[[harmonic-analysis/bounded-fourier-support|bounded Fourier support]] of the
restriction \(F|_{\mathbb R^d}\) through the
[[harmonic-analysis/paley-wiener-bounded-fourier-support|Paley–Wiener theorem]].

## References

1. Steven G. Krantz, *Function Theory of Several Complex Variables*, 2nd ed., AMS Chelsea, 2001. [Publisher record](https://bookstore.ams.org/chel-340-h/).
