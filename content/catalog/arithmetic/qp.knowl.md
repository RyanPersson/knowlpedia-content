+++
id = "catalog/arithmetic/qp"
title = "Field Q_p"
kind = "definition"
summary = "Field Q_p with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/completion-at-place", "shared-foundations/p-adic-valuation"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

For a prime \(p\), the **\(p\)-adic number field** \(\mathbb Q_p\) is the [[algebra-fields-galois/completion-at-place|completion]] of \(\mathbb Q\) for \(|x|_p=p^{-v_p(x)}\), where \(v_p\) is the [[shared-foundations/p-adic-valuation|\(p\)-adic valuation]]. It carries the topology from this absolute value.

## Integral elements and topology

The valuation ring is [[shared-foundations/p-adic-integers|\(\mathbb Z_p\)]]. Its [[algebra-rings/maximal-ideal|maximal ideal]] is \(p\mathbb Z_p\), its [[algebra-commutative/residue-field|residue field]] is \(\mathbb F_p\), and \(p\) is a uniformizer. The field is locally compact, complete, nondiscrete and totally disconnected.

## Category distinctions

As a rational algebra it carries a specified inclusion of \(\mathbb Q\), but it has infinite rational dimension. Topological-field morphisms must be continuous as well as preserve field operations. It has characteristic zero; the characteristic of its residue field is a different invariant.

## References

1. [J. S. Milne, Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 7, Theorem 7.23; Propositions 7.26, 7.46; Remark 7.49, pp. 115–127.
