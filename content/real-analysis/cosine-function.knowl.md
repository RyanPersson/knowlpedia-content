+++
id = "real-analysis/cosine-function"
title = "Cosine function"
kind = "definition"
summary = "The even trigonometric function defined by its entire power series."
aliases = ["cosine", "cos"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/power-series", "shared-foundations/factorial"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **cosine function** is
\[
\cos x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!}.
\]
The [[real-analysis/power-series|power series]] converges for all real \(x\), is even, and gives \(\cos0=1\).

## Derivative

Termwise differentiation gives \(\cos' x=-\sin x\), where [[real-analysis/sine-function|sine]] is given by its companion odd series.

## Rotation

The addition formulas imply that
\[
\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}
\]
is an orthogonal matrix, and multiplying the matrices for two angles adds their angles. Together with sine, cosine has period \(2\pi\); this fixes the radian angle convention used in polar and cylindrical coordinates.

## References

- [John K. Hunter, Introduction to Analysis, Chapter 10: Power Series](https://www.math.ucdavis.edu/~hunter/intro_analysis_pdf/ch10.pdf).
