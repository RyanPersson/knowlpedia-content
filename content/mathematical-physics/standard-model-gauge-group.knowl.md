+++
id = "mathematical-physics/standard-model-gauge-group"
title = "Standard Model gauge group"
kind = "definition"
summary = "The compact internal-symmetry group of the Standard Model, with an important finite central-quotient convention."
aliases = ["Standard Model internal symmetry group", "Standard Model group"]
domains = ["mathematical-physics", "lie-groups"]
prerequisites = []
dependency_review_count = 1
section_mode = "progressive"
+++

In the finite-dimensional internal-symmetry convention, the **Standard Model gauge group** is often written
\[
G_{\mathrm{SM}}^{\mathrm{prod}}=U(1)_Y\times SU(2)_L\times SU(3)_C.
\]
On the known Standard Model particle multiplets, a central subgroup \(\mathbb Z_6\) acts trivially. The corresponding effective group is
\[
G_{\mathrm{SM}}^{\mathrm{eff}}
=G_{\mathrm{SM}}^{\mathrm{prod}}/\mathbb Z_6
\cong S(U(2)\times U(3)).
\]
Both the product and the quotient are called “the Standard Model gauge group”; statements sensitive to global topology must specify the convention.

## The central kernel

The quotient is realized by
\[
\phi:U(1)\times SU(2)\times SU(3)\longrightarrow S(U(2)\times U(3)),
\qquad
\phi(z,A,B)=(z^3A,z^{-2}B).
\]
Its kernel is
\[
\ker\phi=\{(z,z^{-3}I_2,z^2I_3):z^6=1\}\cong\mathbb Z_6.
\]
The codomain is the [[lie-groups/special-block-unitary-group|special block unitary group]].
This finite [[lie-groups/central-quotient-of-a-lie-group|central quotient]] leaves the [[mathematical-physics/standard-model-lie-algebra|Standard Model Lie algebra]] unchanged, but it restricts which [[algebra-representation-theory/group-representation|group representations]] and principal bundles are globally allowed.

## Physics labels

The factors encode [[mathematical-physics/hypercharge|weak hypercharge]], weak isospin acting on left-handed doublets, and color. The subscripts \(Y,L,C\) are physical labels, not additional mathematical operations. The matter representations factor through \(G_{\mathrm{SM}}^{\mathrm{eff}}\).

## Warning: two meanings of gauge group

Here “gauge group” names a compact finite-dimensional **structure group** of internal symmetries. Given a principal \(G_{\mathrm{SM}}\)-bundle \(P\to M\), its [[fiber-bundles/gauge-group|principal-bundle gauge group]] is instead the generally infinite-dimensional group
\[
\mathcal G(P)=\operatorname{Aut}_{G_{\mathrm{SM}}}(P)
\]
of bundle automorphisms covering the identity of spacetime. These groups should not be identified.

## References

1. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv record](https://arxiv.org/abs/0904.1556). Relevant: §§2.3 and 3.1.
2. John C. Baez and Paul Schwahn, “The Standard Model Gauge Group from the Exceptional Jordan Algebra,” 2026. [arXiv record](https://arxiv.org/abs/2606.15235). Relevant: §§1 and 3.
3. John C. Baez, “Three Generations in \(E_7\),” 2026. [arXiv record](https://arxiv.org/abs/2608.06271). Relevant: §§1–2.
