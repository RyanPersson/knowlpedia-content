+++
id = "fiber-bundles/regular-asd-connection"
title = "Regular ASD connection"
kind = "definition"
summary = "An anti-self-dual connection whose deformation complex has vanishing obstruction space."
aliases = ["unobstructed instanton", "regular instanton"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(A\) be an [[fiber-bundles/self-dual-and-anti-self-dual-connection|anti-self-dual connection]] on a principal bundle over a closed oriented Riemannian four-manifold. In its [[fiber-bundles/asd-deformation-complex|ASD deformation complex]], let
\[
H_A^2=\operatorname{coker}\!\left(
d_A^+:\Omega^1(X;\operatorname{ad}P)\to
\Omega^{2,+}(X;\operatorname{ad}P)\right).
\]
The connection \(A\) is **regular** if \(H_A^2=0\). Equivalently, after Sobolev completion, the linearization \(d_A^+\) of the ASD equation is surjective. Regularity therefore says that the linearized equation has no obstruction space. It does not assert that \(A\) is [[fiber-bundles/irreducible-connection|irreducible]]: regularity concerns the cokernel of the linearized equation, whereas irreducibility concerns the stabilizer of the gauge action.

## Local consequence

Put the nearby connections \(A+a\) in [[fiber-bundles/coulomb-gauge|Coulomb gauge]] \(d_A^*a=0\). The ASD equation becomes
\[
d_A^+a+(a\wedge a)^+=0.
\]
When \(A\) is regular, the derivative of this equation is surjective, so the Banach-space implicit-function theorem makes the gauge-fixed solution set smooth near \(A\). If \(A\) is also irreducible, the gauge quotient is locally a smooth manifold near \([A]\), with tangent space \(H_A^1\) and the expected dimension [Donaldson–Kronheimer, §§4.2–4.3](https://doi.org/10.1093/oso/9780198535539.001.0001).

## Nonregular connections

When \(H_A^2\ne0\), a finite-dimensional Kuranishi map from a neighborhood of \(0\in H_A^1\) to \(H_A^2\) models the local [[fiber-bundles/anti-self-dual-moduli-space|ASD moduli space]]. Its zero set can be singular even if \(A\) is irreducible. Thus “nonregular” means that the direct implicit-function-theorem argument fails, not that every nearby moduli point must be singular.

## Metric dependence and terminology

Regularity depends on the Riemannian metric because the splitting of two-forms and the operator \(d_A^+\) do. For suitable generic metrics, transversality theorems often make relevant irreducible ASD connections regular, subject to hypotheses on the bundle and four-manifold.

Some sources call \(A\) unobstructed rather than regular. Others reserve “regular moduli space” for a locus on which every connection is both irreducible and unobstructed; that is stronger than the pointwise definition here.

## References

1. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [DOI record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §§4.2–4.3, regularity, Kuranishi models, and local dimensions.
2. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 3, transversality and regular instanton moduli.
