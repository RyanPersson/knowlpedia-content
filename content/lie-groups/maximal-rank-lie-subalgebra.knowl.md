+++
id = "lie-groups/maximal-rank-lie-subalgebra"
title = "Maximal-rank Lie subalgebra"
kind = "definition"
summary = "A subalgebra reductive in its ambient reductive Lie algebra and having the same rank as the ambient algebra."
aliases = ["maximal-rank Lie subalgebra", "subalgebra of maximal rank", "equal-rank Lie subalgebra"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/reductive-lie-algebra", "lie-groups/cartan-subalgebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(\mathfrak g\) be a finite-dimensional complex [[lie-groups/reductive-lie-algebra|reductive Lie algebra]], and let \(\mathfrak k\subseteq\mathfrak g\) be **reductive in \(\mathfrak g\)**, meaning that its adjoint action on \(\mathfrak g\) is completely reducible. The subalgebra \(\mathfrak k\) has **maximal rank** in \(\mathfrak g\) if
\[
\operatorname{rank}\mathfrak k=\operatorname{rank}\mathfrak g,
\]
where the rank of a reductive Lie algebra is the dimension of any of its [[lie-groups/cartan-subalgebra|Cartan subalgebras]].

Equivalently, some Cartan subalgebra of \(\mathfrak k\) is a Cartan subalgebra of \(\mathfrak g\). After conjugating the embedding, one may therefore choose a common Cartan subalgebra
\[
\mathfrak h\subseteq\mathfrak k\subseteq\mathfrak g.
\]

## Root-system description

Relative to a common \(\mathfrak h\), a maximal-rank reductive subalgebra is [[lie-groups/regular-lie-subalgebra|regular]], and its roots form a [[lie-groups/root-subsystem|root subsystem]] of the roots of \(\mathfrak g\). If \(\mathfrak k\) is semisimple, this subsystem has full rank. In general its roots can span a smaller space, with the remaining Cartan directions belonging to the center of \(\mathfrak k\). Every [[lie-groups/levi-subalgebra|Levi subalgebra]] is of maximal rank because it retains the whole ambient Cartan.

There are also maximal-rank semisimple subalgebras that are not Levi subalgebras. A standard exceptional example is
\[
\mathfrak{sl}_2\oplus\mathfrak{so}_{12}\subset\mathfrak e_7,
\]
whose ranks add to \(1+6=7\).

## Distinction from maximality

“Maximal rank” concerns the size of a Cartan subalgebra. It does not assert that \(\mathfrak k\) is a [[lie-groups/maximal-lie-subalgebra|maximal proper Lie subalgebra]]. Conversely, a maximal proper subalgebra can have smaller rank than its ambient algebra.

## References

1. Eugene B. Dynkin, “Semisimple subalgebras of semisimple Lie algebras,” *Matematicheskii Sbornik* 30(72), no. 2 (1952), 349–462; English translation, *AMS Translations*, Series 2, vol. 6 (1957), 111–244. [Journal record](https://www.mathnet.ru/eng/sm5435).
2. John C. Baez, “Three Generations in \(E_7\),” 2026, §6. [arXiv record](https://arxiv.org/abs/2608.06271).
