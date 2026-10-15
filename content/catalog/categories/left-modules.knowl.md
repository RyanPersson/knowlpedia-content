+++
id = "catalog/categories/left-modules"
title = "Category of unital left modules"
kind = "definition"
summary = "Category of unital left modules."
aliases = []
domains = ["catalog", "algebra-rings"]
prerequisites = ["algebra-category-theory/category", "catalog/categories/unital-rings"]
+++

Fix a unital ring \(A\), not assumed commutative. The **category \(A\text{-}\mathrm{Mod}\)** has unital left \(A\)-modules as objects: abelian groups \((M,+,0)\) with an action \(A\times M\to M\), written \((a,m)\mapsto am\), satisfying
\[
(ab)m=a(bm),\quad 1m=m,\quad a(m+n)=am+an,\quad (a+b)m=am+bm.
\]
Morphisms \(f:{}_A M\to {}_A N\) are additive functions satisfying \(f(am)=af(m)\).
Here \(a,b\in A\) and \(m,n\in M\). Composition and identities are those of functions. The displayed linearity identity is preserved by composition and holds for identity maps.

## Catalogue scope

The explorer currently records this category only for the fixed ring [[catalog/algebras/m-2-r|\(A=M_2(\mathbb R)\)]]. It records the regular module on that carrier, with its multiplication action. It does not instantiate categories for arbitrary rings or infer further Hom-spaces. The module unit axiom concerns the action; module maps need not send the ring element \(1\) to itself.

