+++
id = "functional-analysis/fourier-transform-schwartz-space"
title = "Fourier transform on Schwartz space"
kind = "definition"
summary = "The Fourier transform restricts to a continuous linear automorphism of the Schwartz space."
aliases = ["Schwartz Fourier transform", "Fourier automorphism of S(R^n)", "Fourier automorphism of S"]
domains = ["functional-analysis", "harmonic-analysis"]
section_mode = "progressive"
+++

For \(f\) in the [[functional-analysis/schwartz-space|Schwartz space]]
\(\mathcal S(\mathbb R^n)\), its **Fourier transform** is
\[
\widehat f(\xi)=\int_{\mathbb R^n}e^{-2\pi i x\cdot\xi}f(x)\,dx .
\]
The integral is a [[measure-theory/lebesgue-integral|Lebesgue integral]];
rapid decay makes \(f\) [[measure-theory/lebesgue-integrable-function|Lebesgue
integrable]]. The map
\(\mathcal F:f\mapsto\widehat f\) is a continuous linear bijection
\(\mathcal S(\mathbb R^n)\to\mathcal S(\mathbb R^n)\) whose inverse is
continuous. This topological automorphism, with the displayed normalization,
is the **Fourier transform on Schwartz space**.

## Why Schwartz space is preserved

Differentiation under the integral and [[real-analysis/integration-by-parts|integration by parts]] exchange
derivatives with polynomial factors:
\[
\partial_\xi^\alpha\widehat f(\xi)
=\widehat{(-2\pi i x)^\alpha f}(\xi),
\qquad
(2\pi i\xi)^\beta\widehat f(\xi)
=\widehat{\partial^\beta f}(\xi).
\]
Every polynomially weighted derivative of \(f\) remains integrable, so these
identities bound every Schwartz seminorm of \(\widehat f\). They also show
continuity of \(\mathcal F\) in the Schwartz topology
[Hörmander, §7.1](https://doi.org/10.1007/978-3-642-61497-2).

## Structural role

Fourier transformation converts constant-coefficient differentiation into
multiplication by a polynomial and translation into modulation. Its
automorphism property therefore makes \(\mathcal S(\mathbb R^n)\) a common
invariant domain for both operations. Taking the transpose of this
automorphism defines the
[[functional-analysis/fourier-transform-tempered-distributions|Fourier
transform of tempered distributions]].

## Conventions and scope

**Warning.** Other standard normalizations place no \(2\pi\) in the
exponential or distribute powers of \(2\pi\) between the transform and its
inverse. Those choices change the displayed differentiation formulas but not
the assertion that the Fourier transform is a topological automorphism of
\(\mathcal S(\mathbb R^n)\).

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: §7.1 on the Fourier transform on Schwartz space.
2. Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction*, Princeton University Press, 2003. [DOI record](https://doi.org/10.1515/9781400831234). Relevant: Chapters 5–6 on the Fourier transform and Schwartz functions.
