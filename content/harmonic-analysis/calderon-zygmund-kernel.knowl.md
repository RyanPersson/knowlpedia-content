+++
id = "harmonic-analysis/calderon-zygmund-kernel"
title = "Calderón–Zygmund kernel"
kind = "definition"
summary = "An off-diagonal kernel with inverse-volume size and Hölder regularity in each variable."
aliases = ["standard singular kernel", "CZ kernel"]
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-norm", "topology/holder-continuity", "measure-theory/measurable-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **Calderón–Zygmund kernel** on \(\mathbb R^n\) is a measurable function \(K(x,y)\), defined for \(x\ne y\), such that for some \(C>0\) and \(0<\alpha\le1\),
\[
|K(x,y)|\le C|x-y|^{-n},
\]
and, whenever \(|x-x'|\le|x-y|/2\),
\[
|K(x,y)-K(x',y)|+|K(y,x)-K(y,x')|
\le C\frac{|x-x'|^\alpha}{|x-y|^{n+\alpha}}.
\]
The second condition is a scale-dependent [[topology/holder-continuity|Hölder bound]] in each variable.

## Kernel versus operator

These estimates concern points away from the diagonal. They neither define a value on the diagonal nor by themselves guarantee a bounded singular-integral operator. In particular, an operator may contain a multiple of the identity that cannot be read from its off-diagonal kernel.

## References

- [Tao, Fourier analysis lecture notes 4, §2](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf).
