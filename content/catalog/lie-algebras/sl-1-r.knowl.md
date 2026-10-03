+++
id = "catalog/lie-algebras/sl-1-r"
title = "sl(1,R) — real special linear Lie algebra"
kind = "definition"
summary = "sl(1,R) — real special linear Lie algebra."
aliases = ["sl(1,R) — real special linear Lie algebra"]
domains = ["catalog", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "linear-algebra/matrix", "lie-groups/general-linear-lie-algebra"]
dependency_heuristic = "semantic-catalog-review-v1"
dependency_review_count = 1
+++

The **real special linear [[lie-groups/lie-algebra|Lie algebra]]** \(\mathfrak{sl}(1,\mathbb R)\) is the trace-zero subspace of [[lie-groups/general-linear-lie-algebra|the general linear Lie algebra]], with bracket

\[
\mathfrak{sl}(1,\mathbb R)=\{X\in M_{1}(\mathbb R):\operatorname{tr}X=0\},\qquad [X,Y]=XY-YX.
\]

## Dimension and structure

Trace is one nonzero linear equation, so the real dimension is \(0\). Closure follows from \(\operatorname{tr}(XY)=\operatorname{tr}(YX)\). The trace equation forces the only entry to vanish: this is the zero [[lie-groups/lie-algebra|Lie algebra]], not a [[lie-groups/simple-lie-algebra|simple Lie algebra]].

[[lie-groups/special-linear-lie-algebra|The family definition]] explains its general construction.

## Scalar convention

This record retains \(\mathbb R\) as its defining field. Its complexification is a different catalogue object; a matrix presentation over complex numbers does not change this field automatically.
