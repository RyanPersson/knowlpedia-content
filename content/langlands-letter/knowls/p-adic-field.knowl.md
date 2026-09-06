+++
id = "langlands-letter/knowls/p-adic-field"
title = "p-adic field"
kind = "knowl"
summary = "A finite extension of Q_p with a discrete valuation, compact valuation ring, and finite residue field."
aliases = ["p-adic-field", "\\(p\\)-Adic Field"]
domains = ["langlands-letter"]
prerequisites = ["algebra-fields-galois/nonarchimedean-local-field", "algebra-fields-galois/valuation-ring", "algebra-rings/maximal-ideal", "algebra-commutative/residue-field", "algebra-fields-galois/finite-field", "algebra-commutative/dvr"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 1
legacy_source_path = "langlands-letter/knowls/p-adic-field.md"
section_mode = "progressive"
+++

A **\(p\)-adic field** is a finite extension \(F/\mathbb Q_p\). It is a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] of characteristic \(0\).

Its normalized discrete valuation

\[
v_F:F^\times\longrightarrow\mathbb Z
\]

determines the [[algebra-fields-galois/valuation-ring|valuation ring]],
[[algebra-rings/maximal-ideal|maximal ideal]], and
[[algebra-commutative/residue-field|residue field]]:

\[
\mathcal O_F=\{x:v_F(x)\geq0\},
\qquad
\mathfrak p_F=\{x:v_F(x)>0\},
\qquad
k_F=\mathcal O_F/\mathfrak p_F.
\]

The residue field is
[[algebra-fields-galois/finite-field|finite]], of cardinality \(q_F=p^f\).
A **[[algebra-commutative/dvr|uniformizer]]** \(\varpi_F\) satisfies
\(v_F(\varpi_F)=1\) and generates
\(\mathfrak p_F\).

## Topology

The ideals \(\mathfrak p_F^n\) form a neighborhood basis of \(0\).
The ring \(\mathcal O_F\) is compact and open, while \(F\) is [[topology/locally-compact-space|locally compact]]
and totally disconnected; its additive group is
[[topology/locally-profinite-group|locally profinite]]. The absolute value
is commonly normalized by

\[
|x|_F=q_F^{-v_F(x)}.
\]

## Scope

Every nonarchimedean local field of characteristic \(0\) is \(p\)-adic.
Local fields of positive characteristic are finite extensions of
\(\mathbb F_q((t))\); they share much of the smooth representation theory
but not every \(p\)-adic Hodge-theoretic construction.

## Langlands role

[[harmonic-analysis/admissible-representation-p-adic-group|Smooth
admissible representations]] of \(G(F)\), the [[langlands/weil-group|Weil]]
and [[langlands/weil-deligne-group|Weil–Deligne]] groups of \(F\),
[[langlands-letter/knowls/maximal-compact-hyperspecial|hyperspecial
subgroups]], and [[langlands/local-l-parameter|local \(L\)-parameters]] form
the nonarchimedean local side of the program.

## References

1. Jean-Pierre Serre, *Local Fields*, Springer, 1979.
