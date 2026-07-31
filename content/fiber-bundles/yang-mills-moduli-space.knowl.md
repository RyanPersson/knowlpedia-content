+++
id = "fiber-bundles/yang-mills-moduli-space"
title = "Yang–Mills moduli space"
kind = "definition"
summary = "The gauge-equivalence classes of Yang–Mills connections on a fixed principal bundle over a Riemannian manifold."
aliases = ["moduli space of Yang–Mills connections", "Yang–Mills gauge quotient"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(P\to M\) be a principal bundle with compact structure group over an oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]], equipped with an invariant [[linear-algebra/inner-product|inner product]] on the [[lie-groups/lie-algebra|Lie algebra]]. The **Yang–Mills moduli space** of \(P\) is the quotient
\[
\mathcal M_{\mathrm{YM}}(P)
=
\{A\in\mathcal A(P)\mid d_A^*F_A=0\}/\mathcal G(P),
\]
where \(\mathcal A(P)\) is the space of connections and \(\mathcal G(P)\) is the [[fiber-bundles/gauge-group|gauge group]]. Thus its points are gauge-equivalence classes of [[fiber-bundles/yangmills-connection|Yang–Mills connections]] on the fixed bundle \(P\). Analytic treatments replace the smooth spaces by compatible Sobolev completions without changing the smooth gauge-equivalence classes.

## Local structure

The [[fiber-bundles/slice-theorem-for-the-gauge-action|slice theorem for the gauge action]] replaces the quotient locally by solutions in a Coulomb slice modulo the [[fiber-bundles/stabilizer-of-a-connection|stabilizer]]. Near an [[fiber-bundles/irreducible-connection|irreducible connection]], after removing unavoidable central [[fiber-bundles/gauge-transformation|gauge transformations]], elliptic deformation theory can give a finite-dimensional manifold when the obstruction space vanishes. [[fiber-bundles/reducible-connection|Reducible connections]] have larger stabilizers and generally create singular strata.

The linearized [[fiber-bundles/yangmills-equation|Yang–Mills equation]] together with the Coulomb condition is elliptic at a solution, but the nonlinear quotient need not be smooth, connected, compact, or finite as a set. These properties depend on \(M\), \(P\), the metric, and the structure group.

## Important subspaces

On an oriented four-manifold, [[fiber-bundles/self-dual-and-anti-self-dual-connection|self-dual and anti-self-dual connections]] define [[fiber-bundles/anti-self-dual-moduli-space|instanton moduli spaces]] inside \(\mathcal M_{\mathrm{YM}}(P)\). They are absolute minima of the [[fiber-bundles/yangmills-functional|Yang–Mills functional]] in the appropriate topological sector by the [[fiber-bundles/yang-mills-energy-identity|Yang–Mills energy identity]]. General Yang–Mills critical points need not be self-dual or anti-self-dual, so the full Yang–Mills moduli space is usually larger.

Over a closed [[differential-geometry/riemann-surface|Riemann surface]], the Yang–Mills functional and its gauge symmetry organize the space into Morse-theoretic strata; Atiyah and Bott use this structure to relate [[fiber-bundles/gauge-theory|gauge theory]] to moduli of holomorphic bundles.

## Compactification and conventions

Sequences of four-dimensional instantons can develop curvature concentration. The ordinary quotient is then enlarged by ideal connections carrying point-like bubbling data, as described by [[fiber-bundles/uhlenbeck-compactness-theorem|Uhlenbeck compactness]].

**Warning.** The notation \(\mathcal M_{\mathrm{YM}}\) is not universal. Some authors use “Yang–Mills moduli space” only for the self-dual or anti-self-dual locus, or fix an energy level or [[fiber-bundles/instanton-number|topological charge]]. The defining equation and quotient convention should always be stated.

## References

1. Michael F. Atiyah and Raoul Bott, “The Yang–Mills Equations over Riemann Surfaces,” *Philosophical Transactions of the Royal Society A* 308 (1983), 523–615. [DOI record](https://doi.org/10.1098/rsta.1983.0017). Relevant: §§3–9, the Yang–Mills functional, gauge quotient, critical sets, and moduli.
2. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 3, spaces of connections, gauge quotients, and local moduli.
