+++
id = "algebra-category-theory/preadditive-category"
title = "Preadditive category"
kind = "knowl"
summary = "A category whose morphism sets are abelian groups and whose composition is bilinear."
aliases = ["preadditive category", "preadditive"]
domains = ["algebra-category-theory", "algebra-homological"]
prerequisites = ["algebra-category-theory/category", "algebra-category-theory/composition-category"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A [[algebra-category-theory/category|category]] \(\mathcal C\) is **preadditive** if every morphism set \(\operatorname{Hom}_{\mathcal C}(X,Y)\) is an abelian group and composition is bilinear:
\[
(f+g)\circ h=f\circ h+g\circ h,
\qquad
k\circ(f+g)=k\circ f+k\circ g.
\]
In particular, there is a zero morphism between every ordered pair of objects.

An [[algebra-category-theory/additive-category|additive category]] is a preadditive category with finite biproducts. Preadditivity supplies the sums and signs used in complexes and [[algebra-category-theory/distinguished-triangle|distinguished triangles]].
