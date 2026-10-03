+++
id = "catalog/algebras/split-complex-numbers"
title = "Split complex numbers C_s"
kind = "definition"
summary = "Catalogue object: Split complex numbers C_s; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/real-numbers"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **split complex algebra** is \(\mathbb C_s=\mathbb R[e]/(e^2-1)\): its elements are \(a+be\), with \(a,b\in\mathbb R\), and multiplication is
\[
(a+be)(c+de)=(ac+bd)+(ad+bc)e.
\]
Conjugation sends \(a+be\) to \(a-be\), and the multiplicative [[linear-algebra/quadratic-form|quadratic form]] is \(N(a+be)=a^2-b^2\).

## Splitting and zero divisors

The map \(a+be\mapsto(a+b,a-b)\) is a unital real-algebra isomorphism to \(\mathbb R\times\mathbb R\). Its inverse sends \((x,y)\) to \((x+y)/2+(x-y)e/2\). The nonzero factors \(1+e\) and \(1-e\) multiply to zero. Thus “norm” here means an isotropic quadratic form of signature \((1,1)\), not a positive norm and not a normed division algebra.

## One-dimensional boundary

The one-dimensional [[nonassociative-algebra/composition-algebra|composition algebra]] is just \(\mathbb R\), with norm \(a^2\); there is no distinct real one-dimensional isotropic split form. In higher dimensions the split quaternion and split octonion algebras supply the other split Hurwitz algebras.

## References

1. [Alberto Elduque, Composition algebras](https://arxiv.org/html/1810.09979), Section 2.1, equation (7); Theorem 2.11 and Corollary 2.12.
