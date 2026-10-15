+++
id = "catalog/categories/right-modules"
title = "Category of unital right modules"
kind = "definition"
summary = "Category of unital right modules."
aliases = []
domains = ["catalog", "algebra-rings"]
prerequisites = ["algebra-category-theory/category", "catalog/categories/unital-rings"]
+++

Fix a unital ring \(A\), not assumed commutative. The **category \(\mathrm{Mod}\text{-}A\)** has unital right \(A\)-modules as objects: abelian groups \((M,+,0)\) with an action \(M\times A\to M\), written \((m,a)\mapsto ma\), satisfying
\[
m(ab)=(ma)b,\quad m1=m,\quad (m+n)a=ma+na,\quad m(a+b)=ma+mb.
\]
Morphisms \(f:M_A\to N_A\) are additive functions satisfying \(f(ma)=f(m)a\).
Here \(a,b\in A\) and \(m,n\in M\). Composition and identities are those of functions. The displayed linearity identity is preserved by composition and holds for identity maps.

## Catalogue scope

The explorer currently records this category only for the fixed ring [[catalog/algebras/m-2-r|\(A=M_2(\mathbb R)\)]]. It records the regular module on that carrier, with its multiplication action. It does not instantiate categories for arbitrary rings or infer further Hom-spaces. The module unit axiom concerns the action; module maps need not send the ring element \(1\) to itself.

