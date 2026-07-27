+++
id = "differential-geometry/ricci-form"
title = "Ricci form"
kind = "definition"
summary = "The real closed (1,1)-form obtained from the Ricci curvature of a Kähler metric."
aliases = ["Ricci (1,1)-form", "Kähler Ricci form"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((X,J,g)\) be a complex \(n\)-dimensional manifold with [[differential-geometry/kahler-metric|Kähler metric]], and let \(\operatorname{Ric}_g\) be its [[differential-geometry/ricci-curvature|Ricci tensor]]. The **Ricci form** is the real \(2\)-form
\[
\rho_g(U,V)=\operatorname{Ric}_g(JU,V).
\]
With the convention \(\omega(U,V)=g(JU,V)\), it is a closed form of type \((1,1)\). In local holomorphic coordinates with Hermitian coefficient matrix \((g_{j\bar k})\),
\[
\rho_g=-\,i\,\partial\bar\partial\log\det(g_{j\bar k}).
\]
The signs in both formulas are linked to the curvature convention and must be changed together if the opposite convention is used.

## Curvature interpretation

The Ricci form is the trace of the [[fiber-bundles/chern-curvature|Chern curvature]] of the [[differential-geometry/holomorphic-tangent-bundle|holomorphic tangent bundle]], with the conventional factor of \(i\). Equivalently, its negative is the curvature form of the canonical bundle with its metric induced by \(g\). The local determinant formula follows by taking the trace of the Chern-connection curvature [Huybrechts, §4.2](https://doi.org/10.1007/b137952).

## Cohomology and Einstein metrics

The de Rham class of the Ricci form is metric-independent:
\[
\left[\frac{\rho_g}{2\pi}\right]=c_1(T^{1,0}X)_{\mathbb R}.
\]
Thus changing the Kähler metric changes \(\rho_g\) by an exact real \((1,1)\)-form. A Kähler metric is Kähler–Einstein with Einstein constant \(\lambda\) exactly when \(\rho_g=\lambda\omega\), where \(\omega\) is its [[differential-geometry/kahler-form|Kähler form]]; it is Ricci-flat exactly when \(\rho_g=0\) [Besse, Chapter 2, §G](https://doi.org/10.1007/978-3-540-74311-8).

## Examples and conventions

The Euclidean Kähler metric on \(\mathbb C^n\) has constant coefficient matrix and hence zero Ricci form. The [[differential-geometry/fubini-study-metric|Fubini–Study metric]] on complex projective space has positive Ricci form proportional to its Kähler form. Authors who define \(\omega(U,V)=g(U,JV)\), reverse the sign of the curvature tensor, or normalize \(d^c\) differently may display the opposite local sign.

## References

1. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Springer DOI record](https://doi.org/10.1007/b137952). Relevant: §4.2, Chern curvature, Ricci form, and the first Chern class.
2. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [Springer DOI record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: Chapter 2, §G, Kähler curvature and the Ricci form.
