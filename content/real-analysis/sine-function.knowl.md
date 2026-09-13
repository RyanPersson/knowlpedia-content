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

The constant [[real-analysis/pi|π]] is the least positive zero of sine and fixes its radian angle convention. With this scale, \( (\cos\theta,\sin\theta)\) parametrizes the unit circle and has period \(2\pi\).

## Derivatives

Termwise differentiation yields \(\sin''x=-\sin x\), so the function is smooth and solves this second-order equation with initial values \(\sin0=0\), \(\sin'0=1\).

## References

- [John K. Hunter, Introduction to Analysis, Chapter 10: Power Series](https://www.math.ucdavis.edu/~hunter/intro_analysis_pdf/ch10.pdf).
