+++
id = "differential-geometry/calabi-yau-theorem"
title = "Calabi–Yau theorem"
kind = "theorem"
summary = "Each Kähler class on a compact Kähler manifold contains a unique metric with any prescribed Ricci form representing the first Chern class."
aliases = ["Yau theorem", "solution of the Calabi conjecture"]
domains = ["differential-geometry", "partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["differential-geometry/kahler-manifold", "differential-geometry/kahler-class", "differential-geometry/kahler-form", "differential-geometry/ricci-form", "differential-geometry/kahler-metric"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a compact connected
[[differential-geometry/kahler-manifold|Kähler manifold]], let \(\kappa\) be
a [[differential-geometry/kahler-class|Kähler class]], and let \(\rho\) be a
real closed \((1,1)\)-form representing \(2\pi c_1(X)\). The **Calabi–Yau
theorem** states that there is a unique [[differential-geometry/kahler-form|Kähler form]] \(\omega\in\kappa\) whose
[[differential-geometry/ricci-form|Ricci form]] is \(\rho\). Equivalently,
after choosing \(\omega_0\in\kappa\) and a smooth real function \(F\)
satisfying
\[
\int_X e^F\omega_0^n=\int_X\omega_0^n,
\]
there is a unique normalized real potential \(\varphi\) with \(\omega_0+i\partial\bar\partial\varphi>0\) and
\[
(\omega_0+i\partial\bar\partial\varphi)^n=e^F\omega_0^n.
\]

## Ricci-flat consequence

If \(c_1(X)=0\) in real cohomology, take \(\rho=0\). Every Kähler class then contains a unique Ricci-flat [[differential-geometry/kahler-metric|Kähler metric]]. In particular, every [[differential-geometry/calabi-yau-manifold|Calabi–Yau manifold]] in the broad trivial-canonical-bundle sense has such a metric in each Kähler class.

The conclusion is uniqueness inside a fixed class. Different Kähler classes generally give different Ricci-flat metrics. It also does not assert full holonomy \(SU(n)\): complex tori and [[differential-geometry/hyperkahler-manifold|hyperkähler manifolds]] have smaller holonomy.

## Analytic content

The Ricci-form equation reduces to the nonlinear complex Monge–Ampère equation displayed in the core. Uniqueness follows from a maximum-principle argument. Existence requires a priori \(C^0\), Laplacian, and higher-order estimates along a continuity path; obtaining these estimates is the central achievement of Yau’s proof.

The volume constraint is necessary: integrating both sides of the Monge–Ampère equation gives it immediately. Adding a constant to \(\varphi\) changes neither side, which is why a normalization such as \(\int_X\varphi\,\omega_0^n=0\) is imposed for uniqueness.

## Conventions and scope

The factor \(2\pi\), the sign of the Ricci form, and whether one writes \(i\partial\bar\partial\varphi\) or \(\frac{i}{2}\partial\bar\partial\varphi\) vary with curvature conventions. The cohomology class of \(\rho\) and the Monge–Ampère normalization must use one consistent convention.

Compactness is essential to the theorem as stated. Complete noncompact analogues require separate geometric and analytic assumptions. The theorem prescribes the Ricci form, not an arbitrary full [[differential-geometry/riemann-curvature-tensor|Riemann curvature tensor]].

## References

1. S.-T. Yau, “On the Ricci Curvature of a Compact Kähler Manifold and the Complex Monge–Ampère Equation, I,” *Communications on Pure and Applied Mathematics* 31 (1978), 339–411. [DOI record](https://doi.org/10.1002/cpa.3160310304). Relevant: Theorems 1–2 and §§2–4, existence, uniqueness, and estimates for the Calabi conjecture.
2. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: Appendix 4.B, the Calabi conjecture and Ricci-flat Kähler metrics.
