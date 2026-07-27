+++
id = "fiber-bundles/characteristic-class"
title = "Characteristic class"
kind = "knowl"
summary = "A connection-independent de Rham cohomology class obtained from an invariant polynomial in curvature."
aliases = ["characteristic-class", "Characteristic class"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/characteristic-class.md"
+++

Let \(\pi:Q\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] over a smooth manifold \(M\), and let \(\Phi\) be an \(\operatorname{Ad}\)-invariant homogeneous polynomial of degree \(k\) on the Lie algebra \(\mathfrak g\) of \(G\). For any principal connection \(\omega\) on \(Q\), the associated Chern–Weil form is closed and its de Rham class is independent of \(\omega\). The **characteristic class associated with \(\Phi\)** is

\[
c_\Phi(Q):=[\mathrm{CW}_\Phi(\omega)]\in H^{2k}_{\mathrm{dR}}(M).
\]

## Remarks

The construction is natural under pullback: if \(f:N\to M\) is smooth, then
\[
c_\Phi(f^*Q)=f^*c_\Phi(Q).
\]

## Examples
1. **First Chern class of a circle bundle.** For a principal \(U(1)\)-bundle, the de Rham class of the curvature form (with conventional normalization) gives the first Chern class \(c_1\in H^2_{\mathrm{dR}}(M)\).

2. **Pontryagin classes.** For an \(SO(n)\)-bundle, Ad-invariant polynomials built from traces of even powers (e.g. \(\mathrm{tr}(X^2)\), \(\mathrm{tr}(X^4)\), etc.) produce the Pontryagin classes \(p_i\in H^{4i}_{\mathrm{dR}}(M)\) via Chern–Weil theory.

3. **Euler class.** For an oriented \(SO(2m)\)-bundle, the Pfaffian polynomial yields a top-degree class in \(H^{2m}_{\mathrm{dR}}(M)\), the Euler class; integrating a representative over a closed base manifold recovers the Euler number.
