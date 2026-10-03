+++
id = "catalog/algebras/hermitian-corner-inclusion"
title = "Nonunital Hermitian Jordan corner embedding"
kind = "theorem"
summary = "Nonunital Hermitian Jordan corner embedding."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/jordan-algebra-homomorphism"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For integers \(1\leq r<s\), the **upper-left corner map** is
\[
\operatorname{Herm}_r(A)\longrightarrow\operatorname{Herm}_s(A),
\qquad X\longmapsto\begin{pmatrix}X&0\\0&0\end{pmatrix}.
\]
Here both Hermitian spaces must be [[nonassociative-algebra/jordan-algebra|Jordan algebras]] over the same field; for octonionic coefficients require \(s\leq3\). The map is an injective [[nonassociative-algebra/jordan-algebra-homomorphism|Jordan homomorphism]], but it does not preserve the unit.

## Product and unit check

Multiplication of two displayed block matrices has the source product in the upper-left corner and zero elsewhere. This proves preservation of the symmetrized product. The source unit maps to \(\operatorname{diag}(I_r,0)\), which differs from \(I_s\).

Thus the map belongs to \(\mathbf{UJord}\) under the catalogue convention and also to \(\mathbf{Jord}\); it is not a morphism in \(\mathbf{Jord}_1\). This is a change in the permitted arrows, while the source and target remain unital Jordan objects.

## Example

The corner embedding from [[nonassociative-algebra/complex-qubit-jordan-algebra|\(\operatorname{Herm}_2(\mathbb C)\)]] into [[nonassociative-algebra/complex-qutrit-jordan-algebra|\(\operatorname{Herm}_3(\mathbb C)\)]] sends the unit to \(\operatorname{diag}(1,1,0)\). Both objects are real Jordan algebras.
