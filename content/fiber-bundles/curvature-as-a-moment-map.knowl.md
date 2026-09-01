+++
id = "fiber-bundles/curvature-as-a-moment-map"
title = "Curvature as a moment map"
kind = "definition"
summary = "The moment-map interpretation of curvature for the gauge action on connections over an oriented closed surface."
aliases = ["Atiyah–Bott moment map", "gauge moment map"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/principal-g-bundle", "linear-algebra/inner-product", "lie-groups/lie-algebra", "fiber-bundles/atiyah-bott-symplectic-form", "fiber-bundles/gauge-group", "fiber-bundles/moment-map"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(P\to\Sigma\) be a [[fiber-bundles/principal-g-bundle|principal bundle]] over a closed oriented surface, with compact structure group \(G\) and an \(\operatorname{Ad}\)-invariant [[linear-algebra/inner-product|inner product]] on its [[lie-groups/lie-algebra|Lie algebra]]. Give \(\mathcal A(P)\) the [[fiber-bundles/atiyah-bott-symplectic-form|Atiyah–Bott symplectic form]]. Identify the dual of the gauge Lie algebra \(\Omega^0(\Sigma;\operatorname{ad}P)\) with \(\Omega^2(\Sigma;\operatorname{ad}P)\) by integration. Then **curvature is a moment map** for the [[fiber-bundles/gauge-group|gauge-group]] action:
\[
\mu\colon\mathcal A(P)\longrightarrow
\Omega^2(\Sigma;\operatorname{ad}P),\qquad
\mu(A)=F_A,
\]
up to the common overall sign convention in the definition of a [[fiber-bundles/moment-map|moment map]].

## Verification of the moment-map identity

For \(\xi\in\Omega^0(\Sigma;\operatorname{ad}P)\), define
\[
\mu^\xi(A)=\int_\Sigma\langle F_A,\xi\rangle.
\]
The curvature variation in the direction \(a\in\Omega^1(\Sigma;\operatorname{ad}P)\) is \(d_Aa\). [[real-analysis/integration-by-parts|Integration by parts]] on the closed surface gives
\[
d\mu^\xi_A(a)
=\int_\Sigma\langle d_Aa,\xi\rangle
=\int_\Sigma\langle a\wedge d_A\xi\rangle,
\]
with the displayed sign corresponding to one standard convention. Since the infinitesimal gauge action is \(d_A\xi\) or \(-d_A\xi\), depending on whether the action and fundamental [[fiber-bundles/vector-field|vector fields]] are defined on the left or right, this is precisely the Hamiltonian identity.

## Symplectic reduction and Yang–Mills

The zero level is the set of flat connections:
\[
\mu^{-1}(0)=\{A:F_A=0\}.
\]
Consequently, the [[fiber-bundles/moduli-space-of-flat-connections|flat moduli space]] is formally the [[differential-geometry/symplectic-quotient|symplectic quotient]] \(\mathcal A(P)\mathbin{/\mkern-6mu/}\mathcal G(P)\). At regular irreducible points this produces the familiar finite-dimensional symplectic structure; stabilizers and obstructions can make the quotient singular.

After a Riemannian metric is chosen on \(\Sigma\), the [[fiber-bundles/yangmills-functional|Yang–Mills functional]] is, up to normalization, the squared \(L^2\)-norm \(\|\mu(A)\|^2\). This is why equivariant Morse theory for a norm-square of a moment map enters the Atiyah–Bott analysis.

## Conventions and scope

Changing the sign of the symplectic form, the infinitesimal gauge action, or the moment-map identity changes \(\mu\) to \(-F_A\). A central constant can also shift a moment map; fixed central-curvature equations are therefore nonzero moment levels. The direct identification above is special to a two-dimensional oriented base, where curvature has top degree.

## References

1. Michael F. Atiyah and Raoul Bott, “The Yang–Mills Equations over Riemann Surfaces,” *Philosophical Transactions of the Royal Society of London A* 308 (1983), 523–615. [DOI record](https://doi.org/10.1098/rsta.1983.0017). Relevant: §9, curvature as the moment map and the symplectic reduction of flat connections.
