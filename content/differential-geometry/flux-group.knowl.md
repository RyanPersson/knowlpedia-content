+++
id = "differential-geometry/flux-group"
title = "Flux group"
kind = "definition"
summary = "The subgroup of first cohomology realized as fluxes of loops of symplectomorphisms."
aliases = ["symplectic flux group", "Gamma_omega"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

For a closed connected [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\), the **flux group** is
\[
\Gamma_\omega
=\operatorname{Flux}\!\left(
\pi_1(\operatorname{Symp}_0(M,\omega),\operatorname{id}_M)
\right)
\subseteq H^1_{\mathrm{dR}}(M;\mathbb R).
\]
In words, it is the subgroup of the first [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology group]] consisting of the [[differential-geometry/flux-homomorphism|flux classes]] of loops of symplectomorphisms based at the identity. It is the ambiguity encountered when one tries to assign flux to the endpoint of an isotopy: two paths from the identity to the same symplectomorphism differ by a loop, so their fluxes differ by an element of \(\Gamma_\omega\).

Therefore flux descends to
\[
\overline{\operatorname{Flux}}:
\operatorname{Symp}_0(M,\omega)
\longrightarrow
H^1_{\mathrm{dR}}(M;\mathbb R)/\Gamma_\omega.
\]
Its kernel is the group of [[differential-geometry/hamiltonian-diffeomorphism|Hamiltonian diffeomorphisms]], giving the exact sequence
\[
1\longrightarrow\operatorname{Ham}(M,\omega)
\longrightarrow\operatorname{Symp}_0(M,\omega)
\xrightarrow{\ \overline{\operatorname{Flux}}\ }
H^1_{\mathrm{dR}}(M;\mathbb R)/\Gamma_\omega
\longrightarrow 0.
\]

## Discreteness

For closed symplectic manifolds, \(\Gamma_\omega\) is discrete. This is the \(C^1\)-flux conjecture proved by Ono. As a consequence, \(\operatorname{Ham}(M,\omega)\) is \(C^1\)-closed in \(\operatorname{Symp}_0(M,\omega)\).

If \(H^1_{\mathrm{dR}}(M)=0\), then \(\Gamma_\omega=0\) and every symplectic isotopy beginning at the identity is Hamiltonian up to its path class. On a torus, nontrivial translation loops and isotopies illustrate why the flux group and the quotient cannot generally be omitted.

## Scope

The definition and exact sequence above use a closed manifold. Compactly supported versions for open manifolds replace the groups and cohomology by support-sensitive variants; their flux group is a different object and should be named with its support convention.

## References

1. Kaoru Ono, “Floer–Novikov Cohomology and the Flux Conjecture,” *Geometric and Functional Analysis* 16 (2006), 981–1020. [DOI record](https://doi.org/10.1007/s00039-006-0575-6).
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: §10.2, the flux group and exact sequence.
