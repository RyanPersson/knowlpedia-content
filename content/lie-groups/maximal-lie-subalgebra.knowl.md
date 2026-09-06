+++
id = "lie-groups/maximal-lie-subalgebra"
title = "Maximal Lie subalgebra"
kind = "definition"
summary = "A proper Lie subalgebra not contained in any other proper Lie subalgebra of the ambient algebra."
aliases = ["maximal Lie subalgebra", "maximal proper Lie subalgebra"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/lie-subalgebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A [[lie-groups/lie-subalgebra|Lie subalgebra]] \(\mathfrak m\subsetneq\mathfrak g\) is a **maximal Lie subalgebra** of \(\mathfrak g\) if every Lie subalgebra \(\mathfrak k\) satisfying
\[
\mathfrak m\subseteq\mathfrak k\subseteq\mathfrak g
\]
is either \(\mathfrak m\) or \(\mathfrak g\). Thus maximality is relative to the chosen embedding and means maximal among **all proper Lie subalgebras**.

## What maximal does not mean

- It does not mean “having the greatest possible dimension”; distinct [[algebra-groups/conjugacy-class|conjugacy classes]] of maximal subalgebras can have different dimensions.
- It does not mean [[lie-groups/maximal-rank-lie-subalgebra|maximal rank]]. Rank and inclusion maximality are independent conditions.
- It does not mean [[lie-groups/maximal-levi-subalgebra|maximal Levi]]. A maximal Levi is maximal only inside the family of proper [[lie-groups/levi-subalgebra|Levi subalgebras]] and is generally contained in a larger proper parabolic subalgebra.
- A maximal subalgebra need not be an [[lie-groups/ideal-lie-algebra|ideal]], so \(\mathfrak g/\mathfrak m\) need not inherit a quotient [[fiber-bundles/lie-bracket|Lie bracket]].

## Adjoint quotient module

The adjoint action of \(\mathfrak m\) preserves \(\mathfrak m\), so it induces a representation on the vector-space quotient \(\mathfrak g/\mathfrak m\):
\[
x\cdot(y+\mathfrak m)=[x,y]+\mathfrak m.
\]
If this \(\mathfrak m\)-module is irreducible, then \(\mathfrak m\) is maximal, because any intermediate Lie subalgebra would give a nonzero proper invariant subspace. The converse need not hold: an invariant subspace of \(\mathfrak g/\mathfrak m\) need not lift to a subalgebra.

## Semisimple ambient algebras

For complex simple ambient algebras, maximal subalgebras include regular examples controlled by root data and nonregular examples arising from [[algebra-representation-theory/irreducible-representation|irreducible representations]]. Dynkin’s classification organizes these possibilities up to [[algebra-groups/inner-automorphism|inner automorphism]].

## References

1. Eugene B. Dynkin, “Semisimple subalgebras of semisimple Lie algebras,” *Matematicheskii Sbornik* 30(72), no. 2 (1952), 349–462; English translation, *AMS Translations*, Series 2, vol. 6 (1957), 111–244. [Journal record](https://www.mathnet.ru/eng/sm5435).
2. Arkady L. Onishchik and Ernest B. Vinberg, eds., *Lie Groups and Lie Algebras III: Structure of Lie Groups and Lie Algebras*, Springer, 1994, Chapter 6. [Publisher record](https://link.springer.com/book/9783540546832).
3. John C. Baez, “Three Generations in \(E_7\),” 2026, §7. [arXiv record](https://arxiv.org/abs/2608.06271).
