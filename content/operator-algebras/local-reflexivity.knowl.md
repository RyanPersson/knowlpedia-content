+++
id = "operator-algebras/local-reflexivity"
title = "Local reflexivity for C*-algebras"
kind = "definition"
summary = "Finite-dimensional pieces of a C*-algebra's bidual can be approximated inside the algebra with asymptotically optimal matrix norm."
aliases = ["locally reflexive C*-algebra"]
domains = ["operator-algebras", "functional-analysis"]
prerequisites = ["operator-algebras/cstar-algebra", "linear-algebra/linear-map", "operator-algebras/completely-bounded-map"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] \(A\) is **locally
reflexive** if, whenever \(E\subseteq A^{**}\) and \(F\subseteq A^*\) are
finite-dimensional and \(\varepsilon>0\), there is a [[linear-algebra/linear-map|linear map]]
\(\phi:E\to A\) such that
\[
\|\phi\|_{\mathrm{cb}}\leq 1+\varepsilon,\qquad
f(\phi(x))=x(f)\quad(x\in E,\ f\in F),
\]
and \(\phi(x)=x\) for \(x\in E\cap A\). Here
\(\|\cdot\|_{\mathrm{cb}}\) is the
[[operator-algebras/completely-bounded-map|completely bounded norm]]. The
property says that finite-dimensional operator-space data in the bidual can
be realized almost isometrically in \(A\), while matching any prescribed
finite collection of dual pairings. No global bounded projection from
\(A^{**}\) onto \(A\) is asserted by this definition.

## Approximation formulation

Equivalently, for each finite-dimensional \(E\subseteq A^{**}\), the
inclusion \(E\hookrightarrow A^{**}\) is a point weak-star limit of maps
\(E\to A\) whose completely bounded norms tend to \(1\), with the maps
fixing \(E\cap A\). Passing between this net formulation and the finite set
\(F\subseteq A^*\) formulation is a finite-dimensional separation argument.
The matrix norm is essential: ordinary Banach-space local reflexivity holds
for every [[linear-algebra/banach-space|Banach space]], while operator-space local reflexivity is a genuine
restriction.

## Relation to exactness

Every [[operator-algebras/exact-cstar-algebra|exact \(C^*\)-algebra]] is
locally reflexive. In particular, nuclear \(C^*\)-algebras are locally
reflexive. Local reflexivity is nevertheless weaker than exactness; it
controls finite-dimensional approximation from the bidual rather than the
behavior of all [[algebra-modules/short-exact-sequence|short exact sequences]] under minimal tensor product.

One tensorial formulation says that the natural comparison maps involving
finite-dimensional operator spaces and \(A^{**}\) preserve the minimal
operator-space norm. Such formulations make local reflexivity useful in
passing approximation and lifting arguments between \(A\), its
representations, and its weak closures.

## Conventions

Some sources define local reflexivity for an arbitrary operator space \(X\)
and then apply that definition to the canonical operator-space structure of
a \(C^*\)-algebra. The interpolation requirement
\(\phi|_{E\cap A}=\operatorname{id}\) may be omitted from an equivalent
version; it can be restored without changing the property.

## References

1. Edward G. Effros and Uffe Haagerup, “Lifting problems and local reflexivity for \(C^*\)-algebras,” *Duke Mathematical Journal* 52 (1985), 103–128. [Project Euclid DOI record](https://doi.org/10.1215/S0012-7094-85-05207-X). Relevant: local reflexivity and its relation to lifting and tensor products.
2. Nathanial P. Brown and Narutaka Ozawa, *\(C^*\)-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [AMS DOI record](https://doi.org/10.1090/gsm/088). Relevant: §9.2 on local reflexivity and exact \(C^*\)-algebras.
