+++
id = "algebra-category-theory/abelian-category"
title = "Abelian category"
kind = "knowl"
summary = "An additive category with kernels and cokernels where exactness behaves like in module categories."
aliases = ["abelian-category", "Abelian category"]
domains = ["algebra-category-theory"]
legacy_source_path = "algebra-category-theory/abelian-category.md"
prerequisites = ["algebra-category-theory/category", "algebra-category-theory/additive-category", "algebra-category-theory/kernel-categorical", "algebra-category-theory/cokernel-categorical", "algebra-category-theory/monomorphism-category", "algebra-category-theory/epimorphism-category", "algebra-category-theory/isomorphism-category"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

An **abelian category** is a [[algebra-category-theory/category|category]] \(\mathcal A\) such that:

1. \(\mathcal A\) is an [[algebra-category-theory/additive-category|additive category]] (in particular, hom-sets are [[algebra-groups/abelian-group|abelian groups]] and finite biproducts exist);
2. every morphism has a [[algebra-category-theory/kernel-categorical|kernel]] and a [[algebra-category-theory/cokernel-categorical|cokernel]];
3. every [[algebra-category-theory/monomorphism-category|monomorphism]] is a kernel of its cokernel, and every [[algebra-category-theory/epimorphism-category|epimorphism]] is a cokernel of its kernel.

These axioms provide an abstract setting for linear algebra, exact sequences, and homological algebra.

## The axioms written out

Unpacking "additive", \(\mathcal A\) is abelian exactly when it satisfies the following.

1. **Preadditivity.** For all objects \(A,B\), the hom-set \(\operatorname{Hom}_{\mathcal A}(A,B)\) is an abelian group, and composition is bilinear (see [[algebra-category-theory/preadditive-category|preadditive category]]).
2. **Zero object.** \(\mathcal A\) has a [[algebra-category-theory/zero-object|zero object]] \(0\), both initial and terminal, so between any two objects there is a zero morphism.
3. **Finite biproducts.** Finite [[algebra-category-theory/categorical-product|products]] and [[algebra-category-theory/coproduct|coproducts]] exist and coincide, so \(A\oplus B\) is both.
4. **Kernels and cokernels.** Every morphism \(f\colon A\to B\) has a kernel \(\ker f\to A\) and a cokernel \(B\to\mathrm{coker}\, f\).
5. **Normal monomorphisms.** Every monomorphism \(m\) is a kernel; equivalently, \(m\cong\ker(\mathrm{coker}\, m)\).
6. **Normal epimorphisms.** Every epimorphism \(e\) is a cokernel; equivalently, \(e\cong\mathrm{coker}(\ker e)\).

In (5) and (6), \(\cong\) is the canonical [[algebra-category-theory/isomorphism-category|isomorphism]] over the common target for kernels and under the common source for cokernels.

## Consequences

In an abelian category:

- one can define [[algebra-category-theory/exact-sequence-categorical|exact sequences]] and do homological algebra;
- every morphism \(f\) admits an “image–coimage” comparison, and the canonical map \(\mathrm{coim}(f)\to \mathrm{im}(f)\) is an isomorphism;
- kernels are monomorphisms and cokernels are epimorphisms, mirroring the familiar situation in \(\mathbf{Ab}\) and \(R\)-modules.

## Examples

1. **\(\mathbf{Ab}\).** The category of abelian groups is abelian.

2. **\(R\text{-}\mathbf{Mod}\).** The category of left modules over a ring \(R\) is abelian.

3. **\(\mathrm{Ch}(R)\).** The category of chain complexes of \(R\)-modules is abelian (kernels and cokernels are computed degreewise).

## Non-examples

- **\(\mathbf{Set}\)** is not abelian (not additive).
- **\(\mathbf{Grp}\)** is not abelian. It is not even additive, since finite products (direct products) and coproducts (free products) differ, and the inclusion of a non-normal subgroup is a monomorphism that is not a kernel.
- **\(\mathbf{Top}\)** is not abelian (again, not additive).
