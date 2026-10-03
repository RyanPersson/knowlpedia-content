+++
id = "catalog/algebras/hermitian-coefficient-inclusion"
title = "Hermitian Jordan embeddings from coefficient inclusions"
kind = "theorem"
summary = "Hermitian Jordan embeddings from coefficient inclusions."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/standard-composition-inclusions", "nonassociative-algebra/jordan-algebra-homomorphism"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

Let \(A\hookrightarrow B\) be a unital real-algebra inclusion that preserves conjugation, and suppose both Hermitian constructions in size \(m\) are [[nonassociative-algebra/jordan-algebra|Jordan algebras]]. Applying the inclusion to every matrix entry defines an injective unital Jordan map
\[
\operatorname{Herm}_m(A)\hookrightarrow\operatorname{Herm}_m(B).
\]
The [[catalog/algebras/standard-composition-inclusions|standard coefficient inclusions]] give \(\mathbb R\to\mathbb C\to\mathbb H\) for every positive size. The inclusion \(\mathbb H\to\mathbb O\) is used only for \(m\in\{1,2,3\}\).

## Product and unit

Conjugation preservation sends self-adjoint matrices to self-adjoint matrices. Entrywise application commutes with each finite sum and two-factor product in matrix multiplication; hence it preserves \((XY+YX)/2\). Injectivity is checked entrywise, and the identity matrix maps to the identity matrix. These are therefore arrows in \(\mathbf{Jord}_1\), as well as in the two categories with weaker unit policies.

## Choice of coefficients

The complex-to-quaternionic map uses a chosen imaginary quaternion, and the quaternion-to-octonionic map uses a chosen copy of \(\mathbb H\). These are specific embeddings, not a classification of every embedding.
