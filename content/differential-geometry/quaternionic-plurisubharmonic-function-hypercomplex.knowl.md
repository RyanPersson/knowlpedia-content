+++
id = "differential-geometry/quaternionic-plurisubharmonic-function-hypercomplex"
title = "Quaternionic plurisubharmonic function on a hypercomplex manifold"
kind = "definition"
summary = "A function whose del-del-J form is a nonnegative real (2,0)-form on a hypercomplex manifold."
aliases = ["hypercomplex plurisubharmonic function", "quaternionic PSH function on a hypercomplex manifold"]
domains = ["differential-geometry", "quaternionic-analysis", "potential-theory"]
section_mode = "progressive"
+++

Let \((M,I,J,K)\) be a
[[differential-geometry/hypercomplex-manifold|hypercomplex manifold]]. A
continuous real-valued function \(u\) is **quaternionic plurisubharmonic** if
the generalized real \((2,0)\)-form
\[
\partial\partial_Ju
\]
is nonnegative. For a smooth \(u\), nonnegativity means that the associated
[[linear-algebra/hyperhermitian-form|hyperhermitian form]]
\(t(\partial\partial_Ju)\) is positive semidefinite.

## Positivity map

In the right-action convention, the identification \(t\) between real
\((2,0)\)-forms and hyperhermitian forms is characterized by
\[
t(\eta)(X,X)=\eta(X,XJ).
\]
This formula translates to the corresponding left-action convention used for
the chosen hypercomplex triple. It makes the positivity condition intrinsic
and independent of coordinates.

## Flat model

On \(M=\mathbb H^n\) with its standard hypercomplex structure,
\(t(\partial\partial_Ju)\) is, up to the fixed normalization, the
[[complex-analysis/quaternionic-hessian|quaternionic Hessian]]. Hence this
definition recovers the linewise
[[complex-analysis/quaternionic-plurisubharmonic-function|flat-space
definition]].

## Approximation class

Wedge products of generalized \(\partial\partial_Ju\) forms are first defined
for functions locally approximable, uniformly on compact subsets, by smooth
quaternionic PSH functions. In flat space every continuous quaternionic PSH
function belongs to this class. On a general hypercomplex manifold the
approximation issue is an additional hypothesis, not automatic from the
symbol \(\partial\partial_Ju\).

## References

1. Semyon Alesker and Misha Verbitsky, “Plurisubharmonic functions on hypercomplex manifolds and HKT-geometry,” *Journal of Geometric Analysis* 16 (2006), 375–399. [arXiv record](https://arxiv.org/abs/math/0510140).
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: §6.
