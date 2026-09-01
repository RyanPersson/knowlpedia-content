+++
id = "fiber-bundles/stabilizer-of-a-connection"
title = "Stabilizer of a connection"
kind = "definition"
summary = "The subgroup of gauge transformations that leave a connection fixed."
aliases = ["gauge stabilizer", "isotropy group of a connection"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/gauge-group", "fiber-bundles/principal-connection", "fiber-bundles/proposition-gauge-group-acts-on-conn-by-pullback", "algebra-groups/stabilizer", "fiber-bundles/gauge-transformation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]], let \(\mathcal G(P)\) be its [[fiber-bundles/gauge-group|gauge group]], and let \(A\) be a [[fiber-bundles/principal-connection|principal connection]]. The **stabilizer of \(A\)** is
\[
\operatorname{Stab}(A)
:=
\{u\in\mathcal G(P)\mid u\cdot A=A\},
\]
where \(u\cdot A\) denotes the [[fiber-bundles/proposition-gauge-group-acts-on-conn-by-pullback|gauge action on connections]]. It is the [[algebra-groups/stabilizer|stabilizer subgroup]] of \(A\) for this action. Its elements are precisely the gauge symmetries of the connection. A connection with stabilizer larger than the unavoidable central [[fiber-bundles/gauge-transformation|gauge transformations]] is called reducible in many gauge-theoretic settings.

## Description by parallel sections

A gauge transformation may be viewed as a section of the adjoint group bundle \(\operatorname{Ad}(P)=P\times_GG\). It fixes \(A\) exactly when that section is parallel for the connection induced by \(A\). Thus a stabilizing transformation is determined by its value at one point on each [[topology/connected-component|connected component]] of \(M\).

If \(M\) is connected and \(p\in P\), evaluation at \(p\) identifies the stabilizer with the [[algebra-groups/centralizer|centralizer]] of the [[fiber-bundles/holonomy-group|holonomy group]]:
\[
\operatorname{Stab}(A)\cong
\{g\in G\mid gh=hg\text{ for every }h\in\operatorname{Hol}_p(A)\}.
\]
Changing \(p\) conjugates both subgroups, so the description is intrinsic up to conjugacy.

## Role in gauge quotients

The [[algebra-groups/orbit|orbit]] of \(A\) is modeled infinitesimally by gauge directions modulo the [[lie-groups/lie-algebra|Lie algebra]] of \(\operatorname{Stab}(A)\). When the stabilizer is minimal, a local gauge slice can often produce a manifold-like chart on the quotient. A larger stabilizer produces isotropy, so the [[fiber-bundles/quotient-space-of-an-action|orbit space]] of connections is generally singular or stratified rather than a [[fiber-bundles/smooth-manifold|smooth manifold]].

For a connected base, every constant transformation with value in the center \(Z(G)\) stabilizes every connection. [[fiber-bundles/gauge-theory|Gauge theory]] therefore often quotients by the center, or calls \(A\) irreducible when its stabilizer is exactly this central subgroup.

## Remarks

The exact terminology depends on the chosen gauge group. Requiring Sobolev regularity, fixing a framing, or fixing the transformation at a basepoint changes the stabilizer. In particular, a [[fiber-bundles/based-gauge-group|based gauge group]] removes constant central symmetries and can make its action free where the full gauge-group action is not.

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 3, gauge-group actions and their stabilizers.
