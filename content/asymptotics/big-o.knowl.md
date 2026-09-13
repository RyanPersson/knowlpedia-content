+++
id = "asymptotics/big-o"
title = "Big-O notation"
kind = "definition"
summary = "An eventual bound by a fixed multiple of a comparison function."
aliases = ["Big O notation", "Landau O notation", "implicit constant"]
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["shared-foundations/function", "real-analysis/absolute-value", "real-analysis/interval", "real-analysis/modulus-on-c", "linear-algebra/normed-vector-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(f,g\) be real or complex [[shared-foundations/function|functions]] on \((0,\varepsilon_0)\), with \(g(\varepsilon)>0\). The statement **\(f(\varepsilon)=O(g(\varepsilon))\) as \(\varepsilon\downarrow0\)** means that there are \(C<\infty\) and \(\varepsilon_1>0\) such that
\[
|f(\varepsilon)|\le Cg(\varepsilon)\qquad(0<\varepsilon<\varepsilon_1).
\]
The constants do not depend on \(\varepsilon\). Other limiting regimes use the corresponding eventual neighborhood. For a normed-space valued function, replace absolute value by its norm.

## Reading an estimate

The notation asserts a bound, not an equality with a particular function. Thus \(\varepsilon^2=O(\varepsilon)\), but the latter statement hides the sharper order. In \(A\lesssim B\), the implicit constant must have the same declared independence as in a Big-O estimate.

## Derivatives require separate control

A bound on values does not automatically bound derivatives. For example, \(f(\varepsilon)=\varepsilon^2\sin(\varepsilon^{-3})\) is \(O(\varepsilon^2)\), whereas its derivative contains \(-3\varepsilon^{-2}\cos(\varepsilon^{-3})\). Parameter-uniform and derivative estimates must be stated separately.

## References

- [NIST Digital Library of Mathematical Functions, §2.1: Definitions and elementary properties](https://dlmf.nist.gov/2.1).
