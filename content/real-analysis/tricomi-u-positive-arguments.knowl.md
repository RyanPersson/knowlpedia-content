+++
id = "real-analysis/tricomi-u-positive-arguments"
title = "Tricomi U for positive real arguments"
kind = "definition"
summary = "A convergent Laplace integral defining a confluent hypergeometric function on a positive real domain."
aliases = ["Tricomi confluent hypergeometric function", "Tricomi U integral"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/gamma-function", "real-analysis/exponential-function", "real-analysis/real-power", "measure-theory/lebesgue-integral"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For \(a>0\), \(b\in\mathbb R\), and \(z>0\), the **Tricomi confluent hypergeometric function** is represented by
\[
U(a,b,z)=\frac1{\Gamma(a)}\int_0^\infty
e^{-zt}t^{a-1}(1+t)^{b-a-1}\,dt.
\]
The [[real-analysis/gamma-function|Gamma factor]] fixes its normalization. The positive integrand is integrable at zero and infinity in this domain.

## Differential equation

Differentiating under the integral and integrating the derivative of \(e^{-zt}t^a(1+t)^{b-a}\) shows
\[
zU_{zz}+(b-z)U_z-aU=0.
\]
Both boundary terms vanish. This real integral domain suffices for many positive-profile calculations; continuation to complex arguments entails additional branch conventions.

## References

- [NIST DLMF, §13.4(i), integral representation of Tricomi U](https://dlmf.nist.gov/13.4#i).
