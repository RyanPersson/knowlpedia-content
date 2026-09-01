+++
id = "operator-algebras/takai-duality"
title = "Takai duality"
kind = "theorem"
summary = "Crossing an abelian C*-dynamical system successively by an action and its dual recovers the original algebra up to stabilization."
aliases = ["Imai-Takai duality", "crossed-product duality"]
domains = ["operator-algebras", "harmonic-analysis", "dynamical-systems"]
prerequisites = ["operator-algebras/cstar-dynamical-system", "operator-algebras/dual-action-crossed-product", "operator-algebras/compact-operator-cstar-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((A,G,\alpha)\) be a [[operator-algebras/cstar-dynamical-system| \(C^*\)-dynamical system]] with \(G\) locally compact abelian, and let
\(\widehat\alpha\) be the [[operator-algebras/dual-action-crossed-product| dual action]] on \(A\rtimes_\alpha G\). **Takai duality** gives a canonical
\(*\)-isomorphism
\[
(A\rtimes_\alpha G)\rtimes_{\widehat\alpha}\widehat G
\cong A\otimes K(L^2(G)).
\]
Here \(K(L^2(G))\) is the [[operator-algebras/compact-operator-cstar-algebra| compact-operator \(C^*\)-algebra]]. Thus crossing twice recovers \(A\) after
stabilization; it does not generally recover \(A\) literally. The theorem is
natural for equivariant \(*\)-homomorphisms and also identifies the
double-dual action, so it retains dynamical information rather than giving
only an abstract algebra isomorphism.

## Equivariance

Pontryagin duality identifies \(\widehat{\widehat G}\) with \(G\), so the
double crossed product carries a double-dual action. Under a standard Takai
isomorphism this action corresponds to
\[
s\longmapsto \alpha_s\otimes\operatorname{Ad}\rho_s,
\]
where \(\rho\) is a [[algebra-representation-theory/regular-representation|regular representation]] of \(G\) on \(L^2(G)\).
Left-versus-right regular-representation and character conventions can
change the displayed implementation by inversion or unitary conjugacy, but
not the stabilized isomorphism class.

## How to interpret the theorem

The first crossed product packages the coefficients \(A\) together with the
\(G\)-action. The dual action then measures the Fourier variable introduced
by that construction. Crossing by \(\widehat G\) performs the inverse
Fourier operation, while the regular representation leaves the compact
operator factor.

Because \(K(L^2(G))\) is Morita equivalent to \(\mathbb C\), Takai duality
implies that the double crossed product is strongly Morita equivalent to
\(A\). Consequently stable invariants, including \(K\)-theory, return to
those of the coefficient algebra.

## Full and reduced versions

For abelian \(G\), the group is amenable. Hence full and reduced crossed
products agree at both stages, so the theorem may be written with either
completion. For nonabelian groups, crossed-product duality is formulated
using coactions rather than a Pontryagin-dual [[algebra-groups/group-action|group action]].

## References

1. Hiroshi Takai, “On a duality for crossed products of \(C^*\)-algebras,” *Journal of Functional Analysis* 19 (1975), 25–39. [Publisher DOI record](https://doi.org/10.1016/0022-1236%2875%2990004-X). Relevant: the original stabilized double-crossed-product theorem.
2. Dana P. Williams, *Crossed Products of \(C^*\)-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [AMS DOI record](https://doi.org/10.1090/surv/134). Relevant: Chapter 7 on dual actions and Takai duality.
