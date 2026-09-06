+++
id = "algebra-homological/mapping-cone"
title = "Mapping cone"
kind = "knowl"
summary = "A complex combining the source and target of a chain map and measuring its failure to be an equivalence."
aliases = ["mapping cone", "cone of a chain map"]
domains = ["algebra-homological", "algebra-category-theory"]
prerequisites = ["algebra-homological/chain-map"]
dependency_review_count = 1
+++

For a [[algebra-homological/chain-map|chain map]] \(f:X^\bullet\to Y^\bullet\), its **mapping cone** is the complex with graded object
\[
\operatorname{Cone}(f)^n=Y^n\oplus X^{n+1}
\]
and differential
\[
d_{\operatorname{Cone}(f)}^n(y,x)
=\bigl(d_Y^n y+f^{n+1}x,\,-d_X^{n+1}x\bigr).
\]
This formula uses cochain complexes; other grading conventions change the displayed signs. The cone fits into a canonical triangle
\[
X\xrightarrow{f}Y\to\operatorname{Cone}(f)\to X[1].
\]

Mapping-cone triangles motivate the [[algebra-category-theory/distinguished-triangle|distinguished triangles]] and the [[algebra-category-theory/octahedral-axiom|octahedral axiom]] of triangulated categories.
