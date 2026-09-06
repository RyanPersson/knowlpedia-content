+++
id = "algebra-hyperstructures/fusion-rule-for-bands"
title = "Fusion rule for bands"
kind = "definition"
summary = "The cancellation rule that combines two null formal sums containing opposite terms."
aliases = ["fusion axiom for bands", "band fusion rule"]
domains = ["algebra-hyperstructures"]
section_mode = "progressive"
prerequisites = ["algebra-hyperstructures/band"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(B\) be a [[algebra-hyperstructures/band|band]], and let \(I\subseteq
B^+\) be an ideal of formal sums. The **fusion rule** is the closure condition
\[
c+\sum_i a_i\in I,\qquad
-c+\sum_j b_j\in I
\quad\Longrightarrow\quad
\sum_i a_i+\sum_j b_j\in I.
\]
An ideal satisfying this rule is a **fusion ideal**.

For \(S\subseteq B^+\), the notation
\[
\langle\!\langle S\rangle\!\rangle
\]
denotes the smallest fusion ideal containing \(S\). It is obtained by closing
\(S\) under ideal operations and the displayed fusion rule.

## Interpretation

Fusion cancels \(c\) against its unique additive inverse \(-c\) across two
null relations. It is an additional closure axiom: the
[[algebra-hyperstructures/null-set-of-a-band|nullset]] of an arbitrary band
need not be a fusion ideal.

## References
Matthew Baker, Tong Jin, and Oliver Lorscheid,
[*New building blocks for \(\mathbb F_1\)-geometry: bands and band schemes*, Definition 1.6](https://arxiv.org/abs/2402.09612).
