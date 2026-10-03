+++
id = "catalog/morphisms/jordan-maps-from-the-scalar-algebra"
title = "Jordan maps from the scalar algebra are idempotents"
kind = "theorem"
summary = "A Jordan homomorphism k→J is determined by an idempotent image of 1; unit preservation selects the unit."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["catalog/categories/jordan-algebras", "nonassociative-algebra/jordan-idempotent"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

Let \(k\) be a field of characteristic different from \(2\), viewed as a [[nonassociative-algebra/jordan-algebra|Jordan algebra]] with ordinary multiplication, and let \(J\) be a Jordan \(k\)-algebra. Evaluation at \(1\) is a bijection
\[
\operatorname{Hom}_{\mathbf{Jord}_k}(k,J)
\longleftrightarrow \{e\in J:e\circ e=e\},
\qquad f\longmapsto f(1).
\]
The inverse sends an [[nonassociative-algebra/jordan-idempotent|idempotent]] \(e\) to \(t\mapsto te\). If \(J\) is unital, the same description holds in [[catalog/categories/unital-jordan-algebras-arbitrary-maps|UJord]], whereas [[catalog/categories/unital-jordan-algebras-unital-maps|Jord1]] contains exactly the map \(t\mapsto t1_J\).

## Proof

Linearity forces \(f(t)=tf(1)\). Preservation of \(1\circ1=1\) requires \(e\circ e=e\). Conversely, if \(e\) is idempotent, bilinearity gives \((se)\circ(te)=st e\), so the map preserves products. It preserves units precisely when \(e=1_J\).

## The complex qubit algebra

For \(J=\operatorname{Herm}_2(\mathbb C)\), as a real Jordan algebra, idempotents are Hermitian projection matrices. They are \(0\), \(I_2\), and [[quantum-foundations/rank-one-projector|rank-one projections]]
\[
p=uu^*,\qquad u\in\mathbb C^2,\qquad u^*u=1.
\]
Vectors differing by a unit complex scalar give the same projection. Thus the real Jordan Hom-set is parametrized by two [[real-analysis/isolated-point|isolated points]] together with \(\mathbb{CP}^1\); only \(I_2\) gives a unit-preserving map. This is a complete classification of these maps, not of all endomorphisms of the qubit algebra.
