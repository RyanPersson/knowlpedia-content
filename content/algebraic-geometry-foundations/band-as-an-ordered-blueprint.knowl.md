+++
id = "algebraic-geometry-foundations/band-as-an-ordered-blueprint"
title = "Band as an ordered blueprint"
kind = "construction"
summary = "The fully faithful, coreflective embedding of bands into ordered blueprints."
aliases = ["ordered blueprint of a band", "bands embedded in ordered blueprints"]
domains = ["algebraic-geometry-foundations", "algebra-hyperstructures", "algebra-category-theory"]
prerequisites = ["algebra-hyperstructures/band", "algebraic-geometry-foundations/ordered-blueprint", "algebra-rings/semiring-homomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(B\) be a [[algebra-hyperstructures/band|band]] with null set \(N_B\). Its associated [[algebraic-geometry-foundations/ordered-blueprint|ordered blueprint]] is
\[
B^{\mathrm{oblpr}}=(B,B^+,\leq),
\]
where \(B\) is the distinguished multiplicative monoid, \(B^+\) is its ambient semiring of formal sums, and the order is determined by
\[
0\leq\sum a_i
\quad\Longleftrightarrow\quad
\sum a_i\in N_B.
\]
A band morphism extends termwise to an order-preserving [[algebra-rings/semiring-homomorphism|semiring homomorphism]], and this construction defines a fully faithful functor
\[
(-)^{\mathrm{oblpr}}:\mathbf{Bands}\hookrightarrow
\mathbf{OBlpr}_{\mathbb F_1^\pm}.
\]

## Coreflection

For an ordered blueprint \(C\) over \(\mathbb F_1^\pm\), define \(C^{\mathrm{band}}\) to have underlying monoid \(C^\bullet\) and null set
\[
N_{C^{\mathrm{band}}}
=
\left\{\sum a_i\ \middle|\ 0\leq\sum a_i\text{ in }C\right\}.
\]
Then \((-)^{\mathrm{band}}\) is right adjoint to \((-)^{\mathrm{oblpr}}\), with natural bijections
\[
\operatorname{Hom}_{\mathbf{OBlpr}}
\bigl(B^{\mathrm{oblpr}},C\bigr)
\cong
\operatorname{Hom}_{\mathbf{Bands}}
\bigl(B,C^{\mathrm{band}}\bigr).
\]
Moreover \((B^{\mathrm{oblpr}})^{\mathrm{band}}=B\). Thus bands form a coreflective full subcategory of ordered blueprints over \(\mathbb F_1^\pm\).

## References
Matthew Baker, Tong Jin, and Oliver Lorscheid, [*New building blocks for \(\mathbb F_1\)-geometry: bands and band schemes*, §1.2.8](https://arxiv.org/abs/2402.09612).
