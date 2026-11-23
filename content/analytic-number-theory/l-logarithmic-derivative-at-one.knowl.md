+++
id = "analytic-number-theory/l-logarithmic-derivative-at-one"
title = "Logarithmic derivative of a Dirichlet L-function at one"
kind = "definition"
summary = "The finite value L′(1,χ)/L(1,χ) for a nonprincipal Dirichlet character."
aliases = ["L′/L(1)", "logarithmic derivative at one"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-l-function", "complex-analysis/logarithmic-derivative"]
+++

For a nonprincipal [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\), the notation \(L'/L(1,\chi)\) means \(L'(1,\chi)/L(1,\chi)\). It is the [[complex-analysis/logarithmic-derivative|logarithmic derivative]] with respect to \(s\), evaluated at \(s=1\). Dirichlet’s nonvanishing theorem gives \(L(1,\chi)\ne0\).

## How primes enter

Logarithmically differentiating the Euler product in its half-plane of absolute convergence gives
\[
-\frac{L'}{L}(s,\chi)=\sum_{n\ge1}\Lambda(n)\chi(n)n^{-s},\qquad \operatorname{Re}s>1.
\]
Evaluation at \(1\) uses the analytic function there. For the principal character \(L(s,\chi)\) has a pole at \(1\) and the corresponding [[analytic-number-theory/centered-prime-sum|centering term]] has a different form.

## References

- Kiran Kedlaya, [Notes on analytic number theory, §3.4, nonvanishing at one](https://kskedlaya.org/ant/chap-lfunc.html).
- NIST Digital Library of Mathematical Functions, [§25.15(i), Dirichlet series and Euler product](https://dlmf.nist.gov/25.15).
