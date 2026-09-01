+++
id = "algebraic-geometry-foundations/proj"
title = "Proj of a graded ring"
kind = "definition"
summary = "The scheme built from homogeneous prime ideals of a graded ring."
aliases = ["Proj", "Proj construction", "Proj of a graded ring"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebra-modules/graded-ring", "algebra-rings/prime-ideal", "algebraic-geometry-foundations/affine-scheme", "algebra-commutative/localization-ring", "algebraic-geometry-foundations/structure-sheaf", "algebraic-geometry-foundations/projective-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

Let \(S=\bigoplus_{d\ge 0}S_d\) be a commutative [[algebra-modules/graded-ring|graded ring]], and let

\[
S_+:=\bigoplus_{d>0}S_d
\]

be its irrelevant ideal. The space **\(\operatorname{Proj}S\)** consists of the homogeneous [[algebra-rings/prime-ideal|prime ideals]] of \(S\) that do not contain \(S_+\).

For a homogeneous ideal \(I\subseteq S\), the sets

\[
V_+(I):=\{\mathfrak p\in\operatorname{Proj}S:I\subseteq\mathfrak p\}
\]

are the closed sets of its topology. If \(f\in S\) is homogeneous of positive degree, the standard open subset

\[
D_+(f):=\{\mathfrak p:f\notin\mathfrak p\}
\]

is the [[algebraic-geometry-foundations/affine-scheme|affine scheme]]

\[
D_+(f)\cong\operatorname{Spec}(S_f)_0,
\]

where \((S_f)_0\) is the degree-zero part of the [[algebra-commutative/localization-ring|localization]] \(S_f\). These affine pieces determine the [[algebraic-geometry-foundations/structure-sheaf|structure sheaf]] on \(\operatorname{Proj}S\).

For the polynomial ring with its standard grading,

\[
\operatorname{Proj}k[x_0,\ldots,x_n]=\mathbb P_k^n,
\]

the [[algebraic-geometry-foundations/projective-space|projective \(n\)-space]] over \(k\).
