+++
id = "algebra-rings/semiprime-ideal"
title = "Semiprime ideal"
kind = "knowl"
summary = "An ideal containing no nonzero nilpotent ideal modulo it; in commutative rings, the same as a radical ideal."
aliases = ["semiprime-ideal", "Semiprime ideal"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/two-sided-ideal"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-rings/semiprime-ideal.md"
+++

Let \(R\) be a ring and let \(I\) be a [[algebra-rings/two-sided-ideal|two-sided ideal]]. The ideal \(I\) is **semiprime** if, for every two-sided ideal \(J\subseteq R\),
\[
J^2\subseteq I\quad\Longrightarrow\quad J\subseteq I.
\]

## Remarks

Equivalently, \(R/I\) has no nonzero nilpotent two-sided ideals. In a commutative ring, semiprime ideals are exactly [[algebra-rings/radical-of-ideal|radical ideals]].

## Examples

- In \(k[x,y]\), the ideal \((x)\cap(y)\) is semiprime because it is an intersection of prime ideals.
- In \(\mathbb Z\), the ideal \((6)\) is semiprime because \(6\) is squarefree.
- The ideal \((4)\subseteq\mathbb Z\) is not semiprime, since \((2)^2\subseteq(4)\) but \((2)\nsubseteq(4)\).
