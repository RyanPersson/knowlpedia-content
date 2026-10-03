+++
id = "catalog/algebras/c-complexified"
title = "Complexification of C"
kind = "definition"
summary = "Catalogue object: Complexification of C; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/complex-numbers-c", "algebra-modules/tensor-product"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **complexified C algebra** is the tensor product
\[
\mathbb C_{\mathbb C}=\mathbb C\otimes_{\mathbb R}\mathbb C,
\qquad (a\otimes z)(b\otimes w)=(ab)\otimes zw,
\]
with complex-linear extension of the product on [[shared-foundations/complex-numbers-c|C]]. Its unit is \(1\otimes1\), and its complex dimension is \(2\).

## Coefficient involution

The composition-algebra conjugation is \(a\otimes z\mapsto\overline a\otimes z\). It is complex-linear: it does not conjugate the new scalar \(z\). The composition norm is the complex quadratic extension of the real norm, not a positive Hermitian norm.

## Split description

It is isomorphic to \(\mathbb C\times\mathbb C\), so its complex dimension is two, not one. In a presentation \(\mathbb C[u]/(u^2+1)\), evaluation at \(u=\pm i\) gives the two factors.

This complexification has real dimension \(4\). It has a different catalogue identity from the original real algebra, and forgetting complex scalar multiplication is a separate category view.

## References

1. [Alberto Elduque, Composition algebras](https://arxiv.org/html/1810.09979), Section 2.1, equation (7); Theorem 2.11 and Corollary 2.12.
