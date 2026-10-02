+++
id = "catalog/morphisms/gaussian-field-endomorphisms"
title = "Endomorphisms of Q(i) as a rational vector space and algebra"
kind = "example"
summary = "Q(i) has a full 2×2 rational linear endomorphism algebra, but just identity and conjugation as unital rational algebra endomorphisms."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["catalog/categories/vector-spaces", "catalog/categories/unital-associative-algebras"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

For \(A=\mathbb Q(i)\), the basis \((1,i)\) identifies its rational-linear endomorphism algebra and automorphism group with
\[
\operatorname{End}_{\mathbb Q\text{-}\mathbf{Vect}}(A)\cong M_2(\mathbb Q),
\qquad
\operatorname{Aut}_{\mathbb Q\text{-}\mathbf{Vect}}(A)\cong GL_2(\mathbb Q).
\]
In the [[catalog/categories/unital-associative-algebras|unit-preserving rational algebra category]], however,
\[
\operatorname{End}_{\mathbb Q\text{-}\mathbf{Alg}_1}(A)
=\operatorname{Aut}_{\mathbb Q\text{-}\mathbf{Alg}_1}(A)
=\{\operatorname{id},\;a+bi\mapsto a-bi\}.
\]
The latter automorphism group is cyclic of order two.

## Direct proof

A rational-linear map may send the two basis vectors anywhere, giving any \(2\times2\) rational matrix. It is invertible exactly when its determinant is nonzero.

A unital rational algebra map fixes every rational number. Its image of \(i\) must be a root of \(X^2+1\) in \(\mathbb Q(i)\), so is \(i\) or \(-i\). Both choices extend to the displayed automorphisms. If units are not required, the zero map is the only additional algebra endomorphism: a nonzero map sends \(1\) to a nonzero idempotent in a field, hence to \(1\).

## Scalar embeddings as matrices

Multiplication by \(a+bi\) is the rational-linear matrix
\[
\begin{pmatrix}a&-b\\b&a\end{pmatrix}.
\]
These matrices form the endomorphisms linear over \(\mathbb Q(i)\) itself, a proper subalgebra of \(M_2(\mathbb Q)\). Requiring preservation of the algebra unit leaves only multiplication by \(1\) in that scalar-linear family.
