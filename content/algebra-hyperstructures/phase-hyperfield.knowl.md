+++
id = "algebra-hyperstructures/phase-hyperfield"
title = "Phase hyperfield"
kind = "example"
summary = "The quotient hyperfield of the complex numbers by positive real scaling."
aliases = ["complex phase hyperfield", "hyperfield of phases"]
domains = ["algebra-hyperstructures", "complex-analysis"]
prerequisites = ["algebra-hyperstructures/hyperfield-of-a-field-quotient"]
dependency_review_count = 1
section_mode = "progressive"
+++

The **phase hyperfield** is the
[[algebra-hyperstructures/hyperfield-of-a-field-quotient|quotient
hyperfield]]
\[
\mathbb P=\mathbb C/\mathbb R_{>0}.
\]
Its elements are \(0\) together with the complex phases \(S^1\).
Multiplication is ordinary multiplication of phases, while the hyper-sum of
two phases is the set of phases of all sums of positive real multiples of
representatives.

For distinct non-antipodal \(u,v\in S^1\), the sum \(u\boxplus v\) is the
open shorter arc from \(u\) to \(v\). If \(v=-u\), then
\[
u\boxplus(-u)=\{0,u,-u\}.
\]
The quotient map \(\mathbb C\to\mathbb P\) records the phase of a nonzero
complex number and is a weak hyperfield homomorphism.

## References

1. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034).
2. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204).
