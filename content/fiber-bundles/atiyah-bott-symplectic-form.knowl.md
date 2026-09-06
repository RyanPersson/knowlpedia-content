+++
id = "fiber-bundles/atiyah-bott-symplectic-form"
title = "Atiyah–Bott symplectic form"
kind = "definition"
summary = "The gauge-invariant symplectic form on the affine space of connections over an oriented closed surface."
aliases = ["symplectic form on the space of connections", "Atiyah–Bott form"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["lie-groups/compact-lie-group", "lie-groups/lie-algebra", "linear-algebra/inner-product", "fiber-bundles/principal-g-bundle", "fiber-bundles/bundle-of-connections", "differential-geometry/tangent-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\Sigma\) be a closed oriented surface, let \(G\) be a [[lie-groups/compact-lie-group|compact Lie group]] whose [[lie-groups/lie-algebra|Lie algebra]] has an \(\operatorname{Ad}\)-invariant [[linear-algebra/inner-product|inner product]] \(\langle-,-\rangle\), and let \(P\to\Sigma\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]]. The [[fiber-bundles/bundle-of-connections|space of connections]] \(\mathcal A(P)\) is affine with [[differential-geometry/tangent-space|tangent space]] \(\Omega^1(\Sigma;\operatorname{ad}P)\). Its **Atiyah–Bott symplectic form** is the constant two-form
\[
\omega_A(a,b)=\int_\Sigma\langle a\wedge b\rangle,
\qquad
a,b\in T_A\mathcal A(P).
\]
Here the coefficient pairing and wedge product produce an ordinary two-form. Orientation defines the integral, while compactness makes it finite without support conditions.

## Why the form is symplectic

The formula does not depend on \(A\), so \(\omega\) is closed. If \(a\ne0\), choose a Riemannian metric on \(\Sigma\) and put \(b=*a\); then
\[
\omega_A(a,*a)=\int_\Sigma |a|^2\,d\operatorname{vol}>0.
\]
Thus the pairing is nondegenerate on smooth tangent vectors. In the Fréchet setting this is commonly called a weak symplectic form: the induced map from the tangent space to its continuous dual need not be onto.

The [[fiber-bundles/gauge-group|gauge group]] preserves \(\omega\), because its action on \(\operatorname{ad}P\) preserves the chosen inner product. Together these properties provide the symplectic setup for gauge-theoretic reduction.

## Role in gauge theory

For a surface, curvature is an \(\operatorname{ad}P\)-valued top-degree form. Using the same coefficient pairing, it represents a covector on the Lie algebra \(\Omega^0(\Sigma;\operatorname{ad}P)\) of the gauge group. The resulting [[fiber-bundles/curvature-as-a-moment-map|curvature moment map]] turns flatness into a moment-map equation, so the [[fiber-bundles/moduli-space-of-flat-connections|moduli space of flat connections]] is formally a [[differential-geometry/symplectic-quotient|symplectic quotient]].

## Conventions and scope

Multiplying the invariant inner product by a positive constant rescales \(\omega\). A sign may also be inserted, especially when authors choose the opposite convention for fundamental [[fiber-bundles/vector-field|vector fields]] or [[fiber-bundles/moment-map|moment maps]]. The construction extends to noncompact surfaces only after imposing support or decay conditions that make the integral and functional-analytic setting meaningful.

## References

1. Michael F. Atiyah and Raoul Bott, “The Yang–Mills Equations over Riemann Surfaces,” *Philosophical Transactions of the Royal Society of London A* 308 (1983), 523–615. [DOI record](https://doi.org/10.1098/rsta.1983.0017). Relevant: §9, the symplectic structure on the space of connections and reduction by the gauge group.
