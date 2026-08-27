+++
id = "complex-analysis/quaternionic-monge-ampere-measure"
title = "Quaternionic Monge–Ampère measure"
kind = "definition"
summary = "The Moore-determinant Hessian measure of a continuous quaternionic plurisubharmonic function."
aliases = ["quaternionic Monge-Ampere operator", "quaternionic Monge–Ampère operator", "quaternionic Hessian measure"]
domains = ["complex-analysis", "quaternionic-analysis", "partial-differential-equations"]
section_mode = "progressive"
+++

For a \(C^2\) [[complex-analysis/quaternionic-plurisubharmonic-function|
quaternionic plurisubharmonic function]] \(u\) on
\(\Omega\subseteq\mathbb H^n\), its **quaternionic Monge–Ampère measure** is
\[
\operatorname{MA}_{\mathbb H}(u)
=\det_M\!\left(\frac{\partial^2u}
{\partial\bar q_i\,\partial q_j}\right)dV,
\]
where \(\det_M\) is the [[linear-algebra/moore-determinant|Moore determinant]]
and \(dV\) is [[measure-theory/lebesgue-measure|Lebesgue measure]].

## Continuous potentials

For a continuous quaternionic PSH function, this expression has a unique
extension as a nonnegative Borel measure characterized by agreement with the
smooth formula and continuity under locally
[[real-analysis/uniform-convergence|uniform convergence]]. This is the
quaternionic analogue of Aleksandrov's real Hessian measure and the
Chern–Levine–Nirenberg/Bedford–Taylor
[[complex-analysis/complex-monge-ampere-operator|complex Monge–Ampère measure]].

## Scope

Continuity of \(u\) is part of this basic definition. More singular
quaternionic PSH functions require additional pluripotential-theoretic domains
of definition; one should not apply the determinant measure to an arbitrary
unbounded function without specifying such a class.

## References

1. Semyon Alesker, “Non-commutative linear algebra and plurisubharmonic functions of quaternionic variables,” *Bulletin des Sciences Mathématiques* 127 (2003), 1–35. [arXiv record](https://arxiv.org/abs/math/0104209). Relevant: Theorem 3.4.
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: §3.
