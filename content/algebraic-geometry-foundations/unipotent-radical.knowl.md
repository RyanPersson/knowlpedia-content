+++
id = "algebraic-geometry-foundations/unipotent-radical"
title = "Unipotent radical"
kind = "definition"
summary = "The largest smooth connected normal unipotent subgroup of a linear algebraic group."
aliases = ["unipotent radical R_u(G)", "R_u(G)", "radical unipotent"]
domains = ["algebraic-geometry-foundations", "algebra-groups", "langlands"]
prerequisites = ["algebraic-geometry-foundations/algebraic-group", "algebraic-geometry-foundations/reductive-algebraic-group", "algebra-groups/normal-subgroup"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For a smooth connected
[[algebraic-geometry-foundations/algebraic-group|linear algebraic group]]
\(H\) over a field \(k\), the
**unipotent radical** \(R_u(H)\) is its largest smooth connected normal
unipotent \(k\)-subgroup.

A connected linear algebraic group is
[[algebraic-geometry-foundations/reductive-algebraic-group|reductive]]
precisely when its geometric
unipotent radical is trivial.  The word “geometric” matters over imperfect
fields: formation of the largest \(k\)-defined unipotent
[[algebra-groups/normal-subgroup|normal subgroup]] need
not detect every unipotent subgroup after extending scalars.

## Parabolic subgroups

If \(P\) is a [[algebraic-geometry-foundations/parabolic-subgroup|parabolic
subgroup]] of a connected reductive group, then \(R_u(P)\) is defined over the
base field and the quotient \(P/R_u(P)\) is reductive.  Choosing a
[[algebraic-geometry-foundations/levi-subgroup|Levi subgroup]] \(M\) splits
this quotient and gives

\[
P=M\ltimes R_u(P).
\]

For \(G=\operatorname{GL}_n\), a standard parabolic consists of block upper
triangular matrices, and its unipotent radical consists of those matrices with
identity diagonal blocks.

## In automorphic forms

Integration over \(R_u(P)(F)\backslash R_u(P)(\mathbb A_F)\), using the
[[langlands-letter/knowls/adeles-restricted-product|adeles]] of the global
field \(F\), defines the
[[langlands/automorphic-constant-term|constant term]] along \(P\).  Vanishing
of these terms for every proper parabolic is the
[[langlands/cuspidal-automorphic-representation|cuspidality]] condition.

## References

1. Brian Conrad, *Reductive Group Schemes*, §§5.2 and 5.4.
   [Author notes](https://math.stanford.edu/~conrad/papers/luminysga3.pdf).
2. Armand Borel, *Linear Algebraic Groups*, second edition, Graduate Texts in
   Mathematics 126, Springer, 1991, §§11 and 14.
