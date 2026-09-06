+++
id = "lie-groups/simply-laced-root-system"
title = "Simply laced root system"
kind = "definition"
summary = "A reduced root system whose Dynkin diagram has only single edges."
aliases = ["simply-laced root system", "simply laced root system", "simply-laced"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/root-system", "lie-groups/dynkin-diagram"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A reduced [[lie-groups/root-system|root system]] \(\Phi\) is **simply laced** if every edge of its [[lie-groups/dynkin-diagram|Dynkin diagram]] is a single unoriented edge. Equivalently, the roots in each irreducible component all have the same length. Different orthogonal components may be rescaled independently, so roots in distinct components need not have equal lengths.

## Classification

The irreducible simply laced root systems are precisely
\[
A_n\ (n\geq 1),\qquad D_n\ (n\geq4),\qquad E_6,E_7,E_8.
\]
Thus “ADE type” and “simply laced type” are synonymous for reduced finite root systems. A reducible root system is simply laced exactly when each irreducible component is of one of these types.

## Root geometry

Normalize an irreducible simply laced system so that \(\langle\alpha,\alpha\rangle=2\) for every root. For distinct nonopposite roots,
\[
\langle\alpha,\beta\rangle\in\{-1,0,1\}.
\]
In particular, orthogonal roots have neither their sum nor their difference as a root. This makes orthogonality especially effective in calculations with [[lie-groups/root-subsystem|root subsystems]] and centralizers.

The classical simply laced families are the [[lie-groups/type-a-root-system|type \(A\)]] and [[lie-groups/type-d-root-system|type \(D\)]] systems; the remaining cases are the [[lie-groups/exceptional-e-root-systems|exceptional \(E\)-type systems]].

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, §§9–12. [Publisher record](https://doi.org/10.1007/978-1-4612-6398-2).
2. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6*, Springer, 2002, Chapter VI, §§1, 4. [Publisher record](https://link.springer.com/book/9783540691716).
3. John C. Baez, “Three Generations in \(E_7\),” 2026, §§3, 5. [arXiv record](https://arxiv.org/abs/2608.06271).
