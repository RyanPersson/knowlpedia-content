+++
id = "algebraic-geometry-foundations/sheaf"
title = "Sheaf"
kind = "knowl"
summary = "A system of local data on open sets that can be uniquely glued when compatible."
aliases = ["sheaf"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["topology/topological-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebraic-geometry-foundations/sheaf.md"
+++

Let \(X\) be a [[topology/topological-space|topological space]]. A **sheaf** \(\mathcal F\) on \(X\) assigns an object \(\mathcal F(U)\) to every open set \(U\subseteq X\), together with restriction maps
\[
\mathcal F(U)\longrightarrow \mathcal F(V)\qquad (V\subseteq U),
\]
such that restrictions compose as expected. It must also satisfy two local-to-global conditions. If \(U=\bigcup_i U_i\), then sections over \(U\) are determined by their restrictions to the \(U_i\); and compatible sections \(s_i\in\mathcal F(U_i)\) glue to a unique section \(s\in\mathcal F(U)\).

## Examples

The elements of \(\mathcal F(U)\) are called **sections over \(U\)**. For example, continuous real-valued functions form a sheaf: functions defined on an [[topology/open-cover|open cover]] and agreeing on overlaps glue uniquely. A [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]] similarly records algebraic functions, while a [[algebraic-geometry-foundations/stalk|stalk]] records their germs at one point.
