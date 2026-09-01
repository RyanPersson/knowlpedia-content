+++
id = "algebra-rings/simple-ring"
title = "Simple ring"
kind = "knowl"
summary = "A ring with no nontrivial two-sided ideals."
aliases = ["simple-ring", "Simple ring"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/ring", "algebra-rings/two-sided-ideal"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-rings/simple-ring.md"
+++

A **simple ring** is a nonzero [[algebra-rings/ring|ring]] \(R\) whose only [[algebra-rings/two-sided-ideal|two-sided ideals]] are \(0\) and \(R\).

## Remarks

Simple rings are the “atoms” of ring theory: if \(I\) is a nonzero two-sided ideal, then \(R/I\) is a nontrivial [[algebra-rings/quotient-ring|quotient ring]], so simplicity rules out all proper quotients. Standard families of examples are [[algebra-rings/division-ring|division rings]] and [[algebra-rings/matrix-ring|matrix rings]] over them.

## Examples

- If \(D\) is a division ring, then \(D\) is simple.
- For a division ring \(D\) and \(n\ge1\), the ring \(M_n(D)\) is simple.
- \(\mathbb{Z}\) is not simple since \((2)\) is a nontrivial two-sided ideal.
