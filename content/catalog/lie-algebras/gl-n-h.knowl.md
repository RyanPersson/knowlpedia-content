+++
id = "catalog/lie-algebras/gl-n-h"
title = "gl(n,H) — quaternionic general linear Lie algebra"
kind = "definition"
summary = "gl(n,H) — quaternionic general linear Lie algebra."
aliases = ["gl(n,H) — quaternionic general linear Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

For an integer \(n\geq1\), the **quaternionic general linear [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{gl}(n,\mathbb H)\) is the real [[linear-algebra/vector-space|vector space]]

\[
\mathfrak{gl}(n,\mathbb H)=M_{n}(\mathbb H),\qquad [X,Y]=XY-YX.
\]

## Trace and scalar conventions

Quaternionic matrix multiplication is associative, so its commutator is a real [[fiber-bundles/lie-bracket|Lie bracket]]. Each quaternionic entry has four real coordinates, giving the displayed dimension.

Quaternionic entries do not make this a [[lie-groups/lie-algebra|Lie algebra]] over a commutative field \(\mathbb H\). All scalar-linear categories in this record are over \(\mathbb R\).
