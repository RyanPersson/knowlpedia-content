+++
id = "catalog/morphisms/complex-numbers-linear-versus-algebra-maps"
title = "Endomorphisms of C as a vector space and as an algebra"
kind = "example"
summary = "Real and complex scalar choices, multiplication, and the unit impose different constraints on self-maps of C."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["catalog/categories/vector-spaces", "catalog/categories/associative-algebras", "catalog/categories/unital-associative-algebras"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

The same carrier \(\mathbb C\) has different endomorphism and automorphism collections in the following categories. Here \(k\text{-}\mathbf{Alg}_1\) means [[catalog/categories/unital-associative-algebras|unit-preserving associative algebra maps]].

| Category | Endomorphisms of \(\mathbb C\) | Automorphisms |
| --- | --- | --- |
| Complex [[linear-algebra/vector-space|vector spaces]] | \(z\mapsto az\), \(a\in\mathbb C\) | \(a\ne0\), hence \(\mathbb C^\times\) |
| Real vector spaces | \(z\mapsto az+b\bar z\), \(a,b\in\mathbb C\) | \(|a|^2-|b|^2\ne0\), hence \(GL_2(\mathbb R)\) |
| \(\mathbb C\text{-}\mathbf{Alg}_1\) | identity only | identity only |
| \(\mathbb R\text{-}\mathbf{Alg}_1\) | identity and conjugation | identity and conjugation |

In the two arbitrary-map associative-algebra categories, add the zero map to the endomorphism sets in the last two rows. The automorphism groups do not change.

## Verification of the linear rows

A complex-linear map is determined by its value at \(1\). A real-linear map is determined by \(T(1)\) and \(T(i)\); solving for \(a,b\) gives
\[
a=\frac{T(1)-iT(i)}2,\qquad b=\frac{T(1)+iT(i)}2.
\]
The real determinant is \(|a|^2-|b|^2\). Thus all real-linear endomorphisms form \(M_2(\mathbb R)\) after choosing the basis \((1,i)\).

## Verification of the algebra rows

A unital real algebra map fixes \(\mathbb R\), and its value at \(i\) must square to \(-1\). The only choices in \(\mathbb C\) are \(i\) and \(-i\), producing identity and conjugation. A complex-linear unital map must fix \(i\), leaving only identity. For a nonzero multiplicative map, the image of \(1\) is a nonzero idempotent in the field \(\mathbb C\), hence equals \(1\); the only additional arbitrary-map possibility is zero.

## Jordan views

Since \(\mathbb C\) is commutative, its ordinary product is already its Jordan product. The same algebra classifications therefore apply in the corresponding real or complex Jord, UJord, and [[catalog/categories/unital-jordan-algebras-unital-maps|Jord1 categories]], with their specified unit policies.
