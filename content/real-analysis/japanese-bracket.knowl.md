+++
id = "real-analysis/japanese-bracket"
title = "Japanese bracket"
kind = "notation"
summary = "The smooth positive weight (1 + norm-squared)^(1/2) used to combine local and asymptotic estimates."
aliases = ["Peetre bracket", "angle bracket weight"]
domains = ["real-analysis", "harmonic-analysis", "partial-differential-equations"]
prerequisites = []
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For \(x\in\mathbb R^d\), the **Japanese bracket** is the notation
\[
\langle x\rangle=(1+|x|^2)^{1/2}.
\]
It is smooth and positive everywhere, comparable to \(1+|x|\), and comparable
to \(|x|\) for large \(|x|\).

## Use in weighted estimates

A bound such as \(|f(x)|\le C\langle x\rangle^{-N}\) describes polynomial decay
without a singularity at the origin. Symbol estimates are often written
\(|D^\alpha a(x)|\le C_\alpha\langle x\rangle^{m-|\alpha|}\).

## Basic inequality

There is an absolute constant \(C\) such that
\(\langle x+y\rangle\le C\langle x\rangle\langle y\rangle\). This permits
weighted convolution and translation estimates.

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2).
