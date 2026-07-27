+++
id = "functional-analysis/fourier-transform-tempered-distributions"
title = "Fourier transform of tempered distributions"
kind = "definition"
summary = "The Fourier transform of a tempered distribution is defined by transposing the Fourier automorphism of Schwartz space."
aliases = ["distributional Fourier transform", "Fourier transform on S-prime"]
domains = ["functional-analysis", "harmonic-analysis", "distribution-theory"]
section_mode = "progressive"
+++

Let \(u\) be a [[functional-analysis/tempered-distribution|tempered
distribution]] on \(\mathbb R^n\). Its **Fourier transform**
\(\widehat u\) is the tempered distribution defined by
\[
\langle\widehat u,\varphi\rangle
=\langle u,\widehat\varphi\rangle
\qquad
\text{for every }\varphi\in\mathcal S(\mathbb R^n),
\]
where \(\varphi\mapsto\widehat\varphi\) is the
[[functional-analysis/fourier-transform-schwartz-space|Fourier transform on
Schwartz space]] with kernel \(e^{-2\pi i x\cdot\xi}\). Because that transform
is a continuous automorphism of \(\mathcal S(\mathbb R^n)\), this transpose
operation is well-defined and is itself a linear automorphism of
\(\mathcal S'(\mathbb R^n)\).

## Compatibility with functions

If \(u\) is induced by an integrable function \(f\), Fubini's theorem gives
\[
\langle\widehat u,\varphi\rangle
=\int_{\mathbb R^n}\widehat f(\xi)\varphi(\xi)\,d\xi.
\]
Thus the dual definition agrees with the ordinary Fourier transform whenever
both are available. It also assigns transforms to nonintegrable objects such
as polynomials, plane waves, and derivatives of the Dirac distribution
[Hörmander, §7.1](https://doi.org/10.1007/978-3-642-61497-2).

## Differentiation and multiplication

With the displayed normalization,
\[
\widehat{\partial^\alpha u}(\xi)
=(2\pi i\xi)^\alpha\widehat u(\xi),
\qquad
\widehat{x^\alpha u}(\xi)
=\left(-\frac{1}{2\pi i}\right)^{|\alpha|}
\partial^\alpha\widehat u(\xi).
\]
These identities hold distributionally. They turn constant-coefficient
differential equations into algebraic multiplication equations and are a
principal reason for working in \(\mathcal S'\).

## Conventions and scope

**Warning.** Some authors define the distributional Fourier transform using
\(\langle\widehat u,\varphi\rangle=\langle u,\widecheck\varphi\rangle\);
their test-function transform, pairing convention, or sign in the exponential
then differs. A convention must be checked before transferring formulas for
signs and powers of \(2\pi\).

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: §7.1 on Fourier transformation of distributions.
2. Robert S. Strichartz, *A Guide to Distribution Theory and Fourier Transforms*, CRC Press, 1994. [Publisher record](https://www.routledge.com/A-Guide-to-Distribution-Theory-and-Fourier-Transforms/Strichartz/p/book/9780849382734). Relevant: chapters on tempered distributions and their Fourier transforms.
