+++
id = "catalog/algebras/o-complexified"
title = "Complexification of O"
kind = "definition"
summary = "Catalogue object: Complexification of O; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/octonion-algebra", "algebra-modules/tensor-product"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **complexified O algebra** is the tensor product
\[
\mathbb O_{\mathbb C}=\mathbb O\otimes_{\mathbb R}\mathbb C,
\qquad (a\otimes z)(b\otimes w)=(ab)\otimes zw,
\]
with complex-linear extension of the product on [[nonassociative-algebra/octonion-algebra|O]]. Its unit is \(1\otimes1\), and its complex dimension is \(8\).

## Coefficient involution

The composition-algebra conjugation is \(a\otimes z\mapsto\overline a\otimes z\). It is complex-linear: it does not conjugate the new scalar \(z\). The composition norm is the complex quadratic extension of the real norm, not a positive Hermitian norm.

## Split description

It is the split octonion algebra over \(\mathbb C\), and remains alternative and nonassociative. A nondegenerate [[linear-algebra/quadratic-form|quadratic form]] in eight variables over \(\mathbb C\) is isotropic, so this algebra is not a division algebra.

This complexification has real dimension \(16\). It has a different catalogue identity from the original real algebra, and forgetting complex scalar multiplication is a separate category view.

## References

1. [Alberto Elduque, Composition algebras](https://arxiv.org/html/1810.09979), Section 2.1, equation (7); Theorem 2.11 and Corollary 2.12.
