+++
id = "differential-geometry/flux-homomorphism"
title = "Flux homomorphism"
kind = "definition"
summary = "The homomorphism sending a symplectic-isotopy class to the integrated cohomology class of its generating contraction forms."
aliases = ["symplectic flux", "flux of a symplectic isotopy"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,\omega)\) be a closed connected [[differential-geometry/symplectic-manifold|symplectic manifold]]. For a [[differential-geometry/symplectic-isotopy|symplectic isotopy]] \(\phi_t\) with generating vector field \(X_t\), its **flux** is
\[
\operatorname{Flux}(\{\phi_t\})
=\left[\int_0^1\iota_{X_t}\omega\,dt\right]
\in H^1_{\mathrm{dR}}(M;\mathbb R).
\]
The contraction one-forms are closed, so the integral defines a class in the first [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology group]]. Flux depends on the homotopy class of the path with endpoints fixed, rather than only on the endpoint.

Consequently it defines a homomorphism
\[
\operatorname{Flux}:
\widetilde{\operatorname{Symp}}_0(M,\omega)
\longrightarrow H^1_{\mathrm{dR}}(M;\mathbb R),
\]
where the domain is the universal covering group of the identity component of the [[differential-geometry/symplectomorphism-group|symplectomorphism group]]. The action of a map isotopic to the identity on cohomology is trivial, which makes the concatenation formula additive.

## Hamiltonian kernel

Every [[differential-geometry/hamiltonian-isotopy|Hamiltonian isotopy]] has zero flux because \(\iota_{X_t}\omega=dH_t\). The converse at the level of path classes is the flux theorem: a symplectic path class has zero flux exactly when it has a Hamiltonian representative with the same endpoints. Thus zero flux is a statement about a relative-endpoint homotopy class, not necessarily about the original parameterized path being pointwise Hamiltonian.

## Descending to endpoints

Loops at the identity may have nonzero flux. Their image is the [[differential-geometry/flux-group|flux group]] \(\Gamma_\omega\). Quotienting by this ambiguity gives an endpoint homomorphism
\[
\overline{\operatorname{Flux}}:
\operatorname{Symp}_0(M,\omega)
\longrightarrow
H^1_{\mathrm{dR}}(M;\mathbb R)/\Gamma_\omega
\]
whose kernel is \(\operatorname{Ham}(M,\omega)\).

## Noncompact variants

The displayed definition uses the closed-manifold convention. For compactly supported isotopies on a noncompact manifold, flux naturally takes values in [[differential-geometry/compactly-supported-de-rham-cohomology|compactly supported de Rham cohomology]], and the kernel and endpoint statements require the corresponding support hypotheses. One should not reuse the closed formula without specifying that variant.

## References

1. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: §10.2, definition and exact sequence for flux.
2. Augustin Banyaga, *The Structure of Classical Diffeomorphism Groups*, Kluwer Academic Publishers, 1997. [DOI record](https://doi.org/10.1007/978-1-4757-0185-3). Relevant: Chapter 7.
