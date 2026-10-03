+++
id = "catalog/algebras/h-complexified"
title = "Complexification of H"
kind = "definition"
summary = "Catalogue object: Complexification of H; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quaternion-division-algebra", "algebra-modules/tensor-product"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **complexified H algebra** is the tensor product
\[
\mathbb H_{\mathbb C}=\mathbb H\otimes_{\mathbb R}\mathbb C,
\qquad (a\otimes z)(b\otimes w)=(ab)\otimes zw,
\]
with complex-linear extension of the product on [[linear-algebra/quaternion-division-algebra|H]]. Its unit is \(1\otimes1\), and its complex dimension is \(4\).

## Coefficient involution

The composition-algebra conjugation is \(a\otimes z\mapsto\overline a\otimes z\). It is complex-linear: it does not conjugate the new scalar \(z\). The composition norm is the complex quadratic extension of the real norm, not a positive Hermitian norm.

## Split description

It is isomorphic to \(M_2(\mathbb C)\). One explicit realization sends the quaternion generators to \(i\mapsto\operatorname{diag}(i,-i)\) and \(j\mapsto\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\); the four basis images span \(M_2(\mathbb C)\).

This complexification has real dimension \(8\). It has a different catalogue identity from the original real algebra, and forgetting complex scalar multiplication is a separate category view.

## References

1. [Alberto Elduque, Composition algebras](https://arxiv.org/html/1810.09979), Section 2.1, equation (7); Theorem 2.11 and Corollary 2.12.
