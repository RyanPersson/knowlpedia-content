+++
id = "algebra-homological/mapping-cone"
title = "Mapping cone"
kind = "knowl"
summary = "A complex combining the source and target of a chain map and measuring its failure to be an equivalence."
aliases = ["mapping cone", "cone of a chain map"]
domains = ["algebra-homological", "algebra-category-theory"]
+++

For a [[algebra-homological/chain-map|chain map]] \(f:X^\bullet\to Y^\bullet\), its **mapping cone** is the complex with graded object
\[
\operatorname{Cone}(f)^n=Y^n\oplus X^{n+1}
\]
and differential built from the differentials of \(X\) and \(Y\) together with \(f\), with signs determined by the grading convention. It fits into a canonical triangle
\[
X\xrightarrow{f}Y\to\operatorname{Cone}(f)\to X[1].
\]

Mapping-cone triangles motivate the [[algebra-category-theory/distinguished-triangle|distinguished triangles]] and the [[algebra-category-theory/octahedral-axiom|octahedral axiom]] of triangulated categories.
