+++
id = "functional-analysis/regular-tempered-distribution"
title = "Regular tempered distribution"
kind = "definition"
summary = "A regular tempered distribution is a tempered distribution represented by integration against a locally integrable function."
aliases = ["tempered distribution induced by a function", "slow-growth function as a distribution"]
domains = ["functional-analysis", "distribution-theory", "harmonic-analysis"]
prerequisites = ["functional-analysis/tempered-distribution", "functional-analysis/schwartz-space", "measure-theory/lebesgue-integrable-function", "topology/compact-set", "measure-theory/almost-everywhere"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **regular tempered distribution** on \(\mathbb R^n\) is a
[[functional-analysis/tempered-distribution|tempered distribution]] \(T_f\)
for which there is a locally integrable function \(f\) satisfying
\[
\langle T_f,\varphi\rangle
=\int_{\mathbb R^n}f(x)\varphi(x)\,dx
\qquad
\text{for every }\varphi\in\mathcal S(\mathbb R^n).
\]
Here \(\varphi\) ranges over the
[[functional-analysis/schwartz-space|Schwartz space]], and local integrability
means that \(f\) is
[[measure-theory/lebesgue-integrable-function|Lebesgue integrable]] on every
[[topology/compact-set|compact set]]. In addition, the displayed integral must be absolutely
convergent for every Schwartz function and must depend continuously on
\(\varphi\) in the Schwartz topology. Functions equal [[measure-theory/almost-everywhere|almost everywhere]]
determine the same regular tempered distribution.

## Sufficient growth conditions

If \(f\in L^1_{\mathrm{loc}}(\mathbb R^n)\) and
\[
|f(x)|\leq C(1+|x|)^N
\]
almost everywhere for some \(C,N\), then \(f\) defines a regular tempered
distribution. More generally, it suffices that the integral of \(|f|\) over
balls grow at most polynomially. Pointwise polynomial growth is therefore a
convenient sufficient condition, not the definition.

## Examples

Every function in
[[measure-theory/lp-space|\(L^p(\mathbb R^n)\)]] for
\(1\leq p\leq\infty\) defines a regular tempered distribution by
[[convex-analysis/holder-inequality-integrals|Hölder's inequality]], since
Schwartz functions belong to the conjugate \(L^q\) space. Polynomials and
bounded [[measure-theory/measurable-function|measurable functions]] give further examples. A function such as
\(e^{|x|}\) generally fails because multiplication by a Schwartz function
need not be integrable.

## Regular versus singular

The adjective **regular** refers to representation by a function, not to
smoothness of that function. The Dirac delta and its derivatives are
tempered but not regular, since no locally integrable function represents
point evaluation on all [[functional-analysis/test-function-space|test functions]]. Regular distributions are therefore
a proper subclass of tempered distributions.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: §§2.1 and 7.1 on regular and tempered distributions.
2. Robert S. Strichartz, *A Guide to Distribution Theory and Fourier Transforms*, CRC Press, 1994. [Publisher record](https://www.routledge.com/A-Guide-to-Distribution-Theory-and-Fourier-Transforms/Strichartz/p/book/9780849382734). Relevant: introductory examples of distributions and tempered distributions.
