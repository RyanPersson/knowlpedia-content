+++
id = "fiber-bundles/transgression-theorem-p-p-is-exact"
title = "Transgression theorem (Chern–Simons)"
kind = "knowl"
summary = "The difference of Chern–Weil forms for two connections is exact, with an explicit transgression form."
aliases = ["transgression-theorem-p-p-is-exact", "Transgression theorem (Chern–Simons)"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/transgression-theorem-p-p-is-exact.md"
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\pi:Q\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]], let \(\omega_0,\omega_1\) be [[fiber-bundles/principal-connection|principal connections]] with curvatures \(\Omega_0,\Omega_1\), and let \(p\) be an \(\operatorname{Ad}\)-invariant homogeneous polynomial of degree \(k\) on \(\mathfrak g\).

Set \(\eta=\omega_1-\omega_0\) and \(\omega_t=\omega_0+t\eta\), and let \(\Omega_t\) be the curvature of \(\omega_t\). Then
\[
d\,\mathrm{CS}_p(\omega_0,\omega_1)
=\operatorname{cw}_p(\omega_1)-\operatorname{cw}_p(\omega_0),
\]
where
\[
\mathrm{CS}_p(\omega_0,\omega_1)
=k\int_0^1p(\eta,\Omega_t,\dots,\Omega_t)\,dt.
\]
Here the symmetric polarization of \(p\) is evaluated on one \(1\)-form and \(k-1\) curvature \(2\)-forms. Consequently, the de Rham class of \(\operatorname{cw}_p(\omega)\) is independent of \(\omega\).

## Examples
1. **Degree 1 (abelian case).** For \(k=1\) and \(P(X)=X\) (e.g. \(G=U(1)\)), \(\operatorname{cw}_P(\omega)\) is just the curvature \(2\)-form on the base, and the formula becomes \(\operatorname{cw}_P(\omega_1)-\operatorname{cw}_P(\omega_0)=d(A_1-A_0)\) in a local gauge.
2. **Degree 2 (classical 3D Chern–Simons).** For a matrix group and \(P(X)=\mathrm{tr}(X^2)\), the transgression gives the usual \(3\)-form on a trivialization:
   \[
   \mathrm{CS}(A)=\mathrm{tr}\!\left(A\wedge dA+\tfrac23 A\wedge A\wedge A\right),
   \]
   whose exterior derivative is \(\mathrm{tr}(F\wedge F)\).
3. **Gauge-equivalent connections.** If \(\omega_1\) is obtained from \(\omega_0\) by a gauge transformation, then \(\operatorname{cw}_P(\omega_1)-\operatorname{cw}_P(\omega_0)\) is exact; the theorem produces an explicit primitive.
