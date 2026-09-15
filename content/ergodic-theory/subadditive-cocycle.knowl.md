+++
id = "ergodic-theory/subadditive-cocycle"
title = "Subadditive cocycle"
kind = "definition"
summary = "A sequence whose cost over a concatenated orbit segment is at most the sum of its two segment costs."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "measure-theory/measurable-function"]
+++

A **subadditive cocycle** over \(T\) is a sequence of [[measure-theory/measurable-function|measurable real functions]] \(a_n\), \(n\geq0\), with \(a_0=0\) and
\[
a_{n+m}(x)\leq a_n(x)+a_m(T^nx)
\quad(n,m\geq0)
\]
almost everywhere. Equality defines an additive cocycle.

## Examples

Orbit sums \(a_n=\sum_{j=0}^{n-1}f\circ T^j\) are additive. For products \(A^{(n)}(x)=A(T^{n-1}x)\cdots A(x)\) of invertible matrices, \(a_n(x)=\log\|A^{(n)}(x)\|\) is subadditive by the operator-norm product inequality.
