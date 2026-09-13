+++
id = "real-analysis/exponential-function"
title = "Exponential function"
kind = "definition"
summary = "The real function exp(x) defined by the everywhere convergent series sum x^n/n!."
aliases = ["exponential", "exp", "exponential growth", "exponential decay"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/power-series", "shared-foundations/factorial", "real-analysis/derivative"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **exponential function** is
\[
\exp(x)=e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!},\qquad x\in\mathbb R.
\]
This [[real-analysis/power-series|power series]] has infinite radius of convergence. Termwise differentiation gives \(\exp'(x)=\exp(x)\) and \(\exp(0)=1\). Multiplication of absolutely convergent series gives
\[
\exp(x+y)=\exp(x)\exp(y).
\]
Consequently \(\exp(x)>0\), \(\exp(-x)=1/\exp(x)\), and \(\exp\) is strictly increasing from \(\mathbb R\) onto \((0,\infty)\).

## Growth and decay

For every nonnegative integer \(m\), \(x^m e^{-x}\to0\) as \(x\to+\infty\). Indeed, positivity of the series gives \(e^x\ge x^{m+1}/(m+1)!\) for \(x>0\). This estimate is a basic source of functions vanishing to every order at an endpoint after replacing \(x\) by a reciprocal distance.

## References

- [John K. Hunter, Introduction to Analysis, Chapter 10: Power Series](https://www.math.ucdavis.edu/~hunter/intro_analysis_pdf/ch10.pdf).
