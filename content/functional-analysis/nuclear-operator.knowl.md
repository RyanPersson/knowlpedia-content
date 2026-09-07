+++
id = "functional-analysis/nuclear-operator"
title = "Nuclear operator between Banach spaces"
kind = "definition"
summary = "A bounded operator represented by an absolutely summable series of rank-one operators."
aliases = ["nuclear operator", "nuclear map between Banach spaces"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/banach-space", "functional-analysis/bounded-linear-operator", "convex-analysis/bounded-linear-functional-norm-of-a-functional"]
+++

Let \(X\) and \(Y\) be [[linear-algebra/banach-space|Banach spaces]]. A
bounded linear operator \(T:X\to Y\) is **nuclear** if there are bounded linear
functionals \(\varphi_n:X\to\mathbb K\), vectors \(y_n\in Y\), and scalars
\(\lambda_n\) such that
\[
T x=\sum_{n=1}^{\infty}\lambda_n\varphi_n(x)y_n
\quad\text{for every }x\in X,
\qquad
\sum_{n=1}^{\infty}|\lambda_n|\,\lVert\varphi_n\rVert\,\lVert y_n\rVert<\infty.
\]
The series converges absolutely in operator norm. Equivalently, \(T\) is an
absolutely summable sum of rank-one operators
\(x\mapsto\varphi_n(x)y_n\).

## Nuclear norm and consequences

The infimum of the displayed sums over all such representations is the
nuclear norm. Every finite-rank operator is nuclear, and every nuclear operator
is compact.

Nuclearity is stronger than compactness in general; the distinction matters
when nuclearity is used for the linking maps between completed seminorm
quotients of a [[functional-analysis/nuclear-space|nuclear space]].

## Reference

See Sections 2–3 of [Kazhdan's notes on nuclear spaces](https://math.huji.ac.il/~kazhdan/QFT/nuclear.pdf)
for the Banach-space nuclear expansion and the locally convex nuclear-space
criterion.
