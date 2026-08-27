+++
id = "complex-analysis/pluriharmonic-function"
title = "Pluriharmonic function"
kind = "definition"
summary = "A function whose restriction to every affine complex line is harmonic."
aliases = ["PH function", "pluriharmonicity"]
domains = ["complex-analysis", "several-complex-variables", "potential-theory"]
section_mode = "progressive"
+++

Let \(U\subseteq\mathbb C^d\) be open. A real-valued function \(u\) on \(U\)
is **pluriharmonic** if its restriction to every affine complex line is
[[complex-analysis/harmonic-function|harmonic]] on each component of the
intersection with \(U\).

## Differential characterization

For \(u\in C^2(U)\), pluriharmonicity is equivalent to the vanishing of the
entire [[complex-analysis/levi-form|Levi form]]:
\[
\frac{\partial^2u}{\partial z_j\partial\bar z_k}=0
\qquad (1\le j,k\le d).
\]
Thus both \(u\) and \(-u\) are
[[complex-analysis/plurisubharmonic-function|plurisubharmonic]]. In particular,
every pluriharmonic function is harmonic, but the converse fails in complex
dimension greater than one.

## Local holomorphic representation

Locally, a pluriharmonic function is the real part of a holomorphic function:
near every point there is a holomorphic \(F\) with \(u=\operatorname{Re}F\).
On a non-simply-connected domain these local conjugates can have nontrivial
periods, so a single global \(F\) need not exist.

## References

1. Lars Hörmander, *An Introduction to Complex Analysis in Several Variables*, 3rd ed., North-Holland, 1990. Relevant: Chapter 2, plurisubharmonic and pluriharmonic functions.
2. Marek Klimek, *Pluripotential Theory*, Oxford University Press, 1991. [Publisher record](https://global.oup.com/academic/product/pluripotential-theory-9780198535683).
