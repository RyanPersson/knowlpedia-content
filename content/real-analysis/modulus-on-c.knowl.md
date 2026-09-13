+++
id = "real-analysis/modulus-on-c"
title = "Modulus (absolute value) on ℂ"
kind = "knowl"
summary = "The nonnegative magnitude |z| of a complex number z, equal to its distance from 0."
aliases = ["modulus-on-c", "Modulus (absolute value) on ℂ"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/modulus-on-c.md"
prerequisites = ["shared-foundations/complex-numbers-c", "shared-foundations/complex-conjugate", "real-analysis/nonnegative-square-root"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 3
+++

For \(z=a+bi\in\mathbb{C}\), writing \(\overline z\) for its [[shared-foundations/complex-conjugate|complex conjugate]], the **modulus** (or **absolute value**) of \(z\) is
\[
|z|:=\sqrt{a^2+b^2}=\sqrt{z\overline{z}}.
\]

The square root is the [[real-analysis/nonnegative-square-root|nonnegative square root]].

## Remarks

The modulus makes \(\mathbb{C}\) into a [[linear-algebra/normed-vector-space|normed space]] and induces the standard [[topology/metric|metric]] \(d(z,w)=|z-w|\). It is the complex analogue of [[real-analysis/absolute-value|absolute value]] and is crucial for convergence of complex sequences and series.

## Examples

- If \(z=3-4i\), then \(|z|=\sqrt{3^2+(-4)^2}=5\).
- If \(z\in\mathbb{R}\subseteq\mathbb{C}\), then this definition agrees with the real absolute value.
- \(|e^{i\theta}|=1\) for all \(\theta\in\mathbb{R}\) (Euler's formula context).
