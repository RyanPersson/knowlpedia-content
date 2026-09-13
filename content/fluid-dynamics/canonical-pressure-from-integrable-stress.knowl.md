+++
id = "fluid-dynamics/canonical-pressure-from-integrable-stress"
title = "Canonical pressure from an integrable tensor"
kind = "definition"
summary = "A bounded Fourier symbol assigns an H minus s pressure to an L1 momentum tensor."
aliases = ["double Riesz pressure representation"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["harmonic-analysis/riesz-transform", "functional-analysis/l1-negative-sobolev-bound", "partial-differential-equations/poisson-equation", "linear-algebra/matrix", "real-analysis/divergence-of-tensor", "functional-analysis/fourier-transform-tempered-distributions", "shared-foundations/finite-sum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For a matrix field \(g=(g_{ij})\) with entries in \(L^1(\mathbb R^n)\), define its **canonical pressure** \(\pi_*\) by
\[
\widehat{\pi_*}(\xi)=-\sum_{i,j}\frac{\xi_i\xi_j}{|\xi|^2}\widehat{g_{ij}}(\xi)\quad(\xi\ne0).
\]
The right side is a bounded measurable function. Its inverse Fourier transform is in \(H^{-s}\) for every \(s>n/2\), by the [[functional-analysis/l1-negative-sobolev-bound|integrable-input Sobolev bound]].

## Pressure equation

The definition gives
\[
-\Delta\pi_*=\sum_{i,j}\partial_i\partial_jg_{ij},\qquad
\|\pi_*\|_{H^{-s}}\le C_{n,s}\sum_{i,j}\|g_{ij}\|_1.
\]
For inputs also in \(L^2\), this agrees with \(\sum R_iR_jg_{ij}\). For an incompressible velocity, taking divergence of the momentum equation produces this pressure source with \(g=u\otimes u\), when the other terms have zero divergence. A difference of quadratic tensors gives a difference-pressure source.

## Actual pressures

Another distributional solution differs by a harmonic distribution. Identifying its gradient with \(\nabla\pi_*\) requires a global growth or Sobolev bound on that gradient; the Poisson equation alone does not supply it.
