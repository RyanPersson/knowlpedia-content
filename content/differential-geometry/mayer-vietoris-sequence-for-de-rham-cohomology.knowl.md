+++
id = "differential-geometry/mayer-vietoris-sequence-for-de-rham-cohomology"
title = "Mayer–Vietoris sequence for de Rham cohomology"
kind = "theorem"
summary = "An open two-set cover produces a long exact sequence relating the de Rham cohomology of the manifold, the two open sets, and their intersection."
aliases = ["de Rham Mayer–Vietoris sequence"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M=U\cup V\) be a [[topology/open-cover|cover by two open sets]] of a [[fiber-bundles/smooth-manifold|smooth manifold]]. Restriction and difference of restrictions give a [[algebra-modules/short-exact-sequence|short exact sequence]] of [[differential-geometry/de-rham-complex|de Rham complexes]]
\[
0\longrightarrow\Omega^\bullet(M)\longrightarrow
\Omega^\bullet(U)\oplus\Omega^\bullet(V)\longrightarrow
\Omega^\bullet(U\cap V)\longrightarrow0.
\]
The associated cohomology sequence is exact:
\[
\cdots\to H_{\mathrm{dR}}^k(M)\to H_{\mathrm{dR}}^k(U)\oplus H_{\mathrm{dR}}^k(V)
\to H_{\mathrm{dR}}^k(U\cap V)\xrightarrow{\delta}
H_{\mathrm{dR}}^{k+1}(M)\to\cdots.
\]
This is the **Mayer–Vietoris sequence for de Rham cohomology**. Its connecting
homomorphism measures the obstruction to obtaining a class on \(U\cap V\) as
the difference of classes restricted from \(U\) and \(V\).

## Exactness and the connecting map

The last map of complexes sends \((\alpha,\beta)\) to
\(\alpha|_{U\cap V}-\beta|_{U\cap V}\). Its surjectivity follows from a
[[fiber-bundles/partition-of-unity-subordinate-to-an-open-cover|partition of unity subordinate to the cover]]. If a closed form \(\omega\) on \(U\cap V\) is the difference of restrictions of \((\alpha,\beta)\), then \(d\alpha\) and \(d\beta\) agree on the overlap and glue to a global closed form \(\eta\). The connecting homomorphism is \(\delta[\omega]=[\eta]\).

## Use in calculations

If \(U\), \(V\), and \(U\cap V\) have known cohomology, exactness often determines the [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology]] of \(M\). This is the differential-form analogue of the Mayer–Vietoris sequence in [[topology/singular-cohomology-group|singular cohomology]] and is a principal gluing step in one proof of the [[differential-geometry/de-rham-theorem|de Rham theorem]] [Bott and Tu, de Rham theory](https://doi.org/10.1007/978-1-4757-3951-0).

## Naturality and sign convention

A [[fiber-bundles/smooth-map|smooth map]] compatible with two chosen covers induces a morphism of the corresponding long exact sequences. Reversing the difference map from \(\alpha-\beta\) to \(\beta-\alpha\) changes the displayed connecting map by a sign but does not change exactness. The convention must therefore be fixed when explicit representatives are compared.

## References

1. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter I, the Mayer–Vietoris sequence and de Rham theorem.
2. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: the chapter on de Rham theory and Mayer–Vietoris arguments.
