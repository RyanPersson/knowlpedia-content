+++
id = "fiber-bundles/equivariant-cohomology"
title = "Equivariant cohomology (Cartan model)"
kind = "knowl"
summary = "A cohomology theory for manifolds with a Lie group action, computed by the Cartan complex of equivariant differential forms."
aliases = ["equivariant-cohomology", "Equivariant cohomology (Cartan model)"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/equivariant-cohomology.md"
prerequisites = ["fiber-bundles/lie-group", "lie-groups/lie-algebra-of-a-lie-group", "fiber-bundles/differential-k-form", "fiber-bundles/exterior-derivative", "fiber-bundles/interior-product-contraction-x", "fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold", "lie-groups/exponential-map-lie-group", "lie-groups/adjoint-action-of-a-lie-group", "fiber-bundles/pullback-of-differential-forms", "algebra-modules/symmetric-algebra", "algebra-modules/tensor-product", "algebra-homological/cohomology-module"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let a [[fiber-bundles/lie-group|Lie group]] \(G\) act [[fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold|smoothly]] on \(M\), with [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]] \(\mathfrak g\). Use real [[fiber-bundles/differential-k-form|differential forms]] and the [[algebra-modules/symmetric-algebra|symmetric algebra]] \(S(\mathfrak g^*)\) of the linear dual. Give each linear polynomial degree two. The **Cartan complex** is
\[
\Omega_G^*(M)=\bigl(S(\mathfrak g^*)\otimes_{\mathbb R}\Omega^*(M)\bigr)^G,
\]
where \(\otimes_{\mathbb R}\) is the [[algebra-modules/tensor-product|tensor product]]. An element is a polynomial map \(\alpha:\mathfrak g\to\Omega^*(M)\) satisfying
\[
\alpha(\operatorname{Ad}_g\xi)=(a_{g^{-1}})^*\alpha(\xi),
\qquad a_g(x)=g\cdot x,
\]
using the [[lie-groups/adjoint-action-of-a-lie-group|adjoint action]] and [[fiber-bundles/pullback-of-differential-forms|pullback of forms]]. Total degree is twice polynomial degree plus form degree.

Define the degree-one differential by
\[
(d_G\alpha)(\xi)=d(\alpha(\xi))-\iota_{\xi_M}\alpha(\xi),
\qquad
\xi_M(x)=\left.\frac{d}{dt}\right|_{0}\exp(t\xi)\cdot x,
\]
where \(d\) is the [[fiber-bundles/exterior-derivative|exterior derivative]], \(\iota\) is [[fiber-bundles/interior-product-contraction-x|contraction]], and \(\exp\) is the [[lie-groups/exponential-map-lie-group|exponential map]]. On these invariant polynomial forms, \(d_G^2=0\). The **Cartan equivariant cohomology** is the [[algebra-homological/cohomology-module|cohomology]]
\[
H^*_{G,\mathrm{Cartan}}(M)=H^*(\Omega_G^*(M),d_G).
\]

## Comparison with topological equivariant cohomology

The Borel definition is \(H_G^*(M;R)=H^*(EG\times_GM;R)\), using the [[fiber-bundles/universal-principal-bundle-egbg|universal principal bundle]] and any coefficient ring \(R\). For compact \(G\), the real Cartan complex above computes \(H_G^*(M;\mathbb R)\). Complexifying it computes complex coefficients; real differential forms do not directly compute arbitrary characteristic-zero coefficients, such as \(\mathbb Q\).

For a noncompact group, the Cartan complex is still defined, but this comparison can fail. For example, \(G=(\mathbb R,+)\) acting on a point has Cartan cohomology \(\mathbb R[u]\), with \(\deg u=2\), whereas its Borel cohomology is just \(\mathbb R\) because \(G\) is contractible.

## Examples for compact groups

- **Point:** \(H^*_{G,\mathrm{Cartan}}(\mathrm{pt})=S(\mathfrak g^*)^G\cong H^*(BG;\mathbb R)\).
- **Trivial action:** \(H^*_{G,\mathrm{Cartan}}(M)\cong H^*(M;\mathbb R)\otimes H^*(BG;\mathbb R)\).
- **Free action:** \(H^*_{G,\mathrm{Cartan}}(M)\cong H^*(M/G;\mathbb R)\).

## References

1. Eckhard Meinrenken, “Equivariant cohomology and the Cartan model,” *Encyclopedia of Mathematical Physics* (2006), §§5–6, especially formula (19), Theorem 6.1 and Remark 6.2. [Author's text](https://www.math.toronto.edu/mein/research/enc.pdf).
