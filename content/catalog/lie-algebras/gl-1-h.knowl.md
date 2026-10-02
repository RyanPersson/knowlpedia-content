+++
id = "catalog/lie-algebras/gl-1-h"
title = "gl(1,H) — quaternionic general linear Lie algebra"
kind = "definition"
summary = "gl(1,H) — quaternionic general linear Lie algebra."
aliases = ["gl(1,H) — quaternionic general linear Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **quaternionic general linear [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{gl}(1,\mathbb H)\) is the real [[linear-algebra/vector-space|vector space]]

\[
\mathfrak{gl}(1,\mathbb H)=M_{1}(\mathbb H),\qquad [X,Y]=XY-YX.
\]

## Trace and scalar conventions

Quaternionic matrix multiplication is associative, so its commutator is a real [[fiber-bundles/lie-bracket|Lie bracket]]. Each quaternionic entry has four real coordinates, giving the displayed dimension.

Quaternionic entries do not make this a [[lie-groups/lie-algebra|Lie algebra]] over a commutative field \(\mathbb H\). All scalar-linear categories in this record are over \(\mathbb R\).
