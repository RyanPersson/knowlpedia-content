+++
id = "fiber-bundles/corollary-chernweil-characteristic-classes-are-invariants-of-the-principal-bundle"
title = "Chern–Weil classes are independent of the connection"
kind = "knowl"
summary = "Characteristic classes obtained from invariant polynomials in curvature do not depend on the chosen principal connection."
aliases = ["corollary-chernweil-characteristic-classes-are-invariants-of-the-principal-bundle", "Chern–Weil classes are independent of the connection"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/corollary-chernweil-characteristic-classes-are-invariants-of-the-principal-bundle.md"
+++

Let $\pi:P\to M$ be a principal $G$-bundle, and let $p$ be an $\operatorname{Ad}$-invariant polynomial of degree $k$ on the Lie algebra $\mathfrak g$. The Chern–Weil construction defines a canonical de Rham cohomology class
$$
\mathrm{cw}_p(P)\in H^{2k}_{\mathrm{dR}}(M).
$$
For every [[fiber-bundles/principal-connection|principal connection]] $\omega$ on $P$, the associated Chern–Weil form $\mathrm{CW}_p(\omega)\in\Omega^{2k}(M)$ is closed and represents $\mathrm{cw}_p(P)$. Thus its cohomology class depends only on $P$, not on $\omega$.

## Equivalent formulation

Equivalently, if $\omega_0,\omega_1$ are two connections on $P$, then
$$
\mathrm{CW}_p(\omega_1)-\mathrm{CW}_p(\omega_0)
$$
is an exact [[fiber-bundles/differential-k-form|differential form]] on $M$. Thus Chern–Weil characteristic classes are invariants of the underlying principal bundle.

## Examples
1. **First Chern class of a line bundle.** For a principal $U(1)$-bundle (complex line bundle), choosing $p$ to be the identity on $\mathfrak u(1)$ gives a closed 2-form representing the first Chern class in real cohomology; changing the connection changes the representative by an exact form.
2. **Pontryagin classes.** For a principal $SO(n)$-bundle, invariant polynomials built from traces of powers of curvature produce the Pontryagin classes. For $TM$, this shows Pontryagin classes are independent of the chosen Riemannian metric and its Levi–Civita connection.
3. **Second Chern class for $SU(2)$.** For a principal $SU(2)$-bundle over a 4-manifold, the invariant polynomial $p(X,Y)=\mathrm{tr}(XY)$ yields a 4-form representing the second Chern class (instanton number), independent of the chosen connection.
