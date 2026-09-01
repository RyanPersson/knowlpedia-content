+++
id = "algebra-modules/elementary-divisor-theorem"
title = "Elementary divisor theorem"
kind = "knowl"
summary = "Over a PID, a finitely generated module decomposes into primary cyclic summands."
aliases = ["elementary-divisor-theorem", "Elementary divisor theorem"]
domains = ["algebra-modules"]
prerequisites = ["algebra-rings/pid"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-modules/elementary-divisor-theorem.md"
+++

Let \(R\) be a [[algebra-rings/pid|principal ideal domain]] and \(M\) a finitely generated \(R\)-module. Then there are an integer \(r\ge0\), prime elements \(p_1,\ldots,p_t\in R\), and positive integers \(e_1,\ldots,e_t\) such that
\[
M \;\cong\; R^{\,r}\;\oplus\;\bigoplus_i R/(p_i^{e_i}),
\]
The integer \(r\) and the multiset of ideals \((p_i^{e_i})\) are uniquely determined by \(M\), up to reordering.

## Relation to invariant factors

This is equivalent to the invariant-factor form of the [[algebra-modules/structure-theorem-pid|structure theorem over a PID]]: factor the invariant factors into prime powers and regroup their primary summands. For \(R=\mathbb Z\), it gives the primary decomposition in the [[algebra-modules/classification-fg-abelian-groups|classification of finitely generated abelian groups]].
