+++
id = "real-analysis/sine-function"
title = "Sine function"
kind = "definition"
summary = "The odd trigonometric function defined by its entire power series."
aliases = ["sine", "sin"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/power-series", "shared-foundations/factorial"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **sine function** is defined analytically by the everywhere convergent [[real-analysis/power-series|power series]]
\[
\sin x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{(2n+1)!}.
\]
## Identities

It is odd, satisfies \(\sin0=0\), and its derivative is the [[real-analysis/cosine-function|cosine]]. The two series give \(\sin^2x+\cos^2x=1\) and the addition formulas.

## Angle convention

The positive number \(\pi\) is the smallest positive zero of sine; the usual trigonometric identities give period \(2\pi\) for sine and cosine. With angles measured in radians, \((\cos\theta,\sin\theta)\) parametrizes the unit circle. Existence of this first zero and the periodicity follow from the addition formulas and continuity; they are properties of the series-defined functions rather than extra choices of scale.

## Derivatives

Termwise differentiation yields \(\sin''x=-\sin x\), so the function is smooth and solves this second-order equation with initial values \(\sin0=0\), \(\sin'0=1\).

## References

- [John K. Hunter, Introduction to Analysis, Chapter 10: Power Series](https://www.math.ucdavis.edu/~hunter/intro_analysis_pdf/ch10.pdf).
