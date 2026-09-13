+++
id = "real-analysis/natural-logarithm"
title = "Natural logarithm"
kind = "definition"
summary = "The inverse of the real exponential on the positive real axis."
aliases = ["logarithm", "log", "ln"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/exponential-function", "shared-foundations/inverse-function", "real-analysis/inverse-function-theorem-1d"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **natural logarithm** is the inverse of the [[real-analysis/exponential-function|exponential function]]:
\[
\log:(0,\infty)\longrightarrow\mathbb R,
\qquad \exp(\log x)=x.
\]
It is strictly increasing and satisfies
\[
\log 1=0,\qquad \log(xy)=\log x+\log y,
\qquad \frac{d}{dx}\log x=\frac1x.
\]
The derivative formula follows from the [[real-analysis/inverse-function-theorem-1d|inverse function theorem]] or by differentiating \(\exp(\log x)=x\).

## Domain

This real logarithm is defined only for positive inputs. A logarithm of a nonzero complex number requires a branch choice on an appropriate domain; a global single-valued complex logarithm cannot simply be assumed.

## References

- [John K. Hunter, Introduction to Analysis, Chapter 10: Power Series](https://www.math.ucdavis.edu/~hunter/intro_analysis_pdf/ch10.pdf).
