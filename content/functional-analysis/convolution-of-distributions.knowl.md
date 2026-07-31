+++
id = "functional-analysis/convolution-of-distributions"
title = "Convolution of distributions"
kind = "definition"
summary = "Distributional convolution extends ordinary convolution under support hypotheses and includes convolution with test functions."
aliases = ["distribution convolution", "convolution with a distribution", "distributional convolution", "convolution with a compactly supported distribution"]
domains = ["functional-analysis", "distribution-theory", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(S,T\in\mathcal D'(\mathbb R^n)\) be
[[functional-analysis/distribution|distributions]], with at least one of them
[[functional-analysis/compactly-supported-distribution|compactly supported]].
Their **convolution** \(S*T\) is the distribution defined by
\[
\langle S*T,\varphi\rangle
=\big\langle S_x,\langle T_y,\varphi(x+y)\rangle\big\rangle,
\qquad
\varphi\in C_c^\infty(\mathbb R^n).
\]
The support hypothesis makes the iterated pairing well defined. For arbitrary
\(T\) and a [[functional-analysis/test-function-space|test function]]
\(\psi\), convolution is always defined by
\[
(T*\psi)(x)=\langle T_y,\psi(x-y)\rangle,
\]
and produces a smooth function. Both constructions extend classical
convolution of functions and are independent of which factor is evaluated
first whenever the distributional convolution exists.

## Smoothing and differentiation

Convolution with a test function regularizes a distribution:
\(T*\psi\in C^\infty(\mathbb R^n)\), and derivatives may be moved between the
factors,
\[
\partial^\alpha(T*\psi)
=(\partial^\alpha T)*\psi
=T*(\partial^\alpha\psi).
\]
This identity underlies mollification and the use of fundamental solutions.
When both distributions have compact support, convolution is associative and
commutative and remains compactly supported
[Hörmander, §4.2].

## Support and standard examples

Whenever the convolution is defined,
\[
\operatorname{supp}(S*T)
\subseteq\operatorname{supp}S+\operatorname{supp}T,
\]
where the right side is the Minkowski sum. The Dirac distribution is the
identity: \(\delta_0*T=T\), and
\(\delta_a*T\) translates \(T\). If \(f\) and \(g\) are locally integrable
functions and their classical convolution is meaningful, their regular
distributions have the same distributional convolution.

## Broader support conditions

**Warning.** Two arbitrary distributions cannot always be convolved. A more
general sufficient condition is that addition
\((x,y)\mapsto x+y\) be proper on
\(\operatorname{supp}S\times\operatorname{supp}T\); compact support of one
factor is the standard easy case. On a
[[topology/locally-compact-group|locally compact group]], inversion,
[[harmonic-analysis/haar-measure|Haar measure]], and possibly modular factors
enter the corresponding
[[harmonic-analysis/convolution-on-locally-compact-group|group convolution]]
formula.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: §4.2, convolution of distributions and support conditions.
2. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967. [Publisher record](https://shop.elsevier.com/books/topological-vector-spaces-distributions-and-kernels/treves/978-1-4831-9859-0). Relevant: Chapter 27, convolution of distributions.
