+++
id = "lie-groups/central-quotient-of-a-lie-group"
title = "Central quotient of a Lie group"
kind = "definition"
summary = "A Lie-group quotient by a closed subgroup of the center."
aliases = ["central quotient", "quotient by a central subgroup"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] and let \(Z\) be a closed subgroup of its [[lie-groups/center-of-a-lie-group|center]]. The **central quotient of \(G\) by \(Z\)** is the [[lie-groups/quotient-lie-group|quotient Lie group]]
\[
G/Z,
\]
whose multiplication is \((gZ)(hZ)=ghZ\). Centrality makes \(Z\) normal, and closedness gives the [[lie-groups/coset-space|coset space]] its canonical smooth Lie-group structure.

## Infinitesimal effect

If \(\mathfrak z=\operatorname{Lie}(Z)\), then
\[
\operatorname{Lie}(G/Z)\cong \mathfrak g/\mathfrak z.
\]
When \(Z\) is discrete—for example, finite—the quotient map \(G\to G/Z\) is a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]] and the two groups have isomorphic [[lie-groups/lie-algebra|Lie algebras]]. A finite central quotient can therefore change global topology and available representations without changing the infinitesimal symmetry algebra.

## Representations

A [[algebra-representation-theory/group-representation|representation]] \(\rho:G\to GL(V)\) descends to \(G/Z\) exactly when \(Z\subseteq\ker\rho\). Equivalently, representations of \(G/Z\) are representations of \(G\) on which every element of \(Z\) acts trivially.

## Example

The effective [[mathematical-physics/standard-model-gauge-group|Standard Model internal symmetry group]] is often written
\[
\bigl(U(1)\times SU(2)\times SU(3)\bigr)/\mathbb Z_6.
\]
The central \(\mathbb Z_6\) acts trivially in the one-generation Standard Model representation, and the quotient is isomorphic to [[lie-groups/special-block-unitary-group|\(S(U(2)\times U(3))\)]].

## References

1. Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, second edition, Springer, 2015. [DOI record](https://doi.org/10.1007/978-3-319-13467-3). Relevant: quotient Lie groups and covering homomorphisms.
2. John C. Baez and John Huerta, “The Algebra of Grand Unified Theories,” *Bulletin of the American Mathematical Society* 47 (2010), 483–552. [arXiv record](https://arxiv.org/abs/0904.1556). Relevant: §3.1.
