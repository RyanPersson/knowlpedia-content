+++
id = "functional-analysis/tempered-distribution"
title = "Tempered distribution"
kind = "definition"
summary = "A continuous linear functional on the Schwartz space of rapidly decreasing smooth functions."
aliases = ["S-prime", "continuous functional on Schwartz space", "space S-prime", "distribution of slow growth"]
domains = ["functional-analysis", "distribution-theory", "harmonic-analysis"]
prerequisites = ["functional-analysis/schwartz-space", "functional-analysis/topological-dual", "functional-analysis/test-function-space", "functional-analysis/distribution"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **tempered distribution** on \(\mathbb R^n\) is a continuous linear
functional on the
[[functional-analysis/schwartz-space|Schwartz space]]
\(\mathcal S(\mathbb R^n)\). The space of all tempered distributions is the
[[functional-analysis/topological-dual|topological dual]]
\[
\mathcal S'(\mathbb R^n)
=\mathcal L_{\mathrm{cont}}(\mathcal S(\mathbb R^n),\mathbb C).
\]
Equivalently, \(u\in\mathcal S'(\mathbb R^n)\) when there are \(C>0\) and an
integer \(N\) such that
\[
|u(\varphi)|
\leq C\sum_{|\alpha|,|\beta|\leq N}
\sup_{x\in\mathbb R^n}|x^\alpha\partial^\beta\varphi(x)|
\]
for every \(\varphi\in\mathcal S(\mathbb R^n)\). Restriction to compactly
supported [[functional-analysis/test-function-space|test functions]] makes every tempered distribution a
[[functional-analysis/distribution|distribution]], but not every
distribution is tempered.

## Examples and nonexamples

Every polynomially bounded locally integrable function defines a tempered
distribution by integration against Schwartz functions. Finite measures,
polynomials, the Dirac delta, and derivatives of the Dirac delta are
tempered. By contrast, a locally integrable function with sufficiently rapid
exponential growth need not define a functional on all of
\(\mathcal S(\mathbb R^n)\).

## Stable operations

Tempered distributions are closed under distributional differentiation and
under multiplication by polynomials. Translation and multiplication by
smooth functions whose derivatives grow at most polynomially also act
continuously. These stability properties explain why \(\mathcal S'\) is a
natural setting for constant-coefficient differential equations.

## Fourier duality and topology

The
[[functional-analysis/fourier-transform-schwartz-space|Fourier transform]]
is an automorphism of \(\mathcal S(\mathbb R^n)\), so it extends to
\(\mathcal S'(\mathbb R^n)\) by duality. This extension includes objects such
as plane waves and delta distributions that are not integrable functions.
The notation \(\mathcal S'\) specifies the continuous dual as a [[linear-algebra/vector-space|vector space]];
when convergence of tempered distributions is discussed, one must
additionally specify the weak-star or [[functional-analysis/strong-dual|strong dual topology]].

## References

- [Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Chapter 7 (Springer, 2003)](https://doi.org/10.1007/978-3-642-61497-2)
- [Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed., Chapter 9 (Wiley, 1999)](https://www.wiley.com/en-us/Real+Analysis%3A+Modern+Techniques+and+Their+Applications%2C+2nd+Edition-p-9780471317166)
