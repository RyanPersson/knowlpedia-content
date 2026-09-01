+++
id = "differential-geometry/local-hkt-potential"
title = "Local HKT potential theorem"
kind = "theorem"
summary = "Smooth strictly quaternionic PSH functions are exactly the local potentials of HKT metrics."
aliases = ["HKT potential", "local potential of an HKT metric"]
domains = ["differential-geometry", "quaternionic-analysis"]
prerequisites = ["differential-geometry/hypercomplex-manifold", "differential-geometry/quaternionic-plurisubharmonic-function-hypercomplex", "differential-geometry/hkt-metric"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,I,J,K)\) be a
[[differential-geometry/hypercomplex-manifold|hypercomplex manifold]]. If
\(u\) is a smooth strictly
[[differential-geometry/quaternionic-plurisubharmonic-function-hypercomplex|
quaternionic plurisubharmonic function]], then the hyperhermitian form
\[
g_u=t(\partial\partial_Ju)
\]
is an [[differential-geometry/hkt-metric|HKT metric]]. Conversely, every HKT
metric is locally of this form around each point.

## Meaning of the formula

The map \(t\) identifies real positive \((2,0)\)-forms with
[[linear-algebra/hyperhermitian-form|hyperhermitian forms]]. Strict positivity
of \(\partial\partial_Ju\) makes \(g_u\) a Riemannian metric, while
\(\partial^2=0\) gives the HKT closure condition.

## Flat normalization

On \(\mathbb H^n\), the metric matrix is a fixed scalar multiple—\(1/4\) in
the Alesker–Verbitsky convention—of the
[[complex-analysis/quaternionic-hessian|quaternionic Hessian]] of \(u\).
Other normalizations of the
[[complex-analysis/cauchy-fueter-operators|Cauchy–Fueter operators]] move this
scalar but do not
change positivity or the local-potential statement.

## Kähler analogy

The theorem parallels the fact that a smooth strictly complex
[[complex-analysis/plurisubharmonic-function|plurisubharmonic function]] is a local
[[differential-geometry/local-kahler-potential|Kähler potential]]. The HKT
formula uses \(\partial\partial_J\) rather than \(i\partial\bar\partial\), and
the resulting metric may have nonzero torsion.

## References

1. Semyon Alesker and Misha Verbitsky, “Plurisubharmonic functions on hypercomplex manifolds and HKT-geometry,” *Journal of Geometric Analysis* 16 (2006), 375–399. [arXiv record](https://arxiv.org/abs/math/0510140). Relevant: Proposition 1.14.
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: Theorem 6.13.
