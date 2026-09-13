+++
id = "real-analysis/real-power"
title = "Real power of a positive number"
kind = "definition"
summary = "The definition x^a = exp(a log x) for x > 0 and real a."
aliases = ["power law", "power function", "fractional power"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/exponential-function", "real-analysis/natural-logarithm", "real-analysis/chain-rule"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(x>0\) and \(a\in\mathbb R\), the **real power** is
\[
x^a=\exp(a\log x).
\]
This agrees with integer powers and satisfies \(x^{a+b}=x^a x^b\), \((xy)^a=x^ay^a\) for positive \(x,y\), and
\[
\frac{d}{dx}x^a=ax^{a-1}.
\]
The definition uses the real [[real-analysis/natural-logarithm|logarithm]]; negative bases do not admit this definition for arbitrary real exponents.

## Endpoints and parameters

For \(a>0\), setting \(0^a=0\) gives a continuous extension to zero. Smoothness at zero depends on \(a\). Differentiating the exponent instead gives \(\partial_a x^a=x^a\log x\), explaining logarithmic factors when a power-law exponent varies.

## References

- [John K. Hunter, Introduction to Analysis, Chapter 10: Power Series](https://www.math.ucdavis.edu/~hunter/intro_analysis_pdf/ch10.pdf).
