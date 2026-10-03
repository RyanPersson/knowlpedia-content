+++
id = "catalog/relationships/spin8-intertwiner-spaces"
title = "Intertwiners between the three Spin(8) modules"
kind = "theorem"
summary = "Equivariant Hom spaces distinguish three real vector spaces of the same dimension."
aliases = ["Intertwiners between the three Spin(8) modules"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/relationships/spin8-vector-representation", "lie-groups/half-spin-representation", "catalog/relationships/triality-and-central-quotients", "algebra-groups/group-action"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

For compact \(G=\operatorname{Spin}(8)\), let \(V,W\) range over its [[catalog/relationships/spin8-vector-representation|vector]] and two real [[lie-groups/half-spin-representation|half-spin]] modules. With the [[algebra-groups/group-action|group action]] fixed,
\[
\operatorname{Hom}_G(V,W)=\{0\}\quad(V\not\cong W),
\qquad \operatorname{End}_G(V)=\mathbb R I,
\qquad \operatorname{Aut}_G(V)=\mathbb R^\times I.
\]
Here \(\{0\}\) contains the zero map; it is not an empty Hom-set. Forgetting the action instead gives, after bases are chosen,
\[
\operatorname{Hom}_{\mathbb R}(V,W)\cong M_8(\mathbb R),
\qquad \operatorname{Aut}_{\mathbb R}(V)\cong GL(8,\mathbb R).
\]

## Direct proof

The three [[catalog/relationships/triality-and-central-quotients|central kernels]] are distinct. Choose a central element acting as \(+I\) on \(V\) and \(-I\) on a different \(W\). Equivariance forces \(T=-T\), hence \(T=0\).

Each action has image \(SO(8)\). If \(T\) commutes with this image, the stabilizer of a unit vector \(v\) forces \(T(v)\) onto its line. Transitivity on the unit sphere then gives a single scalar \(\lambda\) with \(T=\lambda I\). Such a map is invertible exactly when \(\lambda\ne0\).

## Catalogue comparison

Each representation has a view in the category of real \(G\)-modules and a view in real vector spaces. The categorical view chooses which equations a morphism must satisfy; it does not change the underlying eight-dimensional carrier.

## References

1. Laura P. Schaposnik and Sebastian Schulz, “Triality for Homogeneous Polynomials,” §2.2, Proposition 2.1 and Remark 2.2, p. 5. [Paper](https://sigma-journal.com/2021/079/sigma21-079.pdf).
