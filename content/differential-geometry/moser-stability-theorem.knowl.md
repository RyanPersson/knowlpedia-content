+++
id = "differential-geometry/moser-stability-theorem"
title = "Moser stability theorem"
kind = "theorem"
summary = "A cohomologically constant smooth family of symplectic forms on a compact manifold is trivialized by an isotopy."
aliases = ["Moser trick", "Moser isotopy theorem"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-manifold", "differential-geometry/symplectic-manifold", "differential-geometry/smooth-isotopy", "differential-geometry/symplectomorphism", "fiber-bundles/vector-field", "differential-geometry/de-rham-complex"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a compact [[fiber-bundles/smooth-manifold|smooth manifold]] without boundary, and let \(\omega_t\), \(0\leq t\leq1\), be a smooth family of [[differential-geometry/symplectic-manifold|symplectic forms]] whose de Rham cohomology class \([\omega_t]\) is independent of \(t\). The **Moser stability theorem** states that there is a smooth [[differential-geometry/smooth-isotopy|isotopy]] \(\varphi_t:M\to M\), with \(\varphi_0=\operatorname{id}_M\), such that
\[
\varphi_t^*\omega_t=\omega_0
\]
for every \(t\). In particular, \(\varphi_1\) is a [[differential-geometry/symplectomorphism|symplectomorphism]] from \((M,\omega_0)\) to \((M,\omega_1)\). Compactness ensures that the time-dependent [[fiber-bundles/vector-field|vector field]] used in the proof has a global flow through the whole interval.

## Proof mechanism

Choose a smooth family of one-forms \(\sigma_t\) such that
\[
\dot\omega_t=d\sigma_t.
\]
Define the time-dependent vector field \(X_t\) uniquely by
\[
\iota_{X_t}\omega_t=-\sigma_t.
\]
If \(\varphi_t\) is its flow, then
\[
\frac{d}{dt}\bigl(\varphi_t^*\omega_t\bigr)
=\varphi_t^*\bigl(\dot\omega_t+\mathcal L_{X_t}\omega_t\bigr)
=\varphi_t^*\bigl(d\sigma_t-d\sigma_t\bigr)=0.
\]
This conversion of a deformation equation into an equation for a flow is the **Moser trick**.

## Relative and local forms

If the family and the chosen primitives satisfy suitable vanishing conditions along a submanifold, \(X_t\) can be arranged to vanish there, and the resulting isotopy fixes that submanifold. Local and relative versions underlie the Darboux theorem and symplectic neighborhood theorems. The exact vanishing order matters when one also requires the derivative of the isotopy to be the identity along the submanifold.

## Hypotheses and limitations

**Warning.** Equality of endpoint cohomology classes alone is not a statement about an arbitrary intervening path: one needs a smooth path of symplectic forms with constant class. On a noncompact manifold the Moser vector field need not be complete, so additional support, completeness, or behavior-at-infinity hypotheses are required. Manifolds with boundary likewise require conditions ensuring that the vector field is tangent to the boundary when the isotopy must preserve it.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2008. [Chapter DOI record](https://doi.org/10.1007/978-3-540-45330-7_7). Relevant: “Moser Theorems,” pp. 49–53.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [Oxford DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: §3.2, Moser isotopy arguments.
3. Jürgen Moser, “On the Volume Elements on a Manifold,” *Transactions of the American Mathematical Society* 120 (1965), 286–294. [AMS DOI record](https://doi.org/10.1090/S0002-9947-1965-0182927-5). Relevant: the original deformation-by-isotopy method.
