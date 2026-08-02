+++
id = "fiber-bundles/donaldson-uhlenbeck-yau-theorem"
title = "Donaldson–Uhlenbeck–Yau theorem"
kind = "theorem"
summary = "The equivalence between slope-polystability of a holomorphic vector bundle and existence of a Hermitian Yang-Mills metric."
aliases = ["DUY theorem", "Kobayashi-Hitchin correspondence for vector bundles"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \((X,\omega)\) be a compact complex \(n\)-dimensional
[[differential-geometry/kahler-manifold|Kähler manifold]] and \(E\to X\) a
[[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundle]]. The **Donaldson–Uhlenbeck–Yau theorem** states that \(E\) admits a
[[fiber-bundles/hermitian-metric|Hermitian metric]] whose
[[fiber-bundles/chern-connection|Chern connection]] is
[[fiber-bundles/hermitian-yang-mills-connection|Hermitian Yang–Mills]] if
and only if \(E\) is slope-polystable with respect to \(\omega\). Here
\[
\mu_\omega(E)=\frac{1}{\operatorname{rk}E}
\int_X c_1(E)\wedge\frac{\omega^{n-1}}{(n-1)!},
\]
stability requires \(\mu_\omega(F)<\mu_\omega(E)\) for every coherent
subsheaf \(F\subset E\) with
\(0<\operatorname{rk}F<\operatorname{rk}E\), and polystability means a direct sum of
stable bundles having the same slope.

## The two directions

The differential-geometric direction shows that a Hermitian Yang–Mills
connection forces the slope inequalities and a splitting at equality; hence
the associated holomorphic bundle is polystable. The analytic direction
constructs a Hermitian–Einstein metric from stability by solving a nonlinear
elliptic equation.

## Stable and polystable forms

If \(E\) is stable, its Hermitian–Einstein metric is unique up to multiplication
by a positive scalar, and its Hermitian Yang–Mills connection is irreducible
and unique up to unitary gauge.
If \(E\) is polystable, write
\[
E=\bigoplus_j E_j
\]
with the \(E_j\) stable of common slope; the direct sum of their
Hermitian–Einstein connections solves the equation on \(E\). Equal slope is
essential, because the central constant in the Hermitian [[fiber-bundles/yangmills-equation|Yang–Mills equation]]
is determined by the slope.

## Scope and conventions

The theorem is also called the Kobayashi–Hitchin correspondence in this
vector-bundle setting. The numerical constant in the equation
\(\sqrt{-1}\Lambda_\omega F_A=\lambda I\) depends on conventions for
\(\Lambda_\omega\), \(c_1(E)\), and volume, but its proportionality to
\(\mu_\omega(E)\) does not.

Compactness, the [[differential-geometry/kahler-form|Kähler form]] used to define slope, and holomorphicity are
substantive hypotheses. A merely Hermitian base or an arbitrary smooth
complex bundle is outside the theorem as stated; extensions require different
stability notions and analytic hypotheses.

It suffices to test the stability inequality on saturated coherent
subsheaves of positive rank and rank strictly below that of \(E\). Torsion
subsheaves have rank zero and are not in the range of the displayed slope
test.

## References

1. S. K. Donaldson, “Anti Self-Dual Yang-Mills Connections over Complex Algebraic Surfaces and Stable Vector Bundles,” *Proceedings of the London Mathematical Society* s3-50 (1985), 1–26. [DOI record](https://doi.org/10.1112/plms/s3-50.1.1). Relevant: the correspondence for algebraic surfaces.
2. Karen Uhlenbeck and Shing-Tung Yau, “On the Existence of Hermitian-Yang-Mills Connections in Stable Vector Bundles,” *Communications on Pure and Applied Mathematics* 39 (1986), S257–S293. [DOI record](https://doi.org/10.1002/cpa.3160390714). Relevant: existence for stable bundles over compact Kähler manifolds.
