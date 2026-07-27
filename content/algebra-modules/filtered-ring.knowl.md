+++
id = "algebra-modules/filtered-ring"
title = "Filtered ring"
kind = "knowl"
summary = "A ring equipped with an increasing multiplicative filtration."
aliases = ["filtered-ring", "Filtered ring"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/filtered-ring.md"
+++

A **filtered ring** is a [[algebra-rings/ring|ring]] \(R\) together with an increasing family of additive subgroups \(\{F_nR\}_{n\in\mathbb Z}\) such that:
- \(F_nR\subseteq F_{n+1}R\) for all \(n\),
- \(1\in F_0R\),
- \(F_nR\cdot F_mR \subseteq F_{n+m}R\) for all \(m,n\),
- often \(\bigcup_n F_nR = R\), in which case the filtration is **exhaustive**.

Filtrations measure “order” or “size” of elements and produce graded approximations via the [[algebra-modules/associated-graded-ring|associated graded ring]]; many structural arguments pass from \(R\) to its graded shadow.

## Examples

- The degree filtration on \(k[x_1,\dots,x_n]\) given by \(F_d=\{\text{polynomials of degree}\le d\}\) is multiplicative.
- The order filtration on a ring of differential operators is increasing and multiplicative.

## Remarks

Some authors instead use decreasing filtrations. For example, the powers \(R\supseteq I\supseteq I^2\supseteq\cdots\) of an ideal form the decreasing \(I\)-adic filtration; its indexing convention should not be confused with the increasing convention above.
