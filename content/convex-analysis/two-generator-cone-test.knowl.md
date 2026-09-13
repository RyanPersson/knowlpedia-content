+++
id = "convex-analysis/two-generator-cone-test"
title = "Two-generator cone test"
kind = "theorem"
summary = "An invertible pair of planar generators converts cone membership into two coordinate inequalities."
aliases = []
domains = ["convex-analysis"]
section_mode = "progressive"
prerequisites = ["convex-analysis/positive-span", "linear-algebra/matrix-inverse", "linear-algebra/determinant"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(v_1,v_2\in\mathbb R^2\) be linearly independent and \(H=[v_1\mid v_2]\). Then
\[
T\in\operatorname{pos}\{v_1,v_2\}
\quad\Longleftrightarrow\quad H^{-1}T\in[0,\infty)^2.
\]
Membership in the interior is equivalent to both coefficients being strictly positive. Thus the [[convex-analysis/positive-span|cone]] test is an ordinary matrix inverse followed by componentwise inequalities.

## Oriented determinant form

If \(\det(v_1,v_2)>0\), the coefficients are
\[
y_1=\frac{\det(T,v_2)}{\det(v_1,v_2)},\qquad
y_2=\frac{\det(v_1,T)}{\det(v_1,v_2)}.
\]
Their nonnegativity tests which side of each boundary ray contains \(T\). If the determinant is negative, its sign must be retained in these formulas.
