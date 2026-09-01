+++
id = "differential-geometry/hkt-metric"
title = "HKT metric"
kind = "definition"
summary = "A hyper-Hermitian metric whose three Hermitian structures share a metric connection with skew torsion."
aliases = ["hyperkähler with torsion metric", "hyper-Kähler with torsion", "HKT geometry"]
domains = ["differential-geometry", "quaternionic-analysis"]
prerequisites = ["differential-geometry/hyperhermitian-manifold", "differential-geometry/fundamental-form-almost-hermitian"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,I,J,K,g)\) be a
[[differential-geometry/hyperhermitian-manifold|hyper-Hermitian manifold]],
with [[differential-geometry/fundamental-form-almost-hermitian|fundamental
two-forms]] \(\omega_I,\omega_J,\omega_K\). Set, in the
left-action convention,
\[
\Omega_I=\omega_J+i\omega_K\in\Omega_I^{2,0}(M).
\]
The metric \(g\) is an **HKT metric**—**hyperkähler with torsion**—if
\[
\partial_I\Omega_I=0.
\]

## Connection characterization

Equivalently, the Hermitian Bismut connections of \((g,I)\), \((g,J)\), and
\((g,K)\) coincide. Their common connection preserves the hypercomplex triple
and has totally skew-symmetric torsion. This explains the name.

## Relation to hyperkähler geometry

Every [[differential-geometry/hyperkahler-manifold|hyperkähler metric]] is HKT
with zero torsion. An HKT metric need not be hyperkähler: the individual
fundamental forms need not be closed, and the Levi-Civita connection need not
preserve \(I,J,K\). Thus HKT is an intermediate differential condition on a
hyper-Hermitian metric, not an alias for either neighboring structure.

## Potentials

Every HKT metric admits local potentials. More precisely, locally there is a
smooth [[complex-analysis/strictly-quaternionic-plurisubharmonic-function|
strictly quaternionic plurisubharmonic function]] \(u\) for which the
metric is obtained from \(\partial\partial_Ju\); conversely, such a function
produces an HKT metric.

## Sign convention

With the right-action convention of Alesker–Verbitsky, one writes
\(\Omega=\omega_J-i\omega_K\). The sign changes with the action and
fundamental-form conventions; the condition must be read together with the
definition of \(\Omega\).

## References

1. P. S. Howe and G. Papadopoulos, “Twistor spaces for hyper-Kähler manifolds with torsion,” *Physics Letters B* 379 (1996), 80–86. [DOI record](https://doi.org/10.1016/0370-2693(96)00442-8).
2. Semyon Alesker and Misha Verbitsky, “Plurisubharmonic functions on hypercomplex manifolds and HKT-geometry,” *Journal of Geometric Analysis* 16 (2006), 375–399. [arXiv record](https://arxiv.org/abs/math/0510140).
