+++
id = "lie-groups/complete-filtered-lie-algebra"
title = "Complete filtered Lie algebra"
kind = "definition"
summary = "A Lie algebra complete for a bracket-compatible descending filtration."
aliases = ["complete descendingly filtered Lie algebra", "pronilpotent filtered Lie algebra"]
domains = ["lie-groups", "algebra-topological"]
prerequisites = ["algebra-rings/field", "lie-groups/lie-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(k\) be a [[algebra-rings/field|field]]. A **complete filtered Lie
algebra** is a [[lie-groups/lie-algebra|\(k\)-Lie algebra]] \(\mathfrak g\)
with a descending filtration
\[
\mathfrak g=F^1\mathfrak g\supseteq F^2\mathfrak g\supseteq\cdots
\]
such that
\[
[F^p\mathfrak g,F^q\mathfrak g]\subseteq F^{p+q}\mathfrak g
\quad(p,q\geq1)
\]
and the canonical map
\[
\mathfrak g\longrightarrow
\varprojlim_n\mathfrak g/F^n\mathfrak g
\]
is an isomorphism. Thus the filtration is separated and complete, and Lie
brackets increase filtration degree.

## Pronilpotence

For the convention \(F^1\mathfrak g=\mathfrak g\), each quotient
\(\mathfrak g/F^n\mathfrak g\) is a [[lie-groups/nilpotent-lie-algebra|nilpotent
Lie algebra]] of class at most \(n-1\). The complete filtered algebra is
therefore an inverse limit of nilpotent Lie algebras and is commonly called
**pronilpotent**.

Some authors define a pronilpotent Lie algebra abstractly as an inverse limit
of nilpotent Lie algebras, without choosing one filtration. A chosen complete
bracket-compatible filtration is stronger data and is the convention used
here.

## Convergence

A series \(\sum_{n\geq1}x_n\) with \(x_n\in F^n\mathfrak g\) converges:
its image in every quotient \(\mathfrak g/F^r\mathfrak g\) is a finite sum,
and completeness gives a unique compatible limit. In particular, any formal
Lie series whose terms of bracket length \(n\) lie in \(F^n\mathfrak g\)
can be evaluated in \(\mathfrak g\).

This makes the [[lie-groups/baker-campbell-hausdorff-formula|Baker–Campbell–Hausdorff
series]] convergent when \(k\) has characteristic zero, producing the
associated [[formal-groups/complete-filtered-lie-algebra-bch-group|BCH group]].

## Morphisms

A morphism of complete filtered Lie algebras is a continuous Lie-algebra
homomorphism \(f:\mathfrak g\to\mathfrak h\) satisfying
\(f(F^n\mathfrak g)\subseteq F^n\mathfrak h\) for every \(n\). Such a map
commutes with evaluation of convergent formal Lie series.

## Examples

- A nilpotent Lie algebra \(\mathfrak n\), equipped with its lower central
  series and extended by zeros, is complete filtered.
- If \(\mathfrak g\) is any Lie algebra, the completion
  \(\varprojlim_n\mathfrak g/\gamma_n(\mathfrak g)\) of its lower central
  series is pronilpotent when the transition maps and brackets satisfy the
  indicated separatedness conditions.

## References

1. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 1–3*, Springer, 1989. [Publisher record](https://doi.org/10.1007/978-3-540-64242-8). Relevant: Chapter II, §§6–7 on formal Lie series and complete filtered algebras.
2. Jean-Pierre Serre, *Lie Algebras and Lie Groups*, Lecture Notes in Mathematics 1500, Springer, 1992. [Publisher record](https://doi.org/10.1007/978-3-540-70634-2). Relevant: Part II on the Campbell–Hausdorff formula and formal groups.
